from matrix import Matrix,Vector
import sys
from norm import norm
from solve import solve
from utils import eye
from inv import inv
from power import power

def richardson(A:Matrix,b:Vector,P:Matrix,x0:Vector,tol,nmax:int,alpha):

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
    [Arows,Acols] = A.size()

    B = eye(n) - alpha * (inv(P) * A)
    if abs(power(B)[0]) > 1:
        print("System will not converge")
        sys.exit()


    if Arows != n or Acols != n or len(x0) != n:
        print("Imcompatible dimensions of parameters")
        sys.exit()

    x = x0
    k = 0
    r = b - A*x
    normalized_res = norm(r) / norm(b)

    while normalized_res > tol and k<nmax:

        z = solve(P,r)
        x = x + alpha * z
        r = r - alpha*(A*z)
        normalized_res = norm(r)/norm(b)
        k = k + 1


    print("Converged in",k,"iterations.")
    return [x,k]
