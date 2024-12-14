from matrix import Matrix
from lu import lu

def det(A:Matrix):
    [L,U,_] = lu(A)
    det = 1
    for i in range(len(A)):
        det *= (U[i][i] * L[i][i])
    return det

A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
[L,U,P] = lu(A)
print(A)
