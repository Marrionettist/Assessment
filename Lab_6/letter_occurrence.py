def letter_occurrence(input_string):
   

    count = 0

    # Loop through each character in the string
    for char in input_string:
        # Check if the character is 'a' or 'A'
        if char == 'a' or char == 'A':
            count += 1

    return count


# Example usage:
input_string = "Apple, Amazon and Adidas are massive companies!"
result = letter_occurrence(input_string)
print(f"The letter 'a' or 'A' appears {result} times.")
