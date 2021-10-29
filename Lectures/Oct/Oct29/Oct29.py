L = [5,6,7,1,8,7,6]

L[1:4:1] # [6, 7, 1]
L[5:] # [7, 6]
L[5::-2] # [7, 1, 6]

L[::-1] # reverse
L[:] # copy

############################

L[[1, 2], [3, 4]]

L1 = L[:] # L1 = [L[0], L[1]] -> lists are referred to in booth L and L1
# any changes to inner lists will be noticed in both outer lists
L1 = []

# deep copy
for sublist in L:
    L1.append(sublist[:])

############################

# binary search
def find_i_binary(L, e):
    # Current consider L[low: (high-1)]
    low = 0 # 1
    high = len(L) - 1 # 3
    while high - low >= 2: # 3
        mid = (low + high) // 2 # 3
        if L[mid] == e: # 3
            return mid # 2
        elif L[mid] > e: # 3
            high = mid # 2
        else:
            low = mid # 1

    if L[low] == e: # 3
        return low # 1
    elif L[high] == e: # 3
        return high # 1
    
    return None # 1

    ## Total Num of Ops (from lecture): 4 + 7 + 11k
    ## What is k in the worst case? -> e not in L
    ## High-low = n-1 -> n-1/2 -> n-1/2/2
    ## n-1 .= 2^k
    ## log2(n-1) .= k
    ## Worst Case 11 + 11*log2(n) = 11 + 11*log2(n)*(log2/log2)
    ## = 11 + 11*log(n)/log(2) = 11 + (11/log(2))*log(n)
    ## Proportional to just log(n)
    
    ## THEREFORE: O ( log(n) )