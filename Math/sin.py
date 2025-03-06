import init
from math import sin as sine
from LinAlg.matrix import ndarray

def sin(x:ndarray):
    for j in range(len(x)):
        for i in range(len(x[0])):
            x[j][i] = sine(x[j][i])
    return x