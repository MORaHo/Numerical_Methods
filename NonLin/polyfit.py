import init
from LinAlg import vand,solve,matrix
from Maths.maths import log
Vector = matrix.Vector
solver = solve.solve
vandermonde = vand.vand

def polyfit(x_nodes:Vector,y_nodes:Vector,n:int):
    V = vandermonde(x_nodes,n)
    p = solver(V,y_nodes)
    return p

#x = Vector([1,2,3,4,5])
#y = Vector([1,2,3,4,5])
#y = 2*(x**2)
#y = log(x)
#print(polyfit(x,y,2))