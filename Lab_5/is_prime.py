def is_prime(num):
    """
    Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:
        boolean = is_prime(5)  # returns True
        print(boolean)
    """
    # Handle edge cases for numbers less than 2
    if num < 2:
        return False

    # Check divisors from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:  # If divisible, it's not prime
            return False

    # If no divisors were found, it's prime
    return True


# Example usage of the function
if __name__ == "__main__":
    # Test case 1: Prime number
    boolean = is_prime(5)
    print(f"Is 5 a prime number? {boolean}")  # Output: True

    # Test case 2: Non-prime number
    boolean = is_prime(10)
    print(f"Is 10 a prime number? {boolean}")  # Output: False

    # Test case 3: Edge case for number less than 2
    boolean = is_prime(1)
    print(f"Is 1 a prime number? {boolean}")  # Output: False

    # Test case 4: Larger prime number
    boolean = is_prime(29)
    print(f"Is 29 a prime number? {boolean}")  # Output: True
