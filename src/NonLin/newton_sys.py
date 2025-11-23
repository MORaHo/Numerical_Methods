from src.LinAlg import Vector,Matrix,solve,norm

EPS = 1E-6

#This is my implementation of Newton's algorithm for root-finding, applied to a system of linear and non-linear equations
#For the functioning of the system, the inputs f and J_f need to lambda functions or just functions since using my mathematical functions will not work as they require a defined input rather than an arbirary one.

def newton_sys(f:Vector,J_f:Matrix,x0:Vector,tol=EPS,nmax=1000):
    
    n = 0
    err = tol+1
    x = x0
    while err > tol and n < nmax:
        Jx = J_f(x)
        R = f(x)
        delta = solve(Jx,R)*-1
        x = x + delta
        err = norm(delta,1)
        n += 1

    R = norm(f(x),1)

    if err>tol:
        print("Did not converge.")
    return [x,R,n]