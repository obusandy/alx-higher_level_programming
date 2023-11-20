#!/usr/bin/python3
def safe_print_division(a, b):
    divisn_rslt = None
    try:
        divisn_rslt = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside divisn rslt: {}".format(divisn_rslt))
    return divisn_rslt
