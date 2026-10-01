'''Ek student ke 5 subjects ke marks input lo. Calculate karo:

Total marks
Percentage
Average

Assume each subject is out of 100'''

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))
total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100
average = total_marks / 5
print("Total marks:", total_marks)
print("Percentage:", percentage)
print("Average marks:", average)