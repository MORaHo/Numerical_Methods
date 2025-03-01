from typing import Union
import sys

numbers  = Union[int,float,complex]

class ndarray():

    def __init__(self,data,rows:int,columns:int):

        if type(data[0])==list:
            data_size = len(data)*len(data[0])
        else: 
            data_size = len(data)

        if data_size != rows*columns:
            print("Data doesn't fit in the size parameters.")
            sys.exit()

        if type(data) == list and type(data[0]) == list: #if the input data is already a 2d array
            self.matrix = data
        else:
            self.matrix = [ data[ r*columns:r*columns+columns ] for r in range(rows) ]

    
    def T(self): #returns matrix transpose

        M = self.matrix
        T = [ [ M[j][i] for j in range(len(M)) ] for i in range(len(M[0])) ]
        return Matrix(T,len(T),len(T[0]))

    def H(self): #complex conjugate equivalent of the tranpose

        M = self.matrix
        H = [ [ conj(M[j][i]) if type(M[j][i]) == complex else M[j][i] for j in range(len(M)) ] for i in range(len(M[0])) ]
        return Matrix(H,len(H),len(H[0]))
    
    def __str__(self):
        """Prints matrix in Matlab style, although the variable name is not printed"""
        string = "\n"
        
        for j in range(len(self.matrix)):
            string += "  "
            for i in range(len(self.matrix[0])):
                number = format(float(self.matrix[j][i]),'.4')
                string += str(number)
                string += "  "
            string += ("\n" + (j<len(self.matrix)-1)*"\n")
        return string
    
    def __len__(self):
        return len(self.matrix)
    
    def __getitem__(self,index):

        
        if type(index)==int:
            return self.matrix[index]

        elif type(index)==slice:
            return self.matrix[index]

        elif type(index)==tuple and len(index)==2:
            y,x = index
            return self.matrix[y][x]
        
    def __setitem__(self,i,item):
        self.matrix[i] = item  
        
    def __add__(self,B): # addition

        M = self.matrix
        if type(self) == type(B) and len(M) == len(B) and len(M[0]) == len(B[0]):
            C = [ [ M[i][j]+B[i][j] for j in range(len(B[0])) ] for i in range(len(B)) ]
            return Matrix(C)
        else:
            print("Matrix dimensions or types don't match")
            sys.exit()

    def __sub__(self,s): #subdivision

        M = self.matrix
        S = [ [ 0 for _ in range(len(M[0])) ] for _ in range(len(M)) ]

        if type(self) != type(s) or len(M) != len(s) or len(M[0]) != len(M[0]):
            print("Matrix dimensions or types do not match")
            sys.exit()          
        else:
            for i in range(len(M)):
                for j in range(len(M[0])):
                    S[i][j] = M[i][j] - s[i][j]
            
            return Matrix(S)

    def __mul__(self,B): # element-wise scalar multiplication and dot product

        M = self.matrix

        if type(B) in numbers.__args__: #allows element wise moltiplication by scalar with the matrix

            M = self.matrix
            Z = [[ 0 for _ in range(len(M[0]))] for _ in range(len(M))]
            for j in range(len(M)):
                for i in range(len(M[0])):
                    Z[j][i] = B*M[j][i]
            
            return Matrix(Z)

        elif len(M[0]) != len(B): #if the dimensions don't match the dotproduct cannot be performed
            print("Dimensions of the two matrices don't match")
            sys.exit()

        Z = [[ 0 for _ in range(len(B[0]))] for _ in range(len(M))] 
        n = len(M[0])
        
        #dot-product
        for i in range(len(B[0])):
            for j in range(len(M)):
                sum = 0
                for k in range(n):
                    sum += M[j][k] * B[k][i]
                Z[j][i] = sum
        
        if len(Z) == 1 and len(Z[0]) == 1:
            return Z[0][0]
        else:
            return Matrix(Z)
        
    def __rmul__(self,m):
        return self.__mul__(m)

    def __truediv__(self,s): #element-wise division
        M = self.matrix
        S = [[M[j][i]/s  for i in range(len(M[0])) ] for j in range(len(M))]
        return Matrix(S)
    
    def size(self):
        return [len(self.matrix),len(self.matrix[0])]

class Matrix(ndarray):

    def __new__(cls,data,rows:int=0,columns:int=0):
        if rows < 2 or columns < 2:
            if len(data) == 1: #it's a row
                return Vector(data,is_row = 1)
            try:
                if len(data[0]) == 1:
                    return Vector(data)
                else:
                    return super(Matrix, cls).__new__(cls)
            except:
                return Vector(data,is_row=1)
        else:
            return super(Matrix, cls).__new__(cls)

    def __init__(self,data,rows:int=0,columns:int=0):

        rows = rows*(rows!=0)+len(data)*(rows==0)
        try:
            columns = columns*(columns!=0)+len(data[0])*(columns==0)
        except:
            columns = columns
        super().__init__(data=data,rows = rows,columns = columns)

class Vector(ndarray):

    def __init__(self,data,is_row:int=0):
        if is_row and type(data[0]) != list:
            super().__init__(data,1,len(data))
        elif len(data) == 1:
            super().__init__(data,1,len(data[0]))
        else:
            super().__init__(data,len(data),1)

    def col(self): #function to make vectors columns

        x = self.matrix
        if len(x) == 1: #matrix is row vector, need to return column vector
            return self.T()
        elif len(x[0]) == 1: #it's a column vector, no change is needed
            return self   

    def row(self): #function to make vectors columns

        x = self.matrix
        if len(x[0]) == 1: #matrix is column vector, need to return row vector
            return self.T()
        elif len(x) == 1: #it's a row vector, no change is needed
            return self

def conj(integer:numbers):
    return complex(integer.real,-1*integer.imag)

