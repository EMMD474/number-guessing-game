import random



def select_choice(choice, target):
    match choice:
        case 1:
            number_guesses = 0
            print("Great! You have selected the Easy difficulty level.")
            print("You have 10 chances to guess the number! \n")
            while number_guesses < 10:
                guess_number = int(input("Enter you guess: "))
                if guess_number == target:
                    print(f"Congratulations! You guessed the correct number in {number_guesses + 1} attempts. \n")
                    break
                print("Incorrect")
                number_guesses += 1
                print(f"Number of guesses left: {9 - number_guesses}")
                if number_guesses == 9:
                    print("You lost this game!! \n")
                    break
                if guess_number < target:
                    print(f"The number is greater than {guess_number}. \n")
                else:
                    print(f'The number is less than {guess_number}. \n')
                
        case 2:
             number_guesses = 0
             print("Great! You have selected the Medium difficulty level.")
             print("You have 5 chances to guess the number! \n")
             while number_guesses < 5:
                guess_number = int(input("Enter you guess: "))
                if guess_number == target:
                    print(f"Congratulations! You guessed the correct number in {number_guesses + 1} attempts. \n")
                    break
                print("Incorrect")
                number_guesses += 1
                print(f"Number of guesses left: {5 - number_guesses}")
                if number_guesses == 5:
                    print("You lost this game!! \n")
                    break
                if guess_number < target:
                    print(f"The number is greater than {guess_number}. \n")
                else:
                    print(f'The number is less than {guess_number}. \n')
        case 3:
            number_guesses = 0
            print("Great! You have selected the Medium difficulty level.")
            print("You have 5 chances to guess the number! \n")
            while number_guesses < 3:
                guess_number = int(input("Enter you guess: "))
                if guess_number == target:
                    print(f"Congratulations! You guessed the correct number in {number_guesses + 1} attempts. \n")
                    break
                print("Incorrect")
                number_guesses += 1
                print(f"Number of guesses left: {3 - number_guesses}")
                if number_guesses == 3:
                    print("You lost this game!! \n")
                    break
                if guess_number < target:
                    print(f"The number is greater than {guess_number}. \n")
                else:
                    print(f'The number is less than {guess_number}. \n')
        case _:
            print("Not an option")
            return False

def game():
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            target_number = random.choice(range(0, 101))
            print("I'm thinking of a number between 1 and 100. \n")

            print("Select difficulty level: ")
            print("1. Easy (10 chances)")
            print("2. Medium (5 chances)")
            print("3. Hard (3 chances) \n")

            choice = int(input("Enter your choice: "))
            print(target_number)

            select_choice(choice=choice, target=target_number)
        except ValueError:
            print("Enter a valid number.")
        except Exception as e:
            print(f"There was an error: {e}")


if __name__ == "__main__":
    game()