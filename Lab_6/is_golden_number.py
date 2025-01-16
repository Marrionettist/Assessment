def is_golden_number(n):




    # Check all pairs (a, b) where a + b = n
    for a in range(1, n):  # a ranges from 1 to n-1
        b = n - a  # b is automatically determined
        if a * b % 100 == 0:  # Check if the product a * b is divisible by 100
            return True
    
    return False

# Example usage:
print(is_golden_number(200))  # True
print(is_golden_number(300))  # True
print(is_golden_number(15))  # False
