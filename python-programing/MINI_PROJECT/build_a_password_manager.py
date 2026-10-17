
import os
import json
import base64
import secrets
import string
import hashlib
import hmac

from pathlib import Path
from getpass import getpass

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


# -------------------------------
# FILE CONFIGURATION
# -------------------------------

DATA_DIR = Path.home() / ".python_password_manager"
DATA_DIR.mkdir(parents=True, exist_ok=True)

VAULT_FILE = DATA_DIR / "vault.json"
SALT_FILE = DATA_DIR / "salt.bin"
CHECK_FILE = DATA_DIR / "master_check.bin"

ITERATIONS = 600_000


# -------------------------------
# KEY GENERATION
# -------------------------------

def derive_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS
    )

    key = kdf.derive(master_password.encode("utf-8"))

    return base64.urlsafe_b64encode(key)


# -------------------------------
# MASTER PASSWORD SETUP
# -------------------------------

def setup_master_password():
    print("\n=== Create Master Password ===")

    while True:
        password = getpass("Create master password: ")

        if len(password) < 12:
            print("Use at least 12 characters.")
            continue

        confirm = getpass("Confirm master password: ")

        if password != confirm:
            print("Passwords do not match.")
            continue

        salt = os.urandom(16)
        key = derive_key(password, salt)

        verifier = Fernet(key).encrypt(
            b"password-manager-unlocked"
        )

        # Save setup files securely where supported.
        SALT_FILE.write_bytes(salt)
        CHECK_FILE.write_bytes(verifier)

        print("\nMaster password created successfully!")

        return Fernet(key)


# -------------------------------
# MASTER PASSWORD LOGIN
# -------------------------------

def login():
    if not SALT_FILE.exists() or not CHECK_FILE.exists():
        return setup_master_password()

    print("\n=== Password Manager Login ===")

    for attempt in range(3):
        password = getpass("Enter master password: ")

        salt = SALT_FILE.read_bytes()
        key = derive_key(password, salt)

        try:
            verifier = Fernet(key).decrypt(
                CHECK_FILE.read_bytes()
            )

            if verifier == b"password-manager-unlocked":
                print("\nLogin successful!")
                return Fernet(key)

        except InvalidToken:
            pass

        print("Incorrect master password.")

    print("Too many failed attempts. Exiting.")
    raise SystemExit


# -------------------------------
# LOAD ENCRYPTED VAULT
# -------------------------------

def load_vault(cipher):
    if not VAULT_FILE.exists():
        return []

    try:
        encrypted_data = VAULT_FILE.read_bytes()
        decrypted_data = cipher.decrypt(encrypted_data)

        return json.loads(decrypted_data.decode("utf-8"))

    except (InvalidToken, json.JSONDecodeError, UnicodeDecodeError):
        print("Vault could not be decrypted or is corrupted.")
        raise SystemExit(1)


# -------------------------------
# SAVE ENCRYPTED VAULT
# -------------------------------

def save_vault(cipher, vault):
    data = json.dumps(vault, indent=4).encode("utf-8")
    encrypted_data = cipher.encrypt(data)

    temp_file = VAULT_FILE.with_suffix(".tmp")

    try:
        temp_file.write_bytes(encrypted_data)
        os.replace(temp_file, VAULT_FILE)

    finally:
        if temp_file.exists():
            temp_file.unlink()


# -------------------------------
# ADD PASSWORD
# -------------------------------

def add_password(cipher, vault):
    print("\n=== Add New Account ===")

    website = input("Website: ").strip()
    username = input("Username or Email: ").strip()

    if not website or not username:
        print("Website and username are required.")
        return

    password = getpass("Account password: ")

    if not password:
        print("Password cannot be empty.")
        return

    entry = {
        "website": website,
        "username": username,
        "password": password
    }

    vault.append(entry)
    save_vault(cipher, vault)

    print("Account saved securely!")


# -------------------------------
# VIEW PASSWORDS
# -------------------------------

def view_passwords(vault):
    print("\n=== Saved Accounts ===")

    if not vault:
        print("No accounts saved yet.")
        return

    for index, entry in enumerate(vault, start=1):
        print(f"\nAccount {index}")
        print("Website:", entry["website"])
        print("Username:", entry["username"])
        print("Password: [Hidden]")


# -------------------------------
# SEARCH PASSWORD
# -------------------------------

def search_password(vault):
    print("\n=== Search Account ===")

    query = input("Enter website name: ").strip().casefold()

    if not query:
        print("Enter a website name.")
        return

    matches = [
        entry for entry in vault
        if query in entry["website"].casefold()
    ]

    if not matches:
        print("No matching account found.")
        return

    for index, entry in enumerate(matches, start=1):
        print(f"\nResult {index}")
        print("Website:", entry["website"])
        print("Username:", entry["username"])

        reveal = input("Reveal password? (y/n): ").strip().lower()

        if reveal == "y":
            print("Password:", entry["password"])


# -------------------------------
# GENERATE STRONG PASSWORD
# -------------------------------

def generate_password():
    print("\n=== Password Generator ===")

    try:
        length = int(input("Password length (12-64): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 12 <= length <= 64:
        print("Choose a length between 12 and 64.")
        return

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"

    # Ensure every character category is represented.
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols

    password_chars.extend(
        secrets.choice(all_chars)
        for _ in range(length - len(password_chars))
    )

    # Securely shuffle the generated characters.
    secrets.SystemRandom().shuffle(password_chars)

    password = "".join(password_chars)

    print("\nGenerated Password:", password)
    print("Save it somewhere secure if you want to keep it.")


# -------------------------------
# DELETE ACCOUNT
# -------------------------------

def delete_password(cipher, vault):
    print("\n=== Delete Account ===")

    if not vault:
        print("No accounts to delete.")
        return

    for index, entry in enumerate(vault, start=1):
        print(f"{index}. {entry['website']} - {entry['username']}")

    try:
        choice = int(input("Enter account number to delete: "))
    except ValueError:
        print("Enter a valid account number.")
        return

    if not 1 <= choice <= len(vault):
        print("Invalid account number.")
        return

    confirm = input(
        f"Delete {vault[choice - 1]['website']}? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    vault.pop(choice - 1)
    save_vault(cipher, vault)

    print("Account deleted successfully!")


# -------------------------------
# MAIN MENU
# -------------------------------

def main():
    print("=" * 40)
    print("       PYTHON PASSWORD MANAGER")
    print("=" * 40)

    cipher = login()
    vault = load_vault(cipher)

    while True:
        print("\n" + "=" * 40)
        print("1. Add Password")
        print("2. View Saved Accounts")
        print("3. Search Account")
        print("4. Generate Strong Password")
        print("5. Delete Account")
        print("6. Exit")
        print("=" * 40)

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_password(cipher, vault)

        elif choice == "2":
            view_passwords(vault)

        elif choice == "3":
            search_password(vault)

        elif choice == "4":
            generate_password()

        elif choice == "5":
            delete_password(cipher, vault)

        elif choice == "6":
            print("Vault locked. Goodbye!")
            break

        else:
            print("Invalid choice. Select 1-6.")


if __name__ == "__main__":
    main()

