import init
from math import log as logarithm
from LinAlg.matrix import ndarray,Matrix

def ln(x,base):
    return logarithm(x)

def logwithbase(x,base:int):
    return logarithm(x,base)

def log(x:ndarray,base:int=0):
    if base != 0:
        logarithm = logwithbase
    else:
        logarithm = ln
    
    [rows,cols] = x.size()
    M = []
    for j in range(len(x)):
        for i in range(len(x[0])):
            if base != 0:
                M.append(logarithm(x[j][i],base))
    return Matrix(M,rows,cols)
