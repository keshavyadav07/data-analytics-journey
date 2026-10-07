A = int(input("enter first number: "))
B = int(input("enter second number: "))
C = int(input("enter third number: "))

if A > B and A > C:
    print("A is the greatest number")
elif B > A and B > C:
    print("B is the greatest number")
else:
    print("C is the greatest number")         