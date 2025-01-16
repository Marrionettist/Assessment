def sum_of_evens(min_value, max_value):
    """
    Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total (int): Sum of the even numbers between min_value and max_value.

    Example:
        min_value = 10
        max_value = 13
        total = sum_of_evens(min_value, max_value)
        print(total)  # total is 22.
    """
    # Initialize the total
    total = 0

    # Iterate through the range and add only even numbers to total
    for num in range(min_value, max_value + 1):
        if num % 2 == 0:  # Check if the number is even
            total += num

    return total


# Example usage of the function
if __name__ == "__main__":
    # Example 1
    min_value = 10
    max_value = 13
    result = sum_of_evens(min_value, max_value)
    print(f"Sum of evens between {min_value} and {max_value}: {result}")  # Output: 22

    # Example 2
    min_value = 1
    max_value = 10
    result = sum_of_evens(min_value, max_value)
    print(f"Sum of evens between {min_value} and {max_value}: {result}")  # Output: 30
