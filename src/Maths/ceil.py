from math import ceil as ceiling
from src.LinAlg.matrix import ndarray,Matrix

def ceil(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(ceiling(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return ceiling(x)