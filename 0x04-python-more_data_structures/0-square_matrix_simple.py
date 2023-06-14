#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMtr = []
    for i in matrix:
        raw = list(map(lambda x: x**2, i))
        newMtr.append(raw)
    return(newMtr)
