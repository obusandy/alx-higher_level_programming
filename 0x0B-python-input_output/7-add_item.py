#!/usr/bin/python3
"""
Module:Load, add, save

adds all arguments to a Python list, and then save them to a file
"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        strd_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        strd_items = []
    strd_items.extend(sys.argv[1:])
    save_to_json_file(strd_items, "add_item.json")
