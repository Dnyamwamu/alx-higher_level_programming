#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """A subclass of list with additional method print_sorted to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
