#!/usr/bin/python3

for dgt in range(122, 96, -1):
    if dgt % 2 == 0:
        c = dgt
    else:
        c = dgt - 32
    print('{}'.format(chr(c)), end='')
