#!/usr/bin/python3

"""Defines a class Student."""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                # Each element (except first and last) is the sum of the elements directly above in the previous row
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
