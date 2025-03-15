import init
from math import atanh as archyperbtan
from LinAlg.matrix import ndarray,Matrix

def atanh(x:ndarray):
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            M.append(archyperbtan(x[j][i]))
    return Matrix(M,rows,cols)