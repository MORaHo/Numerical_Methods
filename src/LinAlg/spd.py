from src.LinAlg.matrix import Matrix
from src.LinAlg.chol import chol

def spd(A:Matrix):
    # Returns if the matrix is symmetric positive definite.
    try:
        chol(A)
        return True
    except:
        return False