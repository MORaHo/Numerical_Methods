import matrix
from typing import Union
Matrix = matrix.Matrix
numbers = Union[int,float,complex]
from utils import copy
from math import sqrt

def norm(M:Matrix,type_ = 3) -> numbers: #this will be changes to 2 when the spectral norm is implemented
    
    A = copy(M)
    
    match type_:
        
        case 1:
            norm = 0
            for i in range(len(A[0])):
                sum = 0
                for j in range(len(A)):
                    sum += abs(A[j][i])
                if sum > norm:
                    norm = sum
            return norm

        case 100: #infinity norm but I can used infinity
            norm = 0
            for j in range(len(A)):
                sum = 0
                for i in range(len(A[0])):
                    sum += abs(A[j][i])
                if sum > norm:
                    norm = sum
            return norm

        case 3: #Eucledian, 2 will be reserved for what will be the spectral norm or there will be a distinction between vector and matrix normss
            
            norm = 0
            for j in range(len(A)):
                for i in range(len(A[0])):
                    norm += A[j][i]**2
            
            return sqrt(norm)


