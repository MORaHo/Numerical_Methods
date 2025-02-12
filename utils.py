import matrix
from typing import Union
import sys

Matrix = matrix.Matrix
numbers = Union[int,float,complex]

def eye(m:int,n:int=1):
    I = [ [ 1 if i == j else 0 for j in range(m) ] for i in range(n) ]
    return Matrix(I)

def ones(m:int,n:int=1):
    Z = [ [ 1 for _ in range(n) ] for _ in range(m) ]
    return Matrix(Z)

def zeros(m:int,n:int=1):
    Z = [ [ 0 for _ in range(n) ] for _ in range(m) ]
    return Matrix(Z)

def copy(A:Matrix):
    N = [[ A[j][i] for i in range(len(A[0]))] for j in range(len(A))]
    return Matrix(N)

def diag(A:Matrix,offset_:int=0):

    if len(A) == 1 or len(A[0]) == 1: # matrix is a vector so we create a matrix

        shift_y = (offset_ < 0)
        shift_x = (offset_ > 0)
        zero_case = (offset_ == 0) #without this there would need to be a if statement to handle the case where offset_ = 0

        column = (len(A)>1) #allows use to handle both column and row vectors
        row = (len(A[0])>1)

        dim = len(A)*(len(A)>1) + len(A[0])*(len(A[0])>1) + abs(offset_)
        B = zeros(dim,dim)

        for i in range(dim):
            for j in range(dim):  
                if i-shift_x*offset_ == j+shift_y*offset_:       
                    
                    #allow use handle positive, negative and null offsets, as well as row and column vectors 
                    A_j = shift_x*column*j + shift_y*column*i + zero_case*column*j
                    A_i = shift_y*row*i + shift_x*row*j + zero_case*row*i

                    B[j][i] = A[A_j][A_i]
        return B
                    

    elif len(A) == len(A[0]): # matrix is a matrix so we create a vector

        shift_y = (offset_ < 0) #one of the two shifts will be true, if offset_ is non-zero
        shift_x = (offset_ > 0)
        B = []
        
        # I tried to use list comprehension, but it didn't seem to work
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i-shift_x*offset_ == j+shift_y*offset_: #it needs to be added to j since it positive
                    B.append([A[j][i]])
        
        return Matrix(B)

    else:
        print("Matrix is not vector or square matrix")
        sys.exit()

def tril(A:Matrix):
    n = len(A)
    m = len(A[0])
    M = zeros(n,m)
    for i in range(n):
        for j in range(m):
            if i >= j:
                M[i][j] = A[i][j]
    return M

def linspace(a, b, n:int=100):
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return [a + diff*i  for i in range(n)]
