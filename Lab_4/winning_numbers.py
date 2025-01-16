def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.
    """
    # Count how many numbers in user_list match those in winning_list
    matches = len(set(user_list) & set(winning_list))

    # Determine the prize based on the number of matches
    if matches == 3:
        prize = "First"
    elif matches == 2:
        prize = "Second"
    elif matches == 1:
        prize = "Third"
    else:
        prize = "No"

    # Print the result
    print(f"Congratulations, you won {prize} prize!")
    return prize



if __name__ == "__main__":
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]

    result = winning_numbers(user_list, winning_list)
    print(f"Result: {result}")
