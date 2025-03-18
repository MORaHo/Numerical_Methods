import init
import matplotlib.pyplot as mtpl
from Misc.linspace import linspace
from LinAlg.utils import zeros
from LinAlg.matrix import Vector
from Math.cos import cos
def fixed_point(x0,f,nmax:int,toll:int,a,b):
    
    """
    Input Parameters:
    x0 -> Initial Guess
    f -> Function for root determination
    nmax -> Iteration Limit
    toll -> Tollerance Limit
    a,b -> Exploration interval, only for graphical output

    Output Parameters:
    succ -> Iteration vector (let's value is the solution)
    it -> Completed Iterationss
    """

    x = linspace(a,b,1000)
    phi = lambda x: f(x) + x

    succ = [x0]
    x = x0
    x = phi(x)
    succ.append(x)
    err = toll+1
    it = 1

    while err >= toll and it < nmax:
        xold = x
        x = phi(xold)
        succ.append(x)
        err = abs(x-xold)
        it = it + 1

    if it < nmax:
        print('\n Iteration Number: ',it)
        print('\n Calculated fixed point: ',succ[-1])
        print('\n')
    else:
        print('Max number of iterations reaches.')

    return [Vector(succ),it]

f = lambda x: cos(x)
x0 = 0
nmax = 1000
a = 0
b = 3
toll = 1e-6

fixed_point(x0,f,nmax,toll,a,b)
