def print_matrix_dim(M):    # eg M = [[1,2,3], [4,5,6]]
    initial_num_row = len(M)
    initial_num_col = len(M[0])
    
    for row in range(initial_num_row):
        if len(M[row]) != initial_num_col:
            return "not a matrix"
    
    return str(initial_num_row) + "x" + str(initial_num_col)

def mult_M_v(M, v):     # eg. M = [[1,2,3], [4,5,6]], v = [7,8,9]
    if len(M[0]) != len(v):
        return None
    
    new_M = [0]*len(M)
    for i in range(len(new_M)):
        new_M[i] = 0
        for j in range(len(v)):
            new_M[i] += M[i][j]*v[j]

    return new_M

print(mult_M_v([[1,2,3],[4,5,6],[7,8,9]] , [2,1,3]))


def dot_product(M1, M2, row, col):
    sum = 0
    for i in range(len(M1[0])):
        sum += M1[row][i]*M2[i][col]
    return sum


def mul_M1_M2(M1,M2): # M1 = [[1,2],[3,4],[5,6]] * [[1,2,3], [4,5,6]]
    if len(M1[0]) != len(M2):
        return None
    
    new_M = [[0]*len(M2[0])]*len(M1)
    new_M = [[0 for i in range(len(M2[0]))] for j in range(len(M1))]
    for i in range(len(new_M)):
        for j in range(len(new_M[i])):
            new_M[i][j] = dot_product(M1,M2,i,j)
            

    return new_M

print(mul_M1_M2([[1,2],[3,4],[5,6]] , [[1,2,3], [4,5,6]] ))