#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Check if the number is positive, negative, or zero
print(number, end=" ")
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
