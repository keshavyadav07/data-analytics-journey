'''User se 3 numbers lo:

a
b
c

Aur comparison operators ki help se check karo ki a aur b equal hain, lekin c different hai.'''

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

result = (a == b) and (b != c)
print("Are a and b equal, but c different?", result)