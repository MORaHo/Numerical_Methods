from matrix import Matrix
from math import sqrt
from power import power,inv_power

### This function is subject to possible change

def cond(A:Matrix):

    max = sqrt(abs(power(A.T()*A)[0]))
    min = sqrt(abs(inv_power(A.T()*A)[0]))
    return max*min