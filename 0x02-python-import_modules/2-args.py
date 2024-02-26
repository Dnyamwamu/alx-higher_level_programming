#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1  # Subtract 1 to exclude the script name
    args = argv[1:]  # Exclude the script name from the list of arguments

    print("{} argument{}:".format(argc, "s" if argc != 1 else ""), end="")
    print("." if argc == 0 else "")
    
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

