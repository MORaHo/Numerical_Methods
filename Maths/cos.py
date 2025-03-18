import init
from math import cos as cosine
from LinAlg.matrix import ndarray,Matrix

def cos(x):
    if type(x) == ndarray:
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(cosine(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return cosine(x)