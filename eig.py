import matrix
from norm import norm
from inv import inv
from qr import qr

Matrix = matrix.Matrix

toll = 1e-12
nmax = 250

###############################################################
# This is a calculation of the maximum eigen value of matrix, #
# I will probably implement the QR method at a later date     #
###############################################################
# Done! (it doesn't work for one matrix idk why though)       #
###############################################################

def maxeig(A:Matrix):

    x = Matrix([ [1] for _ in range(len(A)) ]) # initial guess
    y = x/norm(x,3)
    iter = 0
    rel_err = 1
    lambda_ = Matrix(y.H) * A * y # eventhough its a 1x1 matrix it's still a matrix so to get the value it needs to be extracted

    while iter < nmax and rel_err > toll:
            
        x = A * y
        y = x/norm(x,3)
        old_lambda = lambda_
        lambda_ = Matrix(y.H)*A*y # safe as a said before, Rayleigh quotient
        rel_err = abs(lambda_-old_lambda)/abs(lambda_) #this is the reason we need to extract the value
        iter += 1
    return lambda_

def mineig(A:Matrix): # used to find minimum eigen value, which is needed to see if a matrix is defined positive
    invA = inv(A)
    x = Matrix([ [1] for _ in range(len(A)) ])
    y = x/norm(x,3)
    iter = 0
    rel_err = 1
    lambda_ = Matrix(y.H) * A * y

    while iter < nmax and rel_err > toll:

        x = invA*y
        y = x/norm(x,3)
        old_lambda = lambda_
        lambda_ = Matrix(y.H)*A*y
        rel_err = abs(lambda_-old_lambda)/abs(lambda_)
        iter += 1
    return lambda_

def eig(A:Matrix):
    
    A_k = A
    k = 0  
    while k < nmax: #I don't know what the end loop conditions are so currently it's only limited by the numbers of iterations

        [Q_k,R_k] = qr(A_k)
        A_k = R_k*Q_k #iteration of A_k to make it into a upper triangular matrix with the eigen values on the primary diagonal
        k+= 1
    
    lambdas = [ A_k[i][i] for i in range(len(A_k))] #vector of eigenvalues to be exported on the principal diagonal of the A_k matrix

    return Matrix(lambdas)


