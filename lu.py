import matrix
from utils import eye,zeros,copy
import sys

Matrix = matrix.Matrix

def lu(A:Matrix):

    #global U
    U = copy(A)

    if len(U) != len(U[0]): # if the matrix is not square it will not work
        print("Matrix is not square")
        sys.exit()

    L = zeros(len(U),len(U[0]))
    P = eye(len(U),len(U[0]))

    for k in range(len(U)-1):
        largest_value = U[k][k]
        row = k
        
        for i in range(k,len(U)): #check the with the largest number on the k-th column so we can pivot and reduce the error, also permit some matrices that wouldn't otherwise be able to be decomposed eventhough the fit the requirements to be decomposed.
            if abs(U[i][k]) > abs(largest_value):
                largest_value = U[i][k]
                row = i
        
        if row != k: #pivoting
            temp = U[k]
            U[k]=A[row]
            U[row]=temp
            temp = P[k]
            P[k] = P[row]
            P[row]=temp
            temp = L[k]
            L[k] = L[row]
            L[row] = temp

        A_kk = U[k][k]
        for j in range(k+1,len(U)):
            
            l_jk = U[j][k]/A_kk
            U[j] = [ U[j][c]- l_jk*A[k][c] for c in range(0,len(U[0])) ]
            L[j][k] = l_jk

    L += eye(len(L),len(L[0]))  

    return [L,U,P]

