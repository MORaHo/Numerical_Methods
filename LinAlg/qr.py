import sys
import init
from math import sqrt
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

def project(vec1:Vector,vec2:Vector):
    print(vec1.T()*vec2)
    s = (vec1.T() * vec2) / (vec2.T() * vec2)
    return vec2 * s

def orthogonalise(A:Matrix):
    [Arows,Acols] = A.size()
    V = zeros(Arows,Acols)
    for i in range(Acols):
        veci = get_column(A,i)
        const_vec_i = get_column(A,i)
        for k in range(i):
            veci -= project(const_vec_i,get_column(V,k))
        V.set_column(i,veci)
    return V

def orthonormalise(A:Matrix):
    V = orthogonalise(A)
    for i in range(len(V)):
        vec_i = get_column(V,i)
        normal = sqrt(vec_i.T()*vec_i)
        V.set_column(i,vec_i/normal)
    return V

def MGS_qr(A:Matrix):
    Q = orthonormalise(A)
    R = Q.T()*A
    return [Q,R]

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
        print(v)
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

#qr = qr_decomposition = house_qr
qr = qr_decomposition = gram_schmidt = MGS_qr


