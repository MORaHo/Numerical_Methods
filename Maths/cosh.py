import init
from math import cosh as hyperbcos
from LinAlg.matrix import ndarray,Matrix

def cosh(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(hyperbcos(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return hyperbcos(x)