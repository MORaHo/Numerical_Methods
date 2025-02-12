from matrix import Matrix
import sys
from norm import norm
from solve import solve
from utils import ones,zeros,diag,eye,tril
from inv import inv
from power import power

def richardson(A:Matrix,b:Matrix,P:Matrix,x0:Matrix,tol,nmax:int,alpha):

    ## Input Arguements:
    #
    # A: System Matrix
    # b: Known value vector
    # P: Precondition matrix
    # x0: Initial guess
    # tol: tollerance
    # nmax: Max iteration number
    # alpha: Acceleration parameter
    #
    ## Output Arguements:
    #
    # x: solution
    # k: number of iterations

    n = len(b)

    B = eye(n,n) - (inv(P) * A) * alpha
    if abs(power(B)[0]) > 1:
        print("System will not converge")
        sys.exit()

    #if len(A) != n or len(A[0]) != n or len(x0) != 0:
    #    print("Imcompatible dimensions of parameters")
    #    sys.exit()

    x = x0
    k = 0;
    r = b - A*x
    normalized_res = norm(r) / norm(b)

    while normalized_res > tol and k<nmax:

        z = solve(P,r)
        x = x + z * alpha
        r = r - (A*z)*alpha
        normalized_res = norm(r)/norm(b)
        k = k + 1


    print("Converged in",k,"iterations.")
    return [x,k]
