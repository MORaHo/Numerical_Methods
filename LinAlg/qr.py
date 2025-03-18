import sys
import init
from LinAlg.matrix import Matrix,Vector
from LinAlg.norm import norm
from LinAlg.utils import zeros,eye,copy


def get_column(A:Matrix,i:int):
    [Arows,_] = A.size()
    a_i = []
    for n in range(Arows):
        a_i.append(A[n][i])
    return Vector(a_i)

def minor(A:Matrix,offset_:int):

    [Arows,Acols] = A.size()
    Zrows = Arows-offset_
    Zcols = Acols-offset_
    Z = zeros(Zrows,Zcols)

    for m in range(Zrows):
        for n in range(Zcols):
            Z[m][n] = A[m+offset_][n+offset_]

    return Z

def house_qr(A:Matrix):

    [m,n] = A.size() # m = Arows and n = Acols, to avoid rewriting a lot
    if m != n:
        print("Currently unable to decompose non-square matrices")
        sys.exit()
    if m<n:
        print("Matrix cannot be QR decomposed")
        sys.exit()
    
    t = (m-1)*(m-1<=n) + (n)*(n<m-1)
    A_k = copy(A)
    Q = eye(m)
    for k in range(t):
        v = get_column(A_k,0)
        alfa = norm(v)
        v[0][0] += alfa*(v[k][0]/abs(v[k][0]))
        c = 2/(v.T()*v)
        Q_k = eye(m-k)-v*v.H()*c # for now just T not H
        if k:
            I = eye(m)
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