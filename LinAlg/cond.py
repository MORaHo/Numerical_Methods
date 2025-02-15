from matrix import Matrix
from math import sqrt
from power import power,inv_power

### This function is subject to possible change

def cond(A:Matrix):

    M1 = A*A.T()
    M2 = A.T()*A
    if len(M1)*len(M1[0]) > len(M2)*len(M2[0]):
        M = A.T()*A
    else:
        M = A*A.T()

    #I avoid using eig since for more ill-posed matrices the error increase
    max = sqrt(abs(power(M)[0]))
    min = sqrt(abs(inv_power(M)[0]))
    return max*min