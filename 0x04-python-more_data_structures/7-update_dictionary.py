#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Update or add key/value in a dictionary."""
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
