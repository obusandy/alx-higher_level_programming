#!/usr/bin/python3

def multiply_by_2(a_dict):
    curr_dict = {}
    for kys, numbr in a_dict.items():
        curr_dict[kys] = numbr * 2
    return curr_dict
