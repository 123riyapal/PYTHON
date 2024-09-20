import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissor or 'q' to quit: ").lower()
    
    if user_input == "q":
        print("Final Scores:")
        print(f"You: {user_score}, Computer: {computer_score}")
        if user_score > computer_score:
            print("You won the game! 🎉")
        elif user_score < computer_score:
            print("Computer won the game! 🎉")
        else:
            print("It's a tie! 🤝")
        break

    if user_input not in options:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    option = random.randint(0, 2)  # To choose from indices 0, 1, 2
    computer_option = options[option]
    print(f"Computer chose {computer_option}")

    if user_input == "rock" and computer_option == "scissors":
        print("You won! 🎉")
        user_score += 1
    elif user_input == "paper" and computer_option == "rock":
        print("You won! 🎉")
        user_score += 1
    elif user_input == "scissors" and computer_option == "paper":
        print("You won! 🎉")
        user_score += 1
    elif user_input == computer_option:
        print("It's a tie! 🤝")
    else:
        print("You lose! 😢")
        computer_score += 1
