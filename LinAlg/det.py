from matrix import Matrix
from lu import lu

def det(A:Matrix):
    [Arows,_] = A.size()
    [_,U,_] = lu(A)
    det = 1
    for i in range(Arows):
        det *= U[i][i]
    return det
