### This is the base for all the calculations that I intend to do within numerical methods
from typing import Union
import sys

# union type of all number types
numbers = Union[int,float,complex]

class Matrix():
    "A matrix class for use in working with numerical methods"
    
    def __init__(self,data,rows:int=0,columns:int=1):
        if rows == 0: #automatically make a column vector if no size if given
            rows = len(data)
        if type(data) == list and type(data[0]) == list:
            self.matrix = data
            self.rows = len(data)
            self.columns = len(data[0])
        elif len(data) != rows*columns:
            print("Data does fit in the matrix")
            sys.exit()
        else:
            self.rows = rows
            self.columns = columns
            self.matrix = [ [ data[i*self.rows+j] for j in range(self.columns) ] for i in range(self.rows) ]
    
    def __getitem__(self,index):
        return self.matrix[index]

    def __setitem__(self,i,item):
        self.matrix[i] = item

    def __len__(self):
        return len(self.matrix)
    
    def __str__(self):
        string = "["

        for i in range(len(self.matrix)):
            if i != 0:
                string += " "
            string += "["
            for j in range(len(self.matrix[0])):
                number = format(float(self.matrix[i][j]),'.4')
                string += str(number)

                if j != len(self.matrix[0])-1:
                    string += ", "
            if i != len(self.matrix)-1:
                string += "],\n"
            else:
                string += "]]\n"
        return string


    def __add__(self,B):
        A = self.matrix
        if len(A) == len(B) and len(A[0]) == len(B[0]):
            C = [ [ A[i][j]+B[i][j] for j in range(len(B[0])) ] for i in range(len(B)) ]
            return Matrix(C)
        else:
            print("Matrix dimensions don't match")
            sys.exit()

    def __mul__(self,B): # scalar multiplication and dot product

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

        return Matrix(Z)

    def reshape(self,rows:int,columns:int):

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

def conj(integer:numbers):
    return integer.real-integer.imag

#test1 = Matrix([[1,1,1,1],[1,0,0,1],[1,1,1,1]])
#test2 = Matrix([[1,1,1,1],[1,0,0,1],[1,1,1,1]])
#print(test1[1][2])
#test2 = Matrix([1,2,3,4,5,6,7,8,9],3,3)
#print(test2[1][2])
#test3 = Matrix([[1,2,3],[4,5,6],[7,8,9]],columns = 1, rows = 2)
#print(test1.matrix)
#test1.reshape(rows = 4,columns = 3)
#print(test1.matrix)
#print(conj(1))
#C = test1+test2
#print(C)
#B = Matrix([[1,2],[2,1]])
#C = Matrix([[1,2,3],[4,5,6]])
#A = B*C
#print(A)

