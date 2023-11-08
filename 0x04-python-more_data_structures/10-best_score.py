#!/usr/bin/python3

def best_score(a_dict):
    if not a_dict:
        return None
    curr_best = max(a_dict.values())
    for key, numbr in a_dict.items():
        if numbr == curr_best:
            bst_key = key
    return bst_key
