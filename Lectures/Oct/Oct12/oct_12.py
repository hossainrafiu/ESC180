L1 = [1, 2, 3]
L1_copy = L1[:] # [L1[0], L1[1], L1[2]] # shallow copy
print(L1)
print(L1_copy)
L1[1] = 5
print(L1)
print(L1_copy)

L2 = [[1, 2], 3]
L2_copy = L2[:]
L2[0][0] = 5

L1 = [[1, 2], [3, 4]]
L2 = [[L1[0][0], L1[0][1]], [L1[1][0], L1[1][1]]] # refering to the same memory values
L1[0][0] = 5

# deep copy for lists of lists of integers
L2 = []
for sublist in L1:
    L2.append(sublist[:])
L1[0][0] = 5 # will not affect L2[0][0]

L1 = [[[1]]]
for sublist in L1:
    L2.append(sublist[:])
L1[0][0][0] = 5 # will not affect L2[0][0][0]