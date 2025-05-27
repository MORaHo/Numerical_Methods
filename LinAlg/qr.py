import sys
import init
from math import sqrt
from LinAlg.matrix import Matrix,Vector
from LinAlg.norm import norm
from LinAlg.utils import zeros,eye,copy
from LinAlg.power import power

def get_column(A:Matrix,i:int):
    [Arows,_] = A.size()
    a_i = []
    for n in range(Arows):
        a_i.append(A[n][i])
    return Vector(a_i)

def project(vec1:Vector,vec2:Vector):
    s = (vec1.T() * vec2) / (vec2.T() * vec2)
    return vec2 * s

def orthogonalise(A:Matrix):
    [Arows,Acols] = A.size()
    V = zeros(Arows,Acols)
    for i in range(Acols):
        veci = A[:,i]
        const_vec_i = A[:,i]
        for k in range(i):
            veci -= project(const_vec_i,V[:,k])
        V[:,i] = veci
    return V

def orthonormalise(A:Matrix):
    V = orthogonalise(A)
    for i in range(len(V)):
        vec_i = V[:,i]
        normal = sqrt(vec_i.T()*vec_i)
        V[:,i] = vec_i/normal
    return V

def MGS_qr(A:Matrix):
    Q = orthonormalise(A)
    R = Q.T()*A
    return [Q,R]

def householder(x:Vector):
    alpha = x[0][0]
    s = norm(Vector(x[1:]))**2
    v = copy(x)

    if s == 0:
        tau = 0
    else:
        t = sqrt(alpha**2 + s)
        if alpha <= 0:
            v[0][0] = alpha-t
        else:
            v[0][0] = -s / (alpha+t)

        tau = 2 * v[0][0]**2 / (s+v[0][0]**2)
        v = v/v[0][0]
    return [v,tau]

def qr_householder(A:Matrix):
    # qr method applied through householder reflections

    [m,n] = A.size() # m = Arows and n = Acols, to avoid rewriting a lot
    ending = n-1
    if m != n:
        ending = n
    if m<n:
        print("Matrix cannot be QR decomposed")
        sys.exit()
    

    R = copy(A)
    Q = eye(m)
    for k in range(0,ending):

        [v,tau] = householder(R[k:,k])
        H = eye(m)
        T = tau * (v.col() * v.row())
        H[k:,k:] -= T
        R = H*R
        Q = H*Q

    return [Q.T(),R]

qrgs = gram_schmidt = MGS_qr
qr = qrh =qr_householder