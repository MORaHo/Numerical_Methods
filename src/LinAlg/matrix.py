import sys
from typing import Union

numbers  = Union[int,float,complex]

class ndarray():

    def __init__(self,data,rows:int,columns:int):

        try:

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
        except:
            self.matrix = []
    
    def T(self): #returns matrix transpose

        T = [ [ self[j][i] for j in range(len(self)) ] for i in range(len(self[0])) ]
        return Matrix(T, rows=len(self[0]), columns=len(self))

    def H(self): #complex conjugate equivalent of the tranpose

        M = self.matrix
        H = [ [ conj(M[j][i]) if type(M[j][i]) == complex else M[j][i] for j in range(len(M)) ] for i in range(len(M[0])) ]
        return Matrix(H,len(H),len(H[0]))
    
    def __str__(self):
        """Prints matrix in Matlab style, although the variable name is not printed"""
        string = "\n"
        
        for j in range(len(self)):
            string += "  "
            for i in range(len(self[0])):
                number = format(float(self[j][i]),'.4')
                string += str(number)
                string += "  "
            string += ("\n" + (j<len(self)-1)*"\n")
        return string
    
    def __len__(self):
        return len(self.matrix)
    
    def __getitem__(self,index):

        
        if type(index)==int:
            return self.matrix[index]

        elif type(index)==slice:
            return self.matrix[index]

        try:

            if type(index)==tuple and len(index)==2:

                y,x = index

                if type(y) == slice:
                    y_start = int(0 if y.start == None else y.start)
                    y_end = int(len(self) if y.stop == None else y.stop)
                elif type(y) == int:
                    y_start = y
                    y_end = y+1
                if type(x) == slice:
                    x_start = int(0 if x.start == None else x.start)
                    x_end = int(len(self[0]) if x.stop == None else x.stop)
                elif type(x) == int:
                    x_start = x
                    x_end = x + 1
       
                M = [ [self[j][i] for i in range(x_start,x_end) ] for j in range(y_start,y_end) ]

                if [len(M),len(M[0])] != [1,1]:
                    return Matrix(M)
                else:
                    return M[0][0]
        
        except:
            return []
        
    def __setitem__(self,index,item):

        if type(index)==tuple and len(index)==2:
                
            y,x = index

            if type(item) == Matrix:

                i_n,i_m = item.size()
    
                if type(y) == slice and (type(x) == slice or type(x) == int):
                    
                    if type(x) == slice:

                        y_start = int(0 if y.start == None else y.start)
                        y_end = int(len(self.matrix) if y.stop == None else y.stop)
                        x_start = int(0 if x.start == None else x.start)
                        x_end = int(len(self.matrix[0]) if x.stop == None else x.stop)

                        if i_n != (y_end-y_start) or i_m != (x_end-x_start):
                            print("Item change dimensions do not match, check the what you are trying to change (matrix input case)")
                            sys.exit()

                        for j in range(y_start,y_end):
                            for i in range(x_start,x_end):
                                self[j][i] = item[j-y_start][i-x_start]

                    
                    if type(x) == int:
                        
                        y_start = int(0 if y.start == None else y.start)
                        y_end = int(len(self) if y.stop == None else y.stop)

                        if i_n != (y_end-y_start):
                            print("Item change dimensions do not match, check the what you are trying to change (column vector case)")
                            sys.exit()
                        
                        for j in range(y_start,y_end):
                                self[j][x] = item[j-y_start][x]
                
                elif type(y) == int and type(x) == slice:

                    x_start = int(0 if x.start == None else x.start)
                    x_end = int(len(self[0]) if x.stop == None else x.stop)

                    if i_n != (x_end-x_start):
                        print("Item change dimensions do not match, check the what you are trying to change (row vector case)")
                        sys.exit()
                    
                    for j in range(x_start,x_end):
                            self[x][j] = item[x][j-x_start]

            elif type(item) == Vector:
                
                i_n = len(item)
                if i_n == 1: #it's a row vector
                    start = int(0 if x.start == None else x.start)
                    end = int(len(self[0]) if x.stop == None else x.stop)+1
                    if type(y) != int:
                        print("Item dimensions too large, it is row vector, so cannot span multipe rows")
                else:
                    start = int(0 if y.start == None else y.start)
                    end = int(len(self) if y.stop == None else y.stop)+1
                    if type(x) != int:
                        print("Item dimensions too large, it is column vector, so cannot span multipe columns")

                if i_n != (end-start):
                    print("Item change dimensions do not match, check the what you are trying to change")
                    sys.exit()
                
                if i_n == 1: #again, row vector
                    for j in range(start,end):
                        self[y][j] = item[0][j-start]    
                else:
                    for j in range(start,end):
                        self[j][x] = item[j-start][0]
                

            elif type(item) in numbers.__args__:
                
                if type(x) != int or type(y) != int:
                    print("Input size does not match")
                    sys.exit()
                
                self.matrix[y][x] = item
        
        else:
            self.matrix[index] = item  
        
    def __add__(self,B): # addition

        if type(self) == type(B) and len(self) == len(B) and len(self[0]) == len(B[0]):
            C = [ [ self[i][j]+B[i][j] for j in range(len(B[0])) ] for i in range(len(B)) ]
            return Matrix(C)
        else:
            print("Matrix dimensions or types don't match! (Addition)")
            sys.exit()

    def __sub__(self,s): #subdivision

        if type(self) != type(s) or len(self) != len(s) or len(self[0]) != len(self[0]):
            print("Matrix dimensions or types do not match! (Subtraction)")
            sys.exit()        

        S = [ [ 0 for _ in range(len(self[0])) ] for _ in range(len(self)) ]
        for i in range(len(self)):
            for j in range(len(self[0])):
                S[i][j] = self[i][j] - s[i][j]
            
        return Matrix(S)

    def __mul__(self,B): # element-wise scalar multiplication and dot product

        n,m = self.size() #rows,columns

        if type(B) in numbers.__args__: #allows element wise moltiplication by scalar with the matrix
            
            Z = [[ B*self[j,i] for i in range(m)] for j in range(n)]
            #for j in range(len(M)):
            #    for i in range(len(M[0])):
            #        Z[j][i] = B*M[j][i]
            
            return Matrix(Z)

        elif m != len(B): #if the dimensions don't match the dotproduct cannot be performed
            print("Dimensions of the two matrices don't match")
            sys.exit()

        Z = Matrix([[ 0 for _ in range(len(B[0]))] for _ in range(n)])
        
        #dot-product
        for i in range(len(B[0])):
            for j in range(n):
                sum = 0
                for k in range(m):
                    sum += self[j,k] * B[k,i]
                Z[j,i] = sum
        
        if len(Z) == 1 and len(Z[0]) == 1:
            return Z[0,0]
        else:
            return Z
        
    def __rmul__(self,m):
        return self.__mul__(m)

    def __truediv__(self,s): #element-wise division
        [n,m] = self.size()
        S = [[self[j][i]/s  for i in range(m) ] for j in range(n)]
        return Matrix(S)

    def __pow__(self,b):
        
        if type(b) == int or type(b) == float:
            I = []
            [rows,cols] = self.size()
            for j in range(rows):
                for i in range(cols):
                    I.append(self[j][i] ** b)
            return Matrix(I,rows,cols)
        
        # matmul didn't work for some reason I just chose to repurpose the power operator to permit element-wise matrix multiplication
        # this will be useful when discretizing for non-linear analysis and solving ODEs
        elif isinstance(b,ndarray):
            if self.size() != b.size():
                print("Dimensions do not match for element-wise multiplication")
                sys.exit()
            [rows,cols] = self.size()
            P = []
            for j in range(rows):
                for i in range(cols):
                    P.append(self[j][i] * b[j][i])
            return Matrix(P,rows,cols)
    
    def size(self):
        # returns [rows,columns]
        if type(self) == Matrix:
            return [len(self),len(self[0])]
        elif type(self) == Vector:
            if not self.is_row:
                return [len(self.matrix),1]
            return [1,len(self.matrix[0])]

