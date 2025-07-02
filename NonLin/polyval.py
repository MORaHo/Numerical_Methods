import init
from Maths.sin import sin
from LinAlg.utils import zeros
from LinAlg.matrix import Vector
from Misc.linspace import linspace
from NonLin.polyfit import polyfit

def polyval(p:Vector,xeval:Vector):

    n = len(p)
    xinit = xeval.col()
    x = len(xinit)
    xeval = zeros(x)
    for i in range(x):
        for j in range(n):
            xeval[i][0] += p[n-j-1][0] * xinit[i][0]**j

    return xeval

# We can also consider the case with small of number of points in x, and y = log(x) which will give large error near 0 as there polynomial will not be able to match the logarithmic descent to -infty with the small number of points given
#x = Vector([0.5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
#y = sin(x)
#p = polyfit(x,y,16)
#xeval = linspace(0.6,10,101)
#print(polyval(p,xeval)-sin(xeval))