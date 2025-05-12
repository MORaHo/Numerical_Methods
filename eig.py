from matrix import Matrix
from norm import norm
from inv import inv
from qr import qr

toll = 2e-16 #tolerance we'll be using for power methods
nmax = 250 #maximum number of iterations 

def maxeig(A:Matrix):
    ## Implementation of the power method, used to find the largest eigenvalue

    x = Matrix([ [1] for _ in range(len(A)) ]) # initial guess
    y = x/norm(x,3)
    iter = 0
    rel_err = 1
    lambda_ = y.H() * A * y # eventhough its a 1x1 matrix it's still a matrix so to get the value it needs to be extracted

    while iter < nmax and rel_err > toll:
            
        x = A * y
        y = x/norm(x,3)
        old_lambda = lambda_
        lambda_ = y.H()*A*y # safe as a said before, Rayleigh quotient
        rel_err = abs(lambda_-old_lambda)/abs(lambda_) #this is the reason we need to extract the value
        iter += 1

    eigvalue = lambda_
    eigvector = x
    return [eigvalue,eigvector]

def mineig(A:Matrix):
    ## Implementation of the inverse power method to find the eigenvalue of minimum value
    invA = inv(A)
    return maxeig(invA)

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
