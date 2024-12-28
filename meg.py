import matrix
from utils import copy
Matrix = matrix.Matrix

def meg(A:Matrix):
    
    M = copy(A)
    for k in range(len(M)-1):
        
        largest_value = M[k][k]
        row = k 
        for i in range(k,len(M)):
            if abs(M[i][k]) > abs(largest_value):
                largest_value = M[i][k]
                row = i

        if row != k: #pivoting
            temp = M[k]
            M[k]=M[row]
            M[row]=temp
       
        if M[k][k] == 0:
            continue

        A_kk = M[k][k]
        for j in range(k+1,len(M)):

            l_kj = M[j][k]/A_kk
            M[j] = [ M[j][c]-l_kj*M[k][c] for c in range(0,len(M[0]))]
            # the else in the last line of code amends the reduction of the list size that would otherwise occur for some reason

    return M


