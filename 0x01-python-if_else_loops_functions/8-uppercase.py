#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            result += chr(ord(char) - 32)
        else:
            result += char
            # Print the entire string in uppercase followed by a newline
            print(result)
