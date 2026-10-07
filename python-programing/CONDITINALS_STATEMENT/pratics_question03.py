password = input("enter your password: ")
print(len(password))

if len(password) >= 8:
    print("your password length is valid")

else:
    print("your password length is invalid")    