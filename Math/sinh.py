import init
from math import sinh as hyperbsine
from LinAlg.matrix import ndarray,Matrix

def sinh(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(hyperbsine(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return hyperbsine(x)