import time

class AdventureGame:
    def __init__(self):
        self.start_game()

    def print_with_delay(self, text, delay=1.5):
        print(text)
        time.sleep(delay)

    def start_game(self):
        self.print_with_delay("Welcome to the Adventure Game!")
        self.print_with_delay("You find yourself at a crossroads in a mysterious land.")
        self.choose_path()

    def choose_path(self):
        self.print_with_delay("There are three paths in front of you:")
        self.print_with_delay("1. A dark forest.")
        self.print_with_delay("2. A narrow mountain trail.")
        self.print_with_delay("3. A road leading to a glowing castle.")
        choice = input("Which path do you choose? (1/2/3): ")

        if choice == '1':
            self.forest_path()
        elif choice == '2':
            self.mountain_trail()
        elif choice == '3':
            self.castle_road()
        else:
            self.invalid_choice(self.choose_path)

    def invalid_choice(self, callback):
        self.print_with_delay("Invalid choice, please try again.")
        callback()

    def forest_path(self):
        self.print_with_delay("\nYou venture into the dark forest. The trees tower over you.")
        self.print_with_delay("Suddenly, you hear footsteps behind you.")
        choice = input("Do you want to 'run' or 'hide'? ").lower()

        if choice == "run":
            self.print_with_delay("\nYou run as fast as you can but trip over a root. The creature catches you. Game over!")
        elif choice == "hide":
            self.print_with_delay("\nYou hide behind a tree. The footsteps pass by, and you escape. You win!")
        else:
            self.invalid_choice(self.forest_path)

    def mountain_trail(self):
        self.print_with_delay("\nYou climb up the narrow mountain trail. The air gets thinner.")
        self.print_with_delay("A large boulder starts rolling down towards you!")
        choice = input("Do you want to 'jump' or 'duck'? ").lower()

        if choice == "jump":
            self.print_with_delay("\nYou leap out of the way just in time! You've reached the top. You win!")
        elif choice == "duck":
            self.print_with_delay("\nYou duck, but the boulder is too large. It crushes you. Game over!")
        else:
            self.invalid_choice(self.mountain_trail)

    def castle_road(self):
        self.print_with_delay("\nYou walk down the road toward the glowing castle. It's grand and mysterious.")
        self.print_with_delay("At the castle gate, you're greeted by a guard.")
        choice = input("Do you want to 'talk' to the guard or 'sneak' into the castle? ").lower()

        if choice == "talk":
            self.print_with_delay("\nThe guard lets you in after you explain your quest. You find treasure inside. You win!")
        elif choice == "sneak":
            self.print_with_delay("\nYou try to sneak in, but the guard catches you. Game over!")
        else:
            self.invalid_choice(self.castle_road)

# Start the game
if __name__ == "__main__":
    AdventureGame()
