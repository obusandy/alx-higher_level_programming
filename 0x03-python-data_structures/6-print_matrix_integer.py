#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    for line in matrix:
        for i, l in enumerate(line):
            print("{:d}".format(l), end=' ' if i < len(line) - 1 else '')
        print()
