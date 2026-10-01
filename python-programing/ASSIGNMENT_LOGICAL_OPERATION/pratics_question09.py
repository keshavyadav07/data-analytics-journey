age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance: "))

eligible = age >= 18 and marks >= 50 and attendance >= 75

print(eligible)