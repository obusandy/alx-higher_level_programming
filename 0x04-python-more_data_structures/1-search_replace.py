#!/usr/bin/python3

def search_replace(my_list, search, replace):

    otput_list = my_list.copy()
    for x, elmnt in enumerate(otput_list):
        if elmnt == search:
            otput_list[x] = replace

    return otput_list
