import init
from math import sqrt as sq
from LinAlg.matrix import ndarray

def sqrt(x:ndarray):
    for j in range(len(x)):
        for i in range(len(x[0])):
            x[j][i] = sq(x[j][i])
    return x
