#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list unchanged
    
    # Create a new list with elements before the specified index
    new_list = my_list[:idx]
    # Extend the new list with elements after the specified index
    new_list.extend(my_list[idx + 1:])
    
    return new_list  # Return the modified list
