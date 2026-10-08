'''Digit Sum Function 🔥
digit_sum(n) function banao jo number ke digits ka sum return kare.'''

def digit_sum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total


num = int(input("Enter number: "))

print(digit_sum(num))