def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    # Check if the list is empty
    if not numbers:
        return None

    # Calculate the sum using a for loop
    total = 0
    for num in numbers:
        total += num

    # Calculate the average
    average = total / len(numbers)
    return average


# Example usage of the function
if __name__ == "__main__":
    # Example 1: Regular list of numbers
    numbers = [10, 20, 30, 40, 50]
    print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0

    # Example 2: Single-element list
    numbers = [42]
    print("The average is:", calculate_average(numbers))  # Expected output: The average is: 42.0

    # Example 3: Empty list
    numbers = []
    print("The average is:", calculate_average(numbers))  # Expected output: The average is: None

    # Example 4: List with floats
    numbers = [1.5, 2.5, 3.5, 4.5]
    print("The average is:", calculate_average(numbers))  # Expected output: The average is: 3.0
