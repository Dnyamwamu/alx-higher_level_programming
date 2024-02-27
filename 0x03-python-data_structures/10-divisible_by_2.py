#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the results
    result = []
    # Iterate through each element in the input list
    for num in my_list:
        # Check if the element is divisible by 2
        if num % 2 == 0:
            result.append(True)  # Append True if divisible by 2
        else:
            result.append(False)  # Append False if not divisible by 2
    return result
