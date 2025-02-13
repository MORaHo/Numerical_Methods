import matrix
import sys

Matrix = matrix.Matrix

def vandermonde(x:Matrix,n:int):
    
    V = []
    if not( len(x) == 1 or len(x[0]) == 1 ): #checking if x is a vectors
        print("Object is not a vector")
        sys.exit()
    
    x = x.col() #making sure it's a column vector

    for m in range(len(x)):
        V.append([ x[m][0]**i for i in range(n,-1,-1)])
    
    return Matrix(V)

vand = vander = vandermonde
