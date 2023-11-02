#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add as my_add, sub as my_sub, mul as my_mul, div as my_div

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == '+':
        result = my_add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif operator == '-':
        result = my_sub(a, b)
        print("{} - {} = {}".format(a, b, result))
    elif operator == '*':
        result = my_mul(a, b)
        print("{} * {} = {}".format(a, b, result))
    else:
        result = my_div(a, b)
        print("{} / {} = {}".format(a, b, result))
