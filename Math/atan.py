import init
from math import atan as arctangent
from LinAlg.matrix import ndarray,Matrix

def atan(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(arctangent(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return arctangent(x)