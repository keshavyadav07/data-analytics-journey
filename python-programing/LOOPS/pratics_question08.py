'''Prime Factors 🔥

Input: 60

Output:
2 2 3 5'''

num = int(input("Enter number: "))

i = 2

while num > 1:
    if num % i == 0:
        print(i, end=" ")
        num = num // i
    else:
        i += 1