from matrix import Matrix
from lu import lu

def det(A:Matrix):
    [L,U,_] = lu(A)
    det = 1
    for i in range(len(A)):
        det *= (U[i][i] * L[i][i])
    return det
