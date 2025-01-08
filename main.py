import random


def play_game(difficulty, max_attempts, target):
    print(f"Great! You have selected the {difficulty} difficulty level.")
    print(f"You have {max_attempts} chances to guess the number! \n")
    
    for attempt in range(1, max_attempts + 1):
        try:
            guess_number = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess_number == target:
            print(f"🎉 Congratulations! You guessed the correct number in {attempt} attempts. \n")
            return
        
        print("❌ Incorrect guess.")
        print(f"Number of guesses left: {max_attempts - attempt}")
        
        if guess_number < target:
            print(f"🔼 The number is greater than {guess_number}. \n")
        else:
            print(f"🔽 The number is less than {guess_number}. \n")
    
    print(f"💥 You lost! The correct number was {target}. \n")


def select_choice(choice, target):
    match choice:
        case 1:
            play_game("Easy", 10, target)
        case 2:
            play_game("Medium", 5, target)
        case 3:
            play_game("Hard", 3, target)
        case _:
            print("❌ Invalid choice. Please select 1, 2, or 3.")


def game():
    print("🎮 Welcome to the Number Guessing Game!")
    while True:
        try:
            target_number = random.choice(range(0, 101))
            print("\nI'm thinking of a number between 1 and 100. \n")
            print("Select difficulty level: ")
            print("1. Easy (10 chances)")
            print("2. Medium (5 chances)")
            print("3. Hard (3 chances) \n")

            choice = int(input("Enter your choice: "))
            select_choice(choice=choice, target=target_number)
        except ValueError:
            print("❌ Enter a valid number for the difficulty choice.")
        except Exception as e:
            print(f"⚠️ There was an error: {e}")


if __name__ == "__main__":
    game()
