
print("=" * 45)
print("          PYTHON QUIZ CHALLENGE")
print("=" * 45)

name = input("Enter your name: ")

questions = [
    {
        "question": "Which language is popular for AI?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. XML"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Set", "C. Tuple", "D. Dictionary"],
        "answer": "C"
    },
    {
        "question": "Which keyword defines a function?",
        "options": ["A. function", "B. define", "C. fun", "D. def"],
        "answer": "D"
    },
    {
        "question": "What is the output of 5 // 2?",
        "options": ["A. 2", "B. 2.5", "C. 3", "D. 1"],
        "answer": "A"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["A. add()", "B. append()", "C. push()", "D. pop()"],
        "answer": "B"
    },
    {
        "question": "What is the output of len('Python')?",
        "options": ["A. 5", "B. 7", "C. 6", "D. 4"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!-- -->", "D. **"],
        "answer": "B"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to start a for loop?",
        "options": ["A. repeat", "B. loop", "C. for", "D. iterate"],
        "answer": "C"
    },
    {
        "question": "What is the output of bool(0)?",
        "options": ["A. True", "B. False", "C. 0", "D. None"],
        "answer": "B"
    },
    {
        "question": "Which method converts text to lowercase?",
        "options": ["A. lower()", "B. small()", "C. lowercase()", "D. down()"],
        "answer": "A"
    },
    {
        "question": "What is the output of 10 % 3?",
        "options": ["A. 3", "B. 1", "C. 0", "D. 3.33"],
        "answer": "B"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "What does the break statement do?",
        "options": [
            "A. Skips one iteration",
            "B. Stops the loop",
            "C. Restarts the loop",
            "D. Pauses the program"
        ],
        "answer": "B"
    },
    {
        "question": "Which keyword is used for exception handling?",
        "options": ["A. check", "B. error", "C. try", "D. test"],
        "answer": "C"
    },
    {
        "question": "What is the output of len([10, 20, 30])?",
        "options": ["A. 2", "B. 3", "C. 10", "D. 60"],
        "answer": "B"
    },
    {
        "question": "Which operator checks equality?",
        "options": ["A. =", "B. ===", "C. ==", "D. !="],
        "answer": "C"
    },
    {
        "question": "What does return do inside a function?",
        "options": [
            "A. Repeats a function",
            "B. Returns a value",
            "C. Prints a value only",
            "D. Restarts the function"
        ],
        "answer": "B"
    },
    {
        "question": "Which collection stores unique elements?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. String"],
        "answer": "C"
    },
    {
        "question": "What is the output of 3 == 3?",
        "options": ["A. True", "B. False", "C. 3", "D. None"],
        "answer": "A"
    }
]

score = 0
wrong_answers = 0

print("\nWelcome,", name)
print("Total Questions:", len(questions))
print("Each correct answer gives 1 point.")

# enumerate() automatically numbers each question
for index, q in enumerate(questions, start=1):

    print("\n" + "-" * 45)
    print(f"Question {index}/{len(questions)}: {q['question']}")

    for option in q["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid option! No point awarded.")
        wrong_answers += 1

    elif user_answer == q["answer"]:
        print("Correct Answer! +1 point")
        score += 1

    else:
        print("Wrong Answer!")
        print("Correct answer:", q["answer"])
        wrong_answers += 1

# Final result
total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n" + "=" * 45)
print("                QUIZ RESULT")
print("=" * 45)

print("Player Name:", name)
print("Total Questions:", total_questions)
print("Correct Answers:", score)
print("Wrong/Invalid Answers:", wrong_answers)
print("Final Score:", f"{score}/{total_questions}")
print("Percentage:", f"{percentage:.2f}%")

if percentage >= 80:
    print("Grade: Excellent Performance!")
elif percentage >= 60:
    print("Grade: Good Job!")
elif percentage >= 40:
    print("Grade: Keep Practicing!")
else:
    print("Grade: Practice More and Try Again!")

print("=" * 45)
print("Thanks for playing,", name)

