#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divisn_rslt = a / b
    except ZeroDivisionError:
        divisn_rslt = None
    finally:
        print("Inside divisn rslt: {}".format(divisn_rslt))
    return divisn_rslt
