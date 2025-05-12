from matrix import Matrix
from lu import lu

def det(A:Matrix):
    [_,U,_] = lu(A)
    det = 1
    for i in range(len(A)):
        det *= U[i][i]
    return det
