import random


attempts = 7


def display_rules():
    print("-----------welcome to the guessing game-----------")
    print("\n")
    print("These are the rules of the game:")
    print("           You have to guess a number between 1 and 100.")
    print("           You have", attempts, "attempts to guess the number.")

def get_user_guess():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Invalid input. Please enter a number between 1 and 100.")

def check_guess(guess_number):
    guess_attampts = 7
    while guess_attampts > 0:
        user_guess = get_user_guess()
        if user_guess == guess_number:
            print(f"Congratulations! You guessed the correct number:{guess_number} from {7-guess_attampts+1} attempts.")
            return True
            
        else:
            guess_attampts -= 1
            print("Incorrect guess. You have", guess_attampts, "attempts left.")
    return False

def play_game():
    guess_number = random.randint(1, 100)
    print("The number has been generated. Start guessing!")
    check_guess(guess_number)


def main():
    display_rules()
    play_game()

main()