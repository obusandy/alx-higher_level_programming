#!/usr/bin/python3
def max_integer(my_lst=[]):
    if my_lst == []:
        return None
    my_lst.sort()
    return my_lst[-1]
