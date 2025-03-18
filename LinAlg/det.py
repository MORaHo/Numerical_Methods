import init
from LinAlg.matrix import Matrix
from LinAlg.lu import lu

def det(A:Matrix):
    [Arows,_] = A.size()
    [_,U,_] = lu(A)
    det = 1
    for i in range(Arows):
        det *= U[i][i]
    return det
