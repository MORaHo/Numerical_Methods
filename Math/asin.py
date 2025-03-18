import init
from math import asin as arcsine
from LinAlg.matrix import ndarray,Matrix

def asin(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(arcsine(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return arcsine(x)