#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary: The input dictionary.
    """
    # Get the sorted list of keys
    sorted_keys = sorted(a_dictionary.keys())

    # Print each key-value pair in sorted order
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
