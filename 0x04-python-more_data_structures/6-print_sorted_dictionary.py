#!/usr/bin/python3

def print_sorted_dictionary(a_dict):

    sort_keys = sorted(a_dict.keys())

    for key in sort_keys:
        numr = a_dict[key]
        print(f"{key}: {numr}")
