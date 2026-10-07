'''Q18. Number Pattern

1
12
123
1234
12345

Q19. Reverse Pattern

12345
1234
123
12
1

Q20. Pyramid Pattern 🔥

    *
   ***
  *****
 *******
*********

Q21. Number Pyramid

    1
   123
  12345
 1234567
123456789'''

r = int(input("enter range = "))
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


r = int(input("enter range = "))
for i in range(r, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


r = int(input("enter range = "))
for i in range(1, r):
    
    for j in range(5 - i):
        print(" ", end="")
    
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()


r = int(input("enter range = "))
for i in range(1, r):

    for j in range(5 - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print(j, end="")

    print()



