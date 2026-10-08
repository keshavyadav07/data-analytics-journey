'''Even/Odd Function
check_even_odd(n) function banao jo bataye number even hai ya odd.'''

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


n = int(input("Enter number: "))

print(check_even_odd(n))


'''Maximum of 3 Numbers
find_max(a, b, c) function banao jo 3 numbers me se maximum return kare.'''





def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = find_max(a, b, c)

print("Maximum:", result)




'''Calculator Function
calculator(a, b, operation) function banao.
'''



def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid operation"


a = int(input("enter a ="))
b = int(input("enter b ="))
operation = input("enter operation =")

print(calculator(a, b, operation))