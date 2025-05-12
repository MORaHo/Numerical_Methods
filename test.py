import numpy as np
import numpy.linalg as la
from numpy.linalg import qr

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
Q = np.zeros(A.shape)
for k in range(A.shape[1]):
    avec = A[:, k]
    q = avec
    for j in range(k):
        q = q - np.dot(avec, Q[:,j])*Q[:,j]
    
    Q[:, k] = q/la.norm(q)

print(Q)
print(qr(A))


