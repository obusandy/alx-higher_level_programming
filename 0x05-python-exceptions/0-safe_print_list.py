#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_prnted = 0
    try:
        for k in range(x):
            print(my_list[k], end='')
            num_prnted = num_prnted + 1
    except IndexError:
        pass
    print("")
    return num_prnted
