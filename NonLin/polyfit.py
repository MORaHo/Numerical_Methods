import init
from LinAlg import vand,solve,matrix
from Maths.maths import log
Vector = matrix.Vector
solver = solve.solve
vandermonde = vand.vand

## See algorithm section: https://uk.mathworks.com/help/matlab/ref/polyfit.html

def polyfit(x_nodes:Vector,y_nodes:Vector,n:int):
    V = vandermonde(x_nodes,n)
    p = solver(V,y_nodes)
    return p  #coefficient vector for x^n,x^(n-1),....,x,1

#x = Vector([1,2,3,4,5])
#y = Vector([1,2,3,4,5])
#y = 1*(x**2)
#y = log(x)
#print(polyfit(x,y,2))