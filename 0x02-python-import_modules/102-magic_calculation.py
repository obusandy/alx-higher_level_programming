#!/usr/bin/python3

def magic_calculation(a, b):

    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for num in range(4, 6):
            i = add(i, num)
        return(i)
    else:
        return(sub(a, b))
