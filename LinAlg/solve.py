import sys
import init
from LinAlg.matrix import Matrix,Vector
from LinAlg.lu import lu
from LinAlg.qr import qr
from LinAlg.utils import zeros

def forward_substitution(L:Matrix,b:Matrix):
    
    b = b.col()
    y = []
    y.append(b[0][0]/L[0][0])

    for j in range(1,len(b)):
        b_j = b[j][0]
        for i in range(j):
            b_j -= L[j][i]*y[i]
        y.append(b_j/L[j][j])
    
    return Matrix(y)

fwd_sub = forward_substitution

def backward_substitution(U:Matrix,y:Matrix):
    y = y.col()
    n = len(y)-1
    x = zeros(n+1,1).matrix
    x[n][0] = y[n][0]/U[n][n]
    
    for j in range(n-1,-1,-1):
        y_j = y[j][0]
        for i in range(n,j,-1):
            y_j -= U[j][i]*x[i][0]
        x[j][0] = y_j/U[j][j]

    return Matrix(x)

bkw_sub = backward_substitution

def solve(A:Matrix,b:Vector):
    
    [m,n] = A.size()
    if m < n:
        print('System cannot be solved')
        sys.exit()

    #this will be expanded to handle more and more cases, initially I intend to add a QR solver and in the end for this function to basically become the \ of matlab
    
    if m != n:
        [Q,R] = qr(A)
        Q1 = Q[:m,:n]
        R1 = R[:n,:n]
        y = Q1.T()*b.col()
        x = bkw_sub(R1,y)
    else:
        [L,U,_] = lu(A)
        y = fwd_sub(L,b)
        x = bkw_sub(U,y)

    return x