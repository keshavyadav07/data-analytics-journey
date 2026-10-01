username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "admin"
correct_password = "1234"

result = username == correct_username and password == correct_password

print(result)