import init
from LinAlg.matrix import ndarray,Matrix

def abs(x:ndarray):
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            M.append(abs(x[j][i]))
    return Matrix(M,rows,cols)