import init
from math import floor as flooring
from LinAlg.matrix import ndarray,Matrix

def floor(x:ndarray):
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            M.append(flooring(x[j][i]))
    return Matrix(M,rows,cols)