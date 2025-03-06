import init
from LinAlg.matrix import ndarray

def root(x:ndarray,n:int):
    for j in range(len(x)):
        for i in range(len(x[0])):
            x[j][i] = x[j][i]**(1/n)
    return x