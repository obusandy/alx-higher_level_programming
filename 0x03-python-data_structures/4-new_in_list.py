#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_lst = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    new_lst_copy = my_list.copy()
    new_lst[idx] = element
    return (new_lst)
