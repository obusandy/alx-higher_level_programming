#!/usr/bin/python3
def fizzbuzz():
    for dgt in range(1, 101):
        if dgt % 3 == 0 and dgt % 5 == 0:
            print("FizzBuzz ", end="")
        elif dgt % 3 == 0:
            print("Fizz ", end="")
        elif dgt % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(dgt), end='')
