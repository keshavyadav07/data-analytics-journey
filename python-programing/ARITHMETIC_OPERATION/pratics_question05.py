'''User se total seconds input lo aur usko:
Minutes
Remaining seconds
mein convert karo'''

sec = int(input("enter total seconds ="))
minutes = sec // 60
remaining_sec = sec % 60
print("Minutes:", minutes)
print("Remaining seconds:", remaining_sec)