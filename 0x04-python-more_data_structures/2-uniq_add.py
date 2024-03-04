#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
        my_list: The list of integers.

    Returns:
        The sum of all unique integers in the list.
    """
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate through each element in the list
    for num in my_list:
        # Add the integer to the set if it's not already present
        unique_integers.add(num)

    # Return the sum of all unique integers
    return sum(unique_integers)
