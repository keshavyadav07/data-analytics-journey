students = []

subjects = ("Python", "Maths", "DBMS", "OS", "COA")

def add_student():

    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))

    marks = []

    for subject in subjects:
        mark = int(input(f"Enter {subject} marks: "))
        marks.append(mark)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")

def show_students():

    if len(students) == 0:
        print("No students found!")
        return

    for student in students:

        print("\n--------------------")
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Marks:", student["marks"])

def search_student():

    roll_no = int(input("Enter roll number to search: "))

    found = False

    for student in students:

        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Marks:", student["marks"])

            found = True
            break

    if found == False:
        print("Student not found!") 

def calculate_result():

    roll_no = int(input("Enter roll number: "))

    for student in students:

        if student["roll_no"] == roll_no:

            marks = student["marks"]

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

            print("\n========== RESULT ==========")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Marks:", marks)
            print("Total:", total)
            print("Percentage:", percentage)
            print("Grade:", grade)

            return

    print("Student not found!")

def show_subjects():

    unique_subjects = set(subjects)

    print("\nUnique Subjects:")

    for subject in unique_subjects:
        print(subject)


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Show Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_result()

    elif choice == "5":
        show_subjects()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")