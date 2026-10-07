''''User se number lo aur loop se reverse karo.
Example:

Input: 12345
Output: 54321'''

num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10   #
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", reverse)



