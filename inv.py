import matrix
from det import det
from utils import copy,eye
import sys
from meg import meg

Matrix = matrix.Matrix

def inv(M:Matrix):

    if len(M) != len(M[0]) or det(M) == 0:
        print("Matrix is not invertible")
        sys.exit()

    A = copy(M)
    I = eye(len(M),len(M[0]))

    for j in range(len(A)):
        A[j] = A[j] + I[j]
    
    A = meg(A)
    for j in range(len(A)):
        A_jj = A[j][j]
        if A_jj == 0:
            print("Matrix is not invertible")
            sys.exit()
        A[j] = [ A[j][i]/A_jj for i in range(len(A[0])) ]
    
    for j in range(1,len(A)): # could possible put this in the above loop, to reduce calculations  

         for k in range(j,0,-1):

            A_kj = A[k-1][j] #this should be divided by A[j][j] but that is 1 so I just skipped it
            A[k-1] = [ A[k-1][i] - A_kj*A[j][i] for i in range(len(A[0])) ]
    #i wonder if there is a way to write this as a matrix, not for computers but for human computation
    

    end = len(A[0])

    for j in range(len(A)):
        A[j] = [ A[j][i] for i in range(len(A),end) ]

    return A

#A = [ [3,0,0,3,0],[-3,0,-2,0,0],[0,-1,0,0,-3],[0,0,0,3,3],[0,-1,2,0,1] ]
#print(inv(Matrix(A)))





