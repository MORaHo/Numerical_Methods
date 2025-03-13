import init
from LinAlg.matrix import ndarray,Matrix

def sqrt(x:ndarray):
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            M.append((x[j][i])**(1/2))
    return Matrix(M,rows,cols)