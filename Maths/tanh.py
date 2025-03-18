import init
from math import tanh as hyperbtan
from LinAlg.matrix import ndarray,Matrix

def tanh(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(hyperbtan(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return hyperbtan(x)