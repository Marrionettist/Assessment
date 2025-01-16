import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
    options = ["rock", "paper", "scissors"]

    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.")

    while True:
        # Get user input
        user_choice = input("Your choice: ").lower()

        # Check if the user wants to quit
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

        # Validate the user's choice
        if user_choice not in options:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Computer makes a random choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors_game()
