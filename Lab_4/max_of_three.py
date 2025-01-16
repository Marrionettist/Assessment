def max_of_three(num1, num2, num3):
  
    

    if num1 > num2:
        if num1 > num3:
            maximum = num1 
        elif num1 < num3:
            maximum = num3
    elif num1 < num2:
        if num2 > num3:
            maximum = num2
        elif num2 < num3:
            maximum = num3
  
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...

    return maximum

# # You are out of the body function where you can test your code.
# Example usage:
maximum = max_of_three(10, 20, 30)
print(maximum, "is the maximum")
