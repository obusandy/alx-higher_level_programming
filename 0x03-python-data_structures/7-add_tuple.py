#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ia = tuple_a[0] if len(tuple_a) > 0 else 0
    ib = tuple_a[1] if len(tuple_a) > 1 else 0
    ja = tuple_b[0] if len(tuple_b) > 0 else 0
    jb = tuple_b[1] if len(tuple_b) > 1 else 0
    return (ia + ja, ib + jb)
