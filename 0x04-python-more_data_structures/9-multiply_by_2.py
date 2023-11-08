#!/usr/bin/python3

def multiply_by_2(a_dict):
    curr_dict = {}
    for key, numbr in a_dict.items():
        curr_dict[key] = numbr * 2
    return curr_dict
