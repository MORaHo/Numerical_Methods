import init
from math import ceil as ceiling
from LinAlg.matrix import ndarray,Matrix

def ceil(x:ndarray):
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            M.append(ceiling(x[j][i]))
    return Matrix(M,rows,cols)