import sys
import init
from LinAlg.matrix import Matrix,Vector,ndarray

### This file implements tests to see if all the functionalities in LinAlg.matrix function or not, since without them nothing else will work

matrix = [[1,1,1],[1,1,1],[1,1,1]]
A = Matrix([[1,1,1],[1,1,1],[1,1,1]])
tests_passed = 0

if A.matrix != matrix:
    print("Major error: Matrix generation not working!")
    sys.exit()

tests_passed += 1

B = Vector([2,2])
print(B)
A[1:2,0] = B
print(A)