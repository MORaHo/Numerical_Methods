import init
from math import acosh as archyperbcos
from LinAlg.matrix import ndarray,Matrix

def acosh(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(archyperbcos(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return archyperbcos(x)