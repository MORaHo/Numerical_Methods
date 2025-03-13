import init
from math import sin as sine
from LinAlg.matrix import ndarray,Matrix

def sin(x:ndarray):
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            M.append(sine(x[j][i]))
    return Matrix(M,rows,cols)