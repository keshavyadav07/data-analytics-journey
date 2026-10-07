

hindi = int(input("Enter marks in Hindi: "))
english = int(input("Enter marks in English: "))
maths = int(input("Enter marks in Maths: "))
science = int(input("Enter marks in Science: "))
social = int(input("Enter marks in Social: "))

if hindi < 33 or english < 33 or maths < 33 or science < 33 or social < 33:
    print("Fail")
else:
    total_marks = hindi + english + maths + science + social
    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 45:
        print("Grade: D")
    else:
        print("Grade: E")