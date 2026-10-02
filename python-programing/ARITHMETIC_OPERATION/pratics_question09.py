'''User se ek 3-digit number input lo. Arithmetic operators ka use karke uske:

Hundreds digit
Tens digit
Ones digit'''

number = int(input("Enter a 3-digit number: ")) 
hundreds_digit = number// 100
tens_digit = (number // 10) % 10
ones_digit = number % 10

print("Hundreds digit:", hundreds_digit)
print("Tens digit:", tens_digit)
print("Ones digit:", ones_digit)