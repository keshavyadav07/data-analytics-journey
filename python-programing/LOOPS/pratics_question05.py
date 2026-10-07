'''Palindrome Number 🔥

Input: 1221
Output: Palindrome

Input: 1234
Output: Not Palindrome'''

num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")