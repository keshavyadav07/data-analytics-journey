username = input("Enter username: ")

result = (
    8 <= len(username) <= 15
    and username[0].isalpha()
    and " " not in username
    and "@" not in username
)

print(result)