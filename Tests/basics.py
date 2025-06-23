import sys
import init
from LinAlg.utils import isequal
from LinAlg.matrix import Matrix,Vector,ndarray

### This file implements tests to see if all the functionalities in LinAlg.matrix function or not, since without them nothing else will work

## Matrix generation test

matrix = [[1,1,1],[1,1,1],[1,1,1]]
A = Matrix([[1,1,1],[1,1,1],[1,1,1]])
A_ = Matrix([1,1,1,1,1,1,1,1,1],3,3)
tests_passed = 0

if A.matrix != matrix or A_.matrix != matrix:
    print("Major error: Matrix generation not working!")
    sys.exit()

x = Vector([1,1,1,1,1])
vector_matrix = [[1],[1],[1],[1],[1]]

if x.matrix != vector_matrix:
    print("Vector not generating properly")
    sys.exit()

tests_passed += 1

## Type-setting test

# These test if the code properly generates a Vector in the special cases we have called upon the matrix generation
x = Matrix([1,1,1,1,1])
vector_matrix = [[1],[1],[1],[1],[1]]
row = Matrix([[1,1,1,1,1]])
row_matrix = [[1,1,1,1,1]]

if x.matrix != vector_matrix or row.matrix != row_matrix:
    print("Vector not generating properly from Matrix call")
    sys.exit()

## __setitem__ test

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

## Transpose test

A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
T = Matrix([[1,4,7],[2,5,8],[3,6,9]])

if not isequal(A.T(),T):
    print("Transpose matrix generation not working!")
    sys.exit()