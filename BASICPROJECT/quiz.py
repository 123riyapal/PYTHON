import tkinter as tk
from tkinter import messagebox

# Quiz Data
questions = [
    {
        "question": "1. What will be the output of the following code?\n"
                    "x = [1, 2, 3, 4]\n"
                    "y = x\n"
                    "y[0] = 10\n"
                    "print(x)\n",
        "options": ["[1, 2, 3, 4]", "[10, 2, 3, 4]", "[1, 2, 3, 10]", "Error"],
        "answer": 1
    },
    {
        "question": "2. Which of the following data types is immutable in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": 2
    },
    {
        "question": "3. What is the correct way to handle exceptions in Python?",
        "options": ["try-exception", "try-catch", "try-except", "try-handle"],
        "answer": 2
    },
    {
        "question": "4. What will the following code output?\n"
                    "print(bool(0), bool(3), bool([]))",
        "options": ["True True False", "False True False", "False False True", "True False True"],
        "answer": 1
    },
    {
        "question": "5. Which of the following is the correct way to define a function in Python?",
        "options": ["def myFunction:", "function myFunction():", "def myFunction():", "myFunction() def:"],
        "answer": 2
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")

        # Initialize question number and score
        self.q_no = 0
        self.score = 0

        # Display question
        self.question_label = tk.Label(root, text=questions[self.q_no]["question"], wraplength=400, justify="left", font=("Arial", 12))
        self.question_label.pack(pady=20)

        # Create buttons for options
        self.option_var = tk.IntVar()
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.option_var, value=i, font=("Arial", 10))
            self.option_buttons.append(button)
            button.pack(anchor="w")

        # Next button
        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        # Display the first question and options
        self.display_question()

    def display_question(self):
        # Update the question text
        self.question_label.config(text=questions[self.q_no]["question"])

        # Update the options text
        for i, option in enumerate(questions[self.q_no]["options"]):
            self.option_buttons[i].config(text=option)

    def next_question(self):
        # Check if the answer is correct
        if self.option_var.get() == questions[self.q_no]["answer"]:
            self.score += 1

        # Move to the next question
        self.q_no += 1

        if self.q_no == len(questions):
            self.show_result()
        else:
            self.option_var.set(-1)  # Reset selected option
            self.display_question()

    def show_result(self):
        result_text = f"Your score is {self.score}/{len(questions)}"
        messagebox.showinfo("Quiz Result", result_text)
        self.root.destroy()

# Main application loop
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
