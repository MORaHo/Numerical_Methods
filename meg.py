import matrix

Matrix = matrix.Matrix

def meg(A:Matrix):

    for k in range(len(A)-1):
        largest_value = A[k][k]
        row = k
        
        for i in range(k,len(A)):
            if A[i][k] > largest_value:
                largest_value = A[i][k]
                row = i

        if row != k:
            temp = A[k]
            A[k]=A[row]
            A[row]=temp
       
        if A[k][k] == 0:
            continue

        A_kk = A[k][k]
        for j in range(k+1,len(A)):
            l_kj = A[j][k]/A_kk
            A[j] = [ A[j][w]-l_kj*A[k][w] if A[j][w]!=0 else A[j][w] for w in range(0,len(A[0]))]
            # the else in the last line of code amends the reduction of the list size that would otherwise occur for some reason

    return A

