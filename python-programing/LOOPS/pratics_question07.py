'''Factors of a Number

Input: 24

Output:
1 2 3 4 6 8 12 24'''


num = int(input("Enter number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")