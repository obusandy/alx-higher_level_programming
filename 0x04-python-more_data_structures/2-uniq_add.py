#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    for indx in set(my_list):
        addition += indx
    return addition