class Matrix(ndarray):

    def __new__(cls,data,rows:int=0,columns:int=0):
        if rows < 2 or columns < 2:
            if columns == 0 and len(data) == 1: #it's a row 
                return Vector(data,is_row = 1)
            try:
                if len(data[0]) == 1:
                    return Vector(data)
                else:
                    return super(Matrix, cls).__new__(cls)
            except:
                return Vector(data)

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

    def __init__(self,data,is_row:bool=False):
        if is_row and type(data[0]) != list:
            self.is_row = is_row
            rows = 1
            cols = len(data)
            super().__init__(data,rows,cols)
        elif len(data) == 1 and type(data[0]) == list:
            self.is_row = True
            rows = 1
            cols = len(data[0])
            super().__init__(data,rows,cols)
        elif len(data) == 1:
            self.is_row = True
            rows = 1
            cols = 1
            super().__init__(data,rows,cols)
        else:
            self.is_row = False
            rows = len(data)
            cols = 1
            super().__init__(data,rows,cols)

    def col(self): #function to make vectors columns

        if self.is_row: #matrix is row vector, need to return column vector
            return self.T()
        else: #it's a column vector, no change is needed
            return self   

    def row(self): #function to make vectors columns

        if self.is_row: #matrix is column vector, need to return row vector
            return self
        else: #it's a row vector, no change is needed
            return self.T()
        
    def sum(self):
        rows = len(self)
        s = 0
        try:
            for j in range(rows):
                s += self[j][0]
            return s
        except:
            return s

def conj(integer:numbers):
    return complex(integer.real,-1*integer.imag)