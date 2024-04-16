#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A set containing the common elements between set_1 and set_2.
    """
    # Use the intersection method to find common elements
    common_elements_set = set_1.intersection(set_2)

    return common_elements_set
