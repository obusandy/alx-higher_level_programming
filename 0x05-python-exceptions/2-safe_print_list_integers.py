#!/usr/bin/python3
def safe_print_list_integers(my_lst=[], x=0):
    num_prnted = 0
    for k in range(x):
        try:
            print("{:d}".format(my_lst[k]), end='')
            num_prnted += 1
        except (TypeError, ValueError):
            pass
    print("")
    return num_prnted
