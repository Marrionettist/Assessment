def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay

    # Calculate pay
    if hours_worked <= standard_hours:
        total_pay = hours_worked * regular_rate
    else:
        # Regular pay for the first 35 hours + Overtime pay for additional hours
        overtime_hours = hours_worked - standard_hours
        total_pay = (standard_hours * regular_rate) + (overtime_hours * overtime_rate)

    return total_pay


# Example usage of the function
if __name__ == "__main__":
    # Test case 1: No overtime
    hours = 35
    print(f"Weekly pay for {hours} hours: £{calculate_weekly_pay(hours)}")  # Output: £420

    # Test case 2: With 1 hour of overtime
    hours = 36
    print(f"Weekly pay for {hours} hours: £{calculate_weekly_pay(hours)}")  # Output: £438

    # Test case 3: Significant overtime
    hours = 40
    print(f"Weekly pay for {hours} hours: £{calculate_weekly_pay(hours)}")  # Output: £510

    # Test case 4: Less than 35 hours
    hours = 30
    print(f"Weekly pay for {hours} hours: £{calculate_weekly_pay(hours)}")  # Output: £360
