import matrix
from norm import norm

Matrix = matrix.Matrix

toll = 1e-12
nmax = 1000

###############################################################
# This is a calculation of the maximum eigen value of matrix, #
# I will probably implement the QR method at a later date     #
###############################################################

def eig(A:Matrix):

    x = Matrix([ [1] for _ in range(len(A)) ]) # initial guess
    y = x/norm(x,3)
    iter = 0
    rel_err = 1
    print(y.H)
    print(A)
    lambda_ = (Matrix(y.H) * A * y)[0][0] # eventhough its a 1x1 matrix it's still a matrix so to get the value it needs to be extracted

    while iter < nmax and rel_err > toll:
            
        x = A * y
        y = x/norm(x,3)
        old_lambda = lambda_
        lambda_ = (Matrix(y.H)*A*y)[0][0] # safe as a said before
        rel_err = abs(lambda_-old_lambda)/abs(lambda_) #this is the reason we need to extract the value
        iter += 1
    return lambda_

A = Matrix([[1,2,3],[4,5,6],[7,8,9]])

print(eig(A))










