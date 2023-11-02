#!/usr/bin/python3

def magic_calculation(a, b):
    if a < b:
        from magic_calculation_102 import add
        for i in range(4, 6):
            a = add(a, i)
        return a
    else:
        from magic_calculation_102 import sub
        return sub(a, b)
