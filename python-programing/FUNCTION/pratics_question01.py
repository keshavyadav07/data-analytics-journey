'''Count Digits
count_digits(n) function banao jo number me kitne digits hain return kare.'''

def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count


num = int(input("Enter number: "))

print(count_digits(num))

'''Reverse Number
reverse_number(n) function banao jo number ko reverse karke return kare.'''



def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse


num = int(input("Enter number: "))

print(reverse_number(num))

'''Prime Number Function 🔥
is_prime(n) function banao jo check kare number prime hai ya nahi'''


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


num = int(input("Enter number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

'''Factorial Function
factorial(n) function banao'''


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


num = int(input("Enter number: "))

print(factorial(num))


