import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from math import sqrt as sq
from LinAlg.matrix import ndarray,Vector

def sqrt(x:ndarray):
    for j in range(len(x)):
        for i in range(len(x[0])):
            x[j][i] = sq(x[j][i])
    return x
