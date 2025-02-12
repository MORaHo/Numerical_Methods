from matrix import Matrix
from norm import norm
from inv import inv
from qr import qr

toll = 2e-16 #tolerance we'll be using for power methods
nmax = 250 #maximum number of iterations 

def eig(A:Matrix):
    
    A_k = A
    k = 0  
    while k < nmax: #I don't know what the end loop conditions are so currently it's only limited by the numbers of iterations

        [Q_k,R_k] = qr(A_k)
        A_k = R_k*Q_k #iteration of A_k to make it into a upper triangular matrix with the eigen values on the primary diagonal
        k+= 1
    
    lambdas = [ A_k[i][i] for i in range(len(A_k))] #vector of eigenvalues to be exported on the principal diagonal of the A_k matrix

    return Matrix(lambdas)

power_method = maxeig
inverse_power_method = mineig
eigen = eig

A = Matrix([1,2,3,4,5,6,7,8,9],3,3)
print(maxeig(A)[0])
