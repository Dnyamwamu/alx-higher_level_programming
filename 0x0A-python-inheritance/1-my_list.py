#!/usr/bin/python3

class MyList(list):
    """A subclass of list with additional method print_sorted to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))

# Example usage:
if __name__ == "__main__":
    # Create an instance of MyList
    my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5])

    # Print the list in sorted order
    my_list.print_sorted()
