def annual_net_income(gross_salary):
    """
    Calculate the annual net income based on the gross salary and tax rate.
    """
    if gross_salary >= 45000:
        tax_rate = 0.50  # 50% tax rate
    elif gross_salary >= 30000:
        tax_rate = 0.30  # 30% tax rate
    else:
        tax_rate = 0.15  # 15% tax rate

    # Calculate the tax amount
    tax_amount = gross_salary * tax_rate

    # Calculate the net salary
    net_salary = gross_salary - tax_amount

    return net_salary


# Example usage:
gross_salary = 35000
net_income = annual_net_income(gross_salary)
print(f"The net income for a gross salary of £{gross_salary} is £{net_income:.2f}")
