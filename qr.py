import sys
import matrix
from norm import norm
Matrix = matrix.Matrix
from utils import zeros,eye,copy
from power import power

def qr_ecomposition(A:Matrix):

    AT = A.T().matrix #this makes the columns of A into the rows of AT making it easier to extract them
    e_k = []
    QT  = []
    R = zeros(len(A),len(A[0])) 

    for k in range(len(A)):
        a_k = Matrix(AT[k])# this AT[k] is a list of integers and we are not inputtin the desired shape, because of how I wrote the class this will automatically be converted into a row vector
        #print(a_k)
        u_k = a_k
        
        for i in range(k):
            u_k -= e_k[i] * ( a_k.T() * e_k[i] )

        if norm(u_k,3) < 2e-12: #this solves a problem with matrices with not all linearly independent columns, and one other matrix which was causing issues
            e_i = zeros(len(u_k),1)
        else:
            e_i = u_k/norm(u_k,3)
        
        e_k.append(e_i)
        
        for i in range(0,k+1):
            R[i][k] = a_k.T() * e_k[i]

    for n in range(len(e_k)):
        QT.append((e_k[n].T())[0])#Appends what should be  the n-th column of Q as a row, so we can later transpose it and actually get Q

    Q = Matrix(QT).T() #actually getting Q

    return [Q,R]

#qr = qr_decomposition
#the error understandably increases as the size of the matrix increases

def get_column(A:Matrix,i:int):
    
    a_i = []
    for n in range(len(A)):
        a_i.append(A[n][i])
    return Matrix(a_i)

def qr_decomposition(A:Matrix):
    N = len(A[0])
    M = len(A)
    Q = zeros(M,N)
    for k in range(N):
        q = get_column(A,k)
        for j in range(k):
            q_j = get_column(Q,j)
            q = q - q_j * (q.T() * q_j)
        if norm(q): 
            for m in range(M):
                Q[m][k] = q[m][0]/norm(q)
        else: #if the norm is 0, then the vector is already orthonormal it doesn't need to be normalized
            for m in range(M):
                Q[m][k] = q[m][0]

    R = Q.T()*A
    return [Q,R]

qr = qr_decomposition

#A = Matrix([1,2,3,4,5,6,7,8,9],3,3)
#[Q,R] = qr(A)
#print(Q.T()*Q)

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

#A = Matrix([10000,10001,10001,10002,10002,10003,10003,10004,10004,10005],5,2)
A = Matrix([1,2,3,4,5,6,7,8,9],3,3)
[Q,R] = house_qr(A)
print(Q)
print(R)
