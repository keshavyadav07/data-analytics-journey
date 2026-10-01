'''User se total amount input lo. ₹500, ₹200, ₹100 ke notes ka minimum breakdown nikalo.

Example:

Enter amount: 1300

500 notes = 2
200 notes = 1
100 notes = 1'''

amount = int(input("Enter amount: "))
notes_500 = amount // 500
amount = amount % 500
notes_200 = amount // 200
amount = amount % 200
notes_100 = amount // 100
print("500 notes =", notes_500)
print("200 notes =", notes_200)
print("100 notes =", notes_100)