#!/usr/bin/python3
def delete_at(my_lst=[], idx=0):
    if 0 <= idx < len(my_lst):
        del my_lst[idx]
        return my_lst
