#User se age input lo aur check karo ki age 13 se 19 ke beech hai ya nahi.
age = int(input("Enter your age: "))
is_teenager = age >= 13 and age <= 19
print("Is the person a teenager?", is_teenager)