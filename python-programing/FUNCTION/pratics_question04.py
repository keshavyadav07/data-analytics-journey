'''Count Vowels

count_vowels(text) function banao jo string me total vowels count kare.

Input: "programming"
Output: 3'''


def count_vowels(text):
    count = 0

    for char in text:
        if char in "aeiou":
            count += 1

    return count


text = input("Enter a string: ")

print("Total Vowels:", count_vowels(text))



'''Student Result 🔥🔥

Function:

student_result(name, marks)

Marks ki list milegi. Function:

Total nikale
Percentage nikale
Grade decide kare
Result return/print kar'''

def student_result(name, marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Student Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)


name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(mark)

student_result(name, marks)

'''Number Analyzer 🔥🔥

Ek function analyze_number(n) banao jo ek number ke liye:

digits count
digit sum
reverse
even/odd

sab calculate kare.'''


def analyze_number(n):
    original = n

    digit_count = 0
    digit_sum = 0
    reverse = 0

    while n > 0:
        digit = n % 10

        digit_count += 1
        digit_sum += digit
        reverse = reverse * 10 + digit

        n = n // 10

    if original % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    print("Digits Count:", digit_count)
    print("Digit Sum:", digit_sum)
    print("Reverse:", reverse)
    print("Even/Odd:", result)


n = int(input("Enter a number: "))

analyze_number(n)


'''Password Validator 🔥🔥

Function:

validate_password(password)

Password ko check karo:

minimum 8 characters
uppercase present
lowercase present
digit present'''


def validate_password(password):
    if len(password) < 8:
        return "Invalid Password: Minimum 8 characters required"

    uppercase = False
    lowercase = False
    digit = False

    for char in password:
        if char.isupper():
            uppercase = True
        elif char.islower():
            lowercase = True
        elif char.isdigit():
            digit = True

    if uppercase and lowercase and digit:
        return "Valid Password"
    else:
        return "Invalid Password"


password = input("Enter password: ")

print(validate_password(password))