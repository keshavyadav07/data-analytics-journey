'''Password Strength
User se password lo aur check karo:

Length >= 8
At least one uppercase letter
At least one lowercase letter
At least one digit'''

password = input("Enter password: ")

print(len(password) >= 8)
print(any(ch.isupper() for ch in password))
print(any(ch.islower() for ch in password))
print(any(ch.isdigit() for ch in password))