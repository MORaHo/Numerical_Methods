import sys
import init
from LinAlg.utils import isequal
from LinAlg.matrix import Matrix,Vector,ndarray

### This file implements tests to see if all the functionalities in LinAlg.matrix function or not, since without them nothing else will work

matrix = [[1,1,1],[1,1,1],[1,1,1]]
A = Matrix([[1,1,1],[1,1,1],[1,1,1]])
A_ = Matrix([1,1,1,1,1,1,1,1,1],3,3)
tests_passed = 0

if A.matrix != matrix or A_.matrix != matrix:
    print("Major error: Matrix generation not working!")
    sys.exit()

tests_passed += 1

A1 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
B = Vector([2,2])
C1 = Matrix([[1,1,1],[2,1,1],[2,1,1]])
A1[1:2,0] = B

A2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
B = Matrix([[2,2],[2,2]])
A2[1:2,1:2] = B
C2 = Matrix([[1,1,1],[1,2,2],[1,2,2]])

if not isequal(A1,C1) or not isequal(A2,C2):
    print("Set item not working")
    sys.exit()

tests_passed += 1