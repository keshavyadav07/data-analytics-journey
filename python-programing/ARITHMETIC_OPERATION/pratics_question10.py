'''User se total days input lo aur usko weeks + remaining days mein convert karo.

Example:

Enter days: 25

Weeks = 3
Remaining days = 4'''

days = int(input("Enter total days: "))
weeks = days // 7
remaining_days = days % 7
print("Weeks =", weeks)
print("Remaining days =", remaining_days)