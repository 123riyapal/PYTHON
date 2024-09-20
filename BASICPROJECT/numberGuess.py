import random

i = 0
computer = int(random.random() * 10)
guess = int(input("Guess a number between 0 and 9: "))

while guess != computer:
    i += 1
    if guess > computer:
        print("The number is smaller")
    elif guess < computer:
        print("The number is greater")
    
    guess = int(input("Guess again: "))

print(f"You guessed the right number in {i + 1} attempts!")
