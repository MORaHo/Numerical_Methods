import matrix
from norm import norm
Matrix = matrix.Matrix
from utils import zeros


def qr_decomp(A:Matrix):

    AT = A.T #this makes the columns of A into the rows of AT making it easier to extract them
    e_k = []
    Q  = []
    R = zeros(len(A),len(A[0]))

    for k in range(len(A)):
        a_k = Matrix(AT[k])# this AT[k] is a list of integers and we are not inputtin the desired shape, because of how I wrote the class this will automatically be converted into a row vector
        #print(a_k)
        u_k = a_k
        
        for i in range(k):
            u_k -= e_k[i] * ( Matrix(a_k.T) * e_k[i] )

        e_i = u_k/norm(u_k,3)
        e_k.append(e_i) #
        
        for i in range(0,k+1):
            R[i][k] = Matrix(a_k.T)*e_k[i]

    for n in range(len(e_k)):
        Q.append((e_k[n].T)[0])#Appends what should be  the i-th column of Q as a row, so we can later transpose it and actually get Q

    Q = Matrix(Q).T #actually getting Q

    return [Matrix(Q),R]

