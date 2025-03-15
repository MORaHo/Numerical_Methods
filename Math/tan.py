import init
from math import tan as tangent
from LinAlg.matrix import ndarray,Matrix

def tan(x:ndarray):
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            M.append(tangent(x[j][i]))
    return Matrix(M,rows,cols)