'''Without using if

User se ek number lo aur calculate karo ki us number ko:

2 se divide karne par remainder kya hai
3 se divide karne par remainder kya hai
5 se divide karne par remainder kya hai'''

number = int(input("Enter a number: "))
remainder_2 = number % 2
remainder_3 = number % 3
remainder_5 = number % 5
print("Remainder when divided by 2:", remainder_2)
print("Remainder when divided by 3:", remainder_3)  
print("Remainder when divided by 5:", remainder_5)