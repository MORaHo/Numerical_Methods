import sys
import init
from LinAlg.lu import lu
from LinAlg.qr import qr
from LinAlg.det import det
from LinAlg.chol import chol
from LinAlg.thomas import thomas
from LinAlg.hess_solve import triag
from LinAlg.matrix import Matrix,Vector
from LinAlg.utils import zeros, tril, triu,diag, isequal

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

    if det(A) == 0:
        print("Solution may not be unique!")

    #this will be expanded to handle more and more cases, initially I intend to add a QR solver and in the end for this function to basically become the \ of matlab
    
    # Following diagram in the algorithm section of https://uk.mathworks.com/help/matlab/ref/double.mldivide.html

    if m != n:
        [Q,R] = qr(A)
        Q1 = Q[:m,:n]
        R1 = R[:n,:n]
        y = Q1.T()*b.col()
        x = bkw_sub(R1,y)
    elif isequal(tril(A),A):
        x = fwd_sub(A,b)
    elif isequal(triu(A),A):
        x = bkw_sub(A,y)
    #elif m <= 16:
    #    [L,U,P] = lu(A)
    #    y = fwd_sub(L,P*b)
    #    x = bkw_sub(U,y)
    else:
        if isequal((triu(A) + diag(diag(A,-1),-1)),A): #is the matrix upper-hessenberg
            if isequal((tril(A) + diag(diag(A,1),1)),A): #If matrix is tridiagonal
                #apply Thomas algorithm
                x = thomas(A,b)
            else:
                #A = triag(A) #convert the matrix to upper-triangular
                #A = triu(A)
                #x = bkw_sub(A,b)
                # since the hess_solve is not working right now, I have defaulted to a LU decomposition
                [L,U,P] = lu(A)
                y = fwd_sub(L,P*b)
                x = bkw_sub(U,y)

        else: #in any other case
            try: #try to apply cholesky
                L = chol(A)
                y = bkw_sub(L.T(),b)
                x = fwd_sub(L,y)
            except: #if cholesky fails (A is not symmetric positive definite) then apply LU factorization
                [L,U,P] = lu(A)
                y = fwd_sub(L,P*b)
                x = bkw_sub(U,y)
    return x

A = Matrix([[2,1,0,0,1],[1,2,1,0,0],[0,1,2,1,0],[0,0,1,2,1],[0,0,0,1,2]])
b = Vector([1,1,1,1,1])
x = solve(A,b)
print(x)
print(A*x-b)