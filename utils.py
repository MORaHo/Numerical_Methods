from matrix import Matrix
from typing import Union

numbers = Union[int,float,complex]

def eye(m:int,n:int=1):
    I = [ [ 1 if i == j else 0 for j in range(m) ] for i in range(n) ]
    return Matrix(I)

def zeros(m:int,n:int=1):
    Z = [ [ 0 for _ in range(m) ] for _ in range(n) ]
    return Matrix(Z)

