# Recurssion
# 
# 
# 

def print_list(L):
    print(L[0])
    if len(L) == 1:
        return
    print_list(L[1:])

    # Total # of calls: n = len(n)
    # 
    # Runtime: 
    # [3]           k1(n-3) + k2
    # [3, 4]        k1(n-2) + k2
    # [3, 4, 6]     k1(n-1) + k2
    # 
    # Total Runtime:
    # n*k2 + k1(1 + 2 + ... + n-1)
    # n*k2 + k1( (n-1)( (n-1)+1 )/2 )
    # (k2-k1/2)*n + k1*n^2-k1/2
    # 
    # Therefore:
    # O(n^2)
    # 
    # Since each call requires a new list to be made, the duration of each
    # call varies by directly with n  

def print_list_reverse(L):
    # L = L[-1::-1]
    # print_list(L)
    if len(L) == 1:
        print(L[0])
        return
    print_list_reverse(L)
    print(L[0])
    
def sum_list(L):
    if len(L) == 0:
        return 0
    return L[0] + sum_list(L[1:])

def sum_list2(L):
    if len(L) == 0:
        return 0
    # Without the following, we would get infinite recurssion
    if len(L) == 1:
        return L[0]
    mid = len(L)//2
    return sum_list2(L[mid:]) + sum_list2(L[:mid])

    # Total num of calls:
    # 2^0 + 2^1 + ... + 2^(log2(n))
    # = (1 - 2^(log2(n))+1)/(1-2)
    # = 2n - 1

def print_list2(L, start, end):
    if start == end:
        print(L[start])
        return
    print(L[start])
    print_list2(L, start + 1, end)

# Runtime: O(n) , n = len(L)
#
# Better than print_list(L) since we aren't making a new list each call
# so each call takes the same amount of time 

def print_list3(L):
    print_list2(L, 0, len(L))
    