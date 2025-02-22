import matrix
from typing import Union
Matrix = matrix.Matrix
numbers = Union[int,float,complex]
from utils import copy
from math import sqrt

def norm(M:Matrix,type_ = 3) -> numbers: #this will be changes to 2 when the spectral norm is implemented
    
    A = copy(M)
    [Arows,Acols] = A.size()
    
    match type_:
        
        case 1:
            norm = 0
            for i in range(Acols):
                sum = 0
                for j in range(Arows):
                    sum += abs(A[j][i])
                if sum > norm:
                    norm = sum
            return norm

        case 100: #infinity norm but I can used infinity
            norm = 0
            for j in range(Arows):
                sum = 0
                for i in range(Acols):
                    sum += abs(A[j][i])
                if sum > norm:
                    norm = sum
            return norm

        case 3: #Eucledian, 2 will be reserved for what will be the spectral norm or there will be a distinction between vector and matrix normss
            
            norm = 0
            for j in range(Arows):
                for i in range(Acols):
                    norm += A[j][i]**2
            
            return sqrt(norm)


