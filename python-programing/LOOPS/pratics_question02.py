'''Digit Sum
Number ke saare digits ka sum nikalo.

Input: 5832
Output: 18'''


num = int(input("Enter number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Digit Sum:", sum)