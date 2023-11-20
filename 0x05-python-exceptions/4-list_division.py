#!/usr/bin/python3
def list_division(my_lst_1, my_lst_2, lst_lenth):
    k = 0
    reslt_lst = []
    for k in range(lst_lenth):
        try:
            rslt = my_lst_1[k] / my_lst_2[k]
        except TypeError:
            print("wrong type")
            rslt = 0
        except ZeroDivisionError:
            print("division by 0")
            rslt = 0
        except IndexError:
            print("out of range")
            rslt = 0
        finally:
            reslt_lst.append(rslt)
    return reslt_lst
