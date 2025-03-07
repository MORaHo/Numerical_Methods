import init
from math import exp as exponential
from LinAlg.matrix import ndarray

def exp(x:ndarray):
    for j in range(len(x)):
        for i in range(len(x[0])):
            x[j][i] = exponential(x[j][i])
    return x