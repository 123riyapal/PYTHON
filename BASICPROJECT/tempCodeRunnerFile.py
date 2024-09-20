def quiz():
    questions = [
        {
            "question": "1. What will be the output of the following code?\n"
                        "x = [1, 2, 3, 4]\n"
                        "y = x\n"
                        "y[0] = 10\n"
                        "print(x)\n",
            "options": ["a) [1, 2, 3, 4]", "b) [10, 2, 3, 4]", "c) [1, 2, 3, 10]", "d) Error"],
            "answer": "b"
        },
        {
            "question": "2. Which of the following data types is immutable in Python?",
            "options": ["a) List", "b) Dictionary", "c) Tuple", "d) Set"],
            "answer": "c"
        },
        {
            "question": "3. What is the correct way to handle exceptions in Python?",
            "options": ["a) try-exception", "b) try-catch", "c) try-except", "d) try-handle"],
            "answer": "c"
        },
        {
            "question": "4. What will the following code output?\n"
                        "print(bool(0), bool(3), bool([]))",
            "options": ["a) True True False", "b) False True False", "c) False False True", "d) True False True"],
            "answer": "b"
        },
        {
            "question": "5. Which of the following is the correct way to define a function in Python?",
            "options": ["a) def myFunction:", "b) function myFunction():", "c) def myFunction():", "d) myFunction() def:"],
            "answer": "c"
        }
    ]

    score = 0

    for i, q in enumerate(questions):
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("\nEnter your answer (a, b, c, or d): ").strip().lower()

        if answer == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")

    print(f"Your final score is {score}/{len(questions)}")

quiz()
