#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            result += chr(ord(char) - 32)
        else:
            result += char
            # Print the result followed by a new line
            print(result)
            # Test the function
            uppercase("hello")
            uppercase("world")
