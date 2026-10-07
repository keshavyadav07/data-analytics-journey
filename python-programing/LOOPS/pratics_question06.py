'''Prime Number 🔥
User se number lo aur check karo prime hai ya nahi.

Input: 29
Output: Prime'''




num = int(input("Enter number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")