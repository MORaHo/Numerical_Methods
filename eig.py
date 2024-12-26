import matrix
from norm import norm
from inv import inv
from qr import qr_decomp
from utils import zeros, diag, ones

Matrix = matrix.Matrix

toll = 1e-12
nmax = 1000

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
    nmax = 1000
    k = 0  
    while k < nmax:

        [Q_k,R_k] = qr_decomp(A_k)
        A_k = R_k*Q_k #iteration of A_k to make it into a upper triangular matrix with the eigen values on the primary diagonal
        k+= 1

    return A_k


#A = diag(ones(10,1)*2)+diag(ones(9,1)*-1,-1)+diag(ones(9,1)*-1,1)
#A = Matrix([[1,1,0],[1,0,1],[0,1,1]]) #the only matrix that doesn't work
#print(eig(A))










