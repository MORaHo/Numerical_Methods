import init
from LinAlg import vand,solve,matrix
Vector = matrix.Vector
solver = solve.solve
vandermonde = vand.vand

def polyfit(x_nodes:Vector,y_nodes:Vector,n:int):
    V = vandermonde(x_nodes,n)
    p = solver(V,y_nodes)
    return p

x = Vector([0,1,2,3,4,5])
y = Vector([0,1,2,3,4,5])
print(polyfit(x,y,2))