#!/usr/bin/python3
def no_c(my_string):
    ns = ""
    for character in my_string:
        if character != "c" and character != "C":
            ns += character
    return (ns)
