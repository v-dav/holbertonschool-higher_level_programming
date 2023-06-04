#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        list = []
        for j in i:
            list.append(j**2)
        new_matrix.append(list)
    return new_matrix
