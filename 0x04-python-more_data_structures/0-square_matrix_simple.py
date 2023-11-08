#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    otpt_matrix = [[elmt**2 for elmt in row] for row in matrix]
    return otpt_matrix
