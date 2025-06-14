import init
from LinAlg.qr import qr
from LinAlg.utils import ndabs,diag
from LinAlg.matrix import Matrix,Vector

toll = 2e-16 #tolerance we'll be using for power methods
nmax = 250 #maximum number of iterations 

# currenctly using this gives a lot of error so for now I wull substitute with a LU decomposition

def triag(A:Matrix):
    
    A_k = A
    k = 0 
    Q = 1
    while k < nmax: #I don't know what the end loop conditions are so currently it's only limited by the numbers of iterations

        [Q_k,R_k] = qr(A_k)
        Q *= Q_k
        A_k = R_k*Q_k #iteration of A_k to make it into a upper triangular matrix with the eigen values on the primary diagonal
        p = diag(A_k)
        pp1 = ndabs(Vector(p[1:len(p)]))
        p = ndabs(Vector(p[0:len(p)-1]))
        pm1 = diag(A_k,-1)
        n = 0
        for i in range(len(pm1)):
            if pm1[i][0] < toll*(pp1[i][0]+p[i][0]):
                n += 1
        if n == len(p): #if all elements fall under the end condition, then end the look
            break
        k+= 1
    
    return A_k