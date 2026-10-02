m1 = int(input("Subject 1 marks: "))
m2 = int(input("Subject 2 marks: "))
m3 = int(input("Subject 3 marks: "))
m4 = int(input("Subject 4 marks: "))
m5 = int(input("Subject 5 marks: "))

marks = [m1, m2, m3, m4, m5]

print("Marks:", marks)


numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)