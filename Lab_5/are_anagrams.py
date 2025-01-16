def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """
    # Normalize the strings by converting to lowercase and sorting the characters
    normalized_str1 = sorted(str1.lower())
    normalized_str2 = sorted(str2.lower())

    # Check if the sorted strings are equal
    output = normalized_str1 == normalized_str2
    return output


# Example usage of the function
if __name__ == "__main__":
    # Test case 1: Anagrams
    print(are_anagrams("listen", "silent"))  # Expected output: True

    # Test case 2: Not anagrams
    print(are_anagrams("hello", "world"))    # Expected output: False

    # Test case 3: Case-insensitive check
    print(are_anagrams("side", "dies"))  # Expected output: True

    # Test case 4: Different lengths
    print(are_anagrams("listen", "listens")) # Expected output: False
