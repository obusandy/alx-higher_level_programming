#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    number_args = len(sys.argv) - 1

    if number_args == 0:
        print(f"{number_args} arguments.")
    else:
        print(f"{number_args} argument{'s' if number_args != 1 else ''}:")

    for num, arg in enumerate(sys.argv[1:], 1):
        print(f"{num}: {arg}")
