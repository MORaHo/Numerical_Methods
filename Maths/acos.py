import init
from math import acos as arccos
from LinAlg.matrix import ndarray,Matrix

def acos(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(arccos(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return arccos(x)