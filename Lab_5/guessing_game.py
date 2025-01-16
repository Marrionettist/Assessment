import random

def guessing_game():
    """
    This function implements a number guessing game where the user has to guess a randomly generated number between 0 and 10.

    The function performs the following steps:
    1. Generates a random number between 0 and 10 (inclusive) that the user needs to guess.
    2. Continuously prompts the user to enter their guess.
    3. Compares the user's guess with the generated number and provides feedback:
       - If the guess is correct, it prints a congratulatory message and exits the loop.
       - If the guess is too low, it informs the user that their guess is too low.
       - If the guess is too high, it informs the user that their guess is too high.
    4. Repeats this process until the user correctly guesses the number.
    """
    answer = random.randint(0, 10)  # Generate a random number between 0 and 10
    print("Welcome to the Guessing Game!")
    print("I have picked a number between 0 and 10. Can you guess what it is?")

    while True:
        try:
            # Get user's guess and convert it to an integer
            guess = int(input("Enter your guess: "))

            # Check if the guess is correct
            if guess == answer:
                print(f"Right! The answer is {answer}. Congratulations!")
                break
            elif guess < answer:
                print(f"Your guess of {guess} is too low!")
            else:
                print(f"Your guess of {guess} is too high!")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 10.")

# Test the game:
if __name__ == "__main__":
    guessing_game()
