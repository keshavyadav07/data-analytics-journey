''''Largest Digit 🔥
Number ke andar sabse bada digit find karo.

Input: 58329
Output: 9'''


num = int(input("enter number"))
largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print(largest)

'''Smallest Digit

Input: 58329
Output: 2'''

num = int(input("enter number"))
smallest = 9
while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print(smallest)