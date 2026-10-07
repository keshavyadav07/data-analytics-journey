'''Digit Count
Number mein total kitne digits hain, loop se count karo.

Input: 987654
Output: 6'''

num = int(input("enter number"))
count = 0

while num > 0:
    num = num // 10
    count += 1

print(count)