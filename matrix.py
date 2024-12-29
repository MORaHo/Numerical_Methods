### This is the base for all the calculations that I intend to do within numerical methods
from typing import Union
import sys

# union type of all number types
numbers = Union[int,float,complex]

class Matrix():
    "A matrix class for use in working with numerical methods"
    
    def __init__(self,data,rows:int=0,columns:int=1):

        if type(data) == list and type(data[0]) == list:
            self.matrix = data
            self.rows = len(data)
            self.columns = len(data[0])

        elif rows == 0: #create column vector
            
            self.rows = len(data)
            self.columns = columns
            self.matrix = [ [ data[i] ] for i in range(self.rows) ]

        elif len(data) != rows*columns:
            print("Data does fit in the matrix")
            sys.exit()

        else:
            self.rows = rows
            self.columns = columns
            self.matrix = [ [ data[i*self.rows+j] for j in range(self.columns) ] for i in range(self.rows) ]

        self.T = self.transpose()
        self.H = self.Htranspose()

    def __getitem__(self,index):
        return self.matrix[index]

    def __setitem__(self,i,item):
        self.matrix[i] = item

    def __len__(self):
        return len(self.matrix)

    def __str__(self):

        string = "\n"
        
        for j in range(len(self.matrix)):
            string += "  "
            for i in range(len(self.matrix[0])):
                number = format(float(self.matrix[j][i]),'.4')
                string += str(number)
                string += "  "
            string += ("\n" + (j<len(self.matrix)-1)*"\n")
        return string


    def __add__(self,B):
        A = self.matrix
        if len(A) == len(B) and len(A[0]) == len(B[0]):
            C = [ [ A[i][j]+B[i][j] for j in range(len(B[0])) ] for i in range(len(B)) ]
            return Matrix(C)
        else:
            print("Matrix dimensions don't match")
            sys.exit()

    def __mul__(self,B): # element-wise scalar multiplication and dot product

        A = self.matrix

        if type(B) in numbers.__args__: #allows element wise moltiplication by scalar with the matrix

            A = self.matrix
            Z = [[ 0 for _ in range(len(A[0]))] for _ in range(len(A))]
            for j in range(len(A)):
                for i in range(len(A[0])):
                    Z[j][i] = B*A[j][i]
            
            return Matrix(Z)

        elif len(A[0]) != len(B): #if the dimensions don't match the dotproduct cannot be performed
            print("Dimensions of the two matrices don't match")
            sys.exit()

        Z = [[ 0 for _ in range(len(B[0]))] for _ in range(len(A))] 
        n = len(A[0])
        
        #dot-product
        for i in range(len(B[0])):
            for j in range(len(A)):
                sum = 0
                for k in range(n):
                    sum += A[j][k] * B[k][i]
                Z[j][i] = sum
        
        if len(Z) == 1 and len(Z[0]) == 1:
            return Z[0][0]
        else:
            return Matrix(Z)

    def __truediv__(self,s): #element-wise division
        A = self.matrix
        S = [[A[j][i]/s  for i in range(len(A[0])) ] for j in range(len(A))]
        return Matrix(S)

    def __sub__(self,s): #subdivision
        A = self.matrix
        S = [ [ 0 for _ in range(len(A[0])) ] for _ in range(len(A)) ]
        if len(A) != len(s) or len(A[0]) != len(s[0]):
            print("Matrix dimensions do not match")
            sys.exit()
        else:
            for i in range(len(A)):
                for j in range(len(A[0])):
                    S[i][j] = A[i][j] - s[i][j]
            
            return Matrix(S)

    def reshape(self,rows:int,columns:int): #allows the dimensioning of a matrix is needed

        if rows*columns != self.columns*self.rows:
            print("Requested reshape does not match matrix size")
            sys.exit()
        else:
            flat = []
            for i in range(self.rows):
                for j in range(self.columns):
                    flat.append(self.matrix[i][j])
            self.matrix = [ [ flat[i*columns+j] for j in range(columns) ] for i in range(rows) ]
            self.rows = rows
            self.columns = columns

    def transpose(self):

        A = self.matrix
        T = [ [ A[j][i] for j in range(len(A)) ] for i in range(len(A[0])) ]
        return T
    
    def Htranspose(self): #complex conjugate equivalent of the tranpose

        A = self.matrix
        H = [ [ conj(A[j][i]) if type(A[j][i]) == complex else A[j][i] for j in range(len(A)) ] for i in range(len(A[0])) ]
        return H

    def col(self):

        x = self.matrix
        if len(x) != 1 and len(x[0]) != 1: #it's a matrix not a vector
            print("Cannot take the column of a matrix, function requires vector")
            sys.exit()
        elif len(x) == 1: #matrix is row vector, need to return row vector
            return Matrix(self.T)
        elif len(x[0]) == 1: #it's a column vector, no change is needed
            return Matrix(x)

def conj(integer:numbers):
    return complex(integer.real,-1*integer.imag)


