def fuel_cost(distance):
  


    MPG = 50  # Miles per gallon
    liters_per_gallon = 4.5  # Liters per gallon
    price_per_liter = 1.49  # Price per liter in pounds (£)

    # number of gallons needed
    gallons_needed = distance / MPG

    # gallons to liters
    liters_needed = gallons_needed * liters_per_gallon

    # total fuel cost
    total_cost = liters_needed * price_per_liter

    return total_cost

# Example usage:
distance_travelled = 50  # For example, 50 miles
cost = fuel_cost(distance_travelled)
print(f"The total fuel cost for {distance_travelled} miles is £{cost:.2f}")
