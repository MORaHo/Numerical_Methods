import sys
import matrix
from norm import norm
Matrix = matrix.Matrix
from utils import zeros,eye,copy

def get_column(A:Matrix,i:int):
    
    a_i = []
    for n in range(len(A)):
        a_i.append(A[n][i])
    return Matrix(a_i)

def minor(A:Matrix,offset_:int):
    Z = zeros(len(A)-offset_,len(A[0])-offset_)
    for m in range(len(Z)):
        for n in range(len(Z[0])):
            Z[m][n] = A[m+offset_][n+offset_]

    return Z

def house_qr(A:Matrix):
    m = len(A)
    n = len(A[0])
    if m != n:
        print("Currently unable to decompose non-square matrices")
        sys.exit()
    if m<n:
        print("Matrix cannot be QR decomposed")
        sys.exit()
    
    t = (m-1)*(m-1<=n) + (n)*(n<m-1)
    A_k = copy(A)
    Q = eye(m,m)
    for k in range(t):
        v = get_column(A_k,0)
        alfa = norm(v)
        v[0][0] += alfa*(v[k][0]/abs(v[k][0]))
        c = 2/(v.T()*v)
        Q_k = eye(m-k,m-k)-v*v.T()*c # for now just T not H
        if k:
            I = eye(m,m)
            for i in range(m-k):
                for j in range(n-k):
                    I[i+k][j+k] = Q_k[i][j]
            Q_k = I
            Q = Q * Q_k.T()
            R_k = Q_k*R_k
        else:
            R_k = Q_k*A
            Q = Q_k
        A_k = minor(R_k,k+1)
    
    R = R_k
    return [Q,R]

qr = qr_decomposition = house_qr