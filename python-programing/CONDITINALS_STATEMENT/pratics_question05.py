A = int(input("enter first number : "))
B = int(input("enter second number : "))
operator = input("enter your operator (+, -, *, /) : ")

if operator == "+":
    result = A + B
    print("the sum of A and B is : ", result)
elif operator == "-":
    result = A - B
    print("the difference of A and B is : ", result)
elif operator == "*":
    result = A * B
    print("the product of A and B is : ", result)
elif operator == "/":
    result = A / B
    print("the quotient of A and B is : ", result)
else:
    print("invalid operator")