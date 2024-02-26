#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def main():
    result_add = add(5, 3)
    result_sub = sub(10, 4)
    result_mul = mul(7, 2)
    result_div = div(15, 3)

    print("Addition:", result_add)
    print("Subtraction:", result_sub)
    print("Multiplication:", result_mul)
    print("Division:", result_div)

if __name__ == "__main__":
    main()

