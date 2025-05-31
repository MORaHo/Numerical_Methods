import init
from LinAlg.matrix import Matrix
import chols

def spd(A:Matrix):
    # Returns if the matrix is symmetric positive definite.
    try:
        L = chol(A)
        return True
    except:
        return False