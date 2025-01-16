def find_maximum_difference(list1, list2):
   

    # Find the maximum and minimum values from both lists
    max_list1 = max(list1)
    min_list1 = min(list1)
    max_list2 = max(list2)
    min_list2 = min(list2)

    # Calculate the possible differences
    diff1 = max_list1 - min_list2
    diff2 = max_list2 - min_list1

    # Return the largest difference
    return max(diff1, diff2)


list1 = [1, 5, 600]
list2 = [100, 7, 3, 29, 39]
result = find_maximum_difference(list1, list2)
print(f"The largest possible difference is {result}")

list1 = [1, 5, 600]
list2 = [100, 7, 3, 602, 39]
result = find_maximum_difference(list1, list2)
print(f"The largest possible difference is {result}")
