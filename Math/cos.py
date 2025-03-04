import init
from math import cos as cosine
from LinAlg.matrix import ndarray

def cos(x:ndarray):
    for j in range(len(x)):
        for i in range(len(x[0])):
            x[j][i] = cosine(x[j][i])
    return x