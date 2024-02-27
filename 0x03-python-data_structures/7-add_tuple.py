#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements of each tuple, or use 0 if the tuple is smaller than 2
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    c = tuple_b[0] if len(tuple_b) > 0 else 0
    d = tuple_b[1] if len(tuple_b) > 1 else 0

    # Add corresponding elements and return a tuple
    return (a + c, b + d)
