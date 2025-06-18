import init
from LinAlg.matrix import Matrix,Vector
from LinAlg.utils import diag,zeros

def thomas(A:Matrix,d:Vector):

    # Thomas algorithm for solving tridiagonal matrices
    # https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm

    c = diag(A,1)
    b = diag(A)
    a = diag(A,-1)
    n = len(d)
    c_prime = zeros(n-1)
    d_prime = zeros(n)
    c_prime[0] = [c[0][0]/b[0][0]]
    d_prime[0] = [d[0][0]/b[0][0]]

    for i in range(1,n-1):
        c_prime[i] = [ c[i][0]/(b[i][0]-a[i][0]*c_prime[i-1][0]) ]

    for i in range(1,n):
        d_prime[i] =  [ ( d[i][0]-a[i-1][0]*d_prime[i-1][0] )/( b[i][0]-a[i-1][0]*c_prime[i-1][0] ) ]

    x = zeros(n)
    x[-1] = d_prime[-1]

    for i in range(n-2,-1,-1):
        x[i] = [d_prime[i][0]-c_prime[i][0]*x[i+1][0]]

    return x