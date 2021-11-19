def sum_list2(L):
    if len(L) == 0:
        return 0
    # Without the following, we would get infinite recurssion
    if len(L) == 1:
        return L[0]
    mid = len(L)//2
    # ^^^ C2
    return sum_list2(L[mid:]) + sum_list2(L[:mid])
    #                   ^---- C1*len(L) ------^


    
###
# 1 [n]
# 2 [n/2] [n/2]
# 4 [n/4] [n/4] [n/4] [n/4] 
# ......
# 2^k = n[1] [1] ................ [1]
# k = log2(n)
# 
# # of calls: 1 + 2 + 4 + ... + 2^(log2(n))
#               = 2^(log2(n)+1)-1 / (2-1) = 2*2^(log2(n)) - 1 = 2n - 1
# 
### But copying lists take time...
# C2 + C1*n [n]
# 2C2 + C1*(n/2 + n/2) [n/2] [n/2]
# 4C2 + C1*(n) [n/4] [n/4] [n/4] [n/4] 
# ......
# nC2 + C1*(n) = n[1] [1] ................ [1]
# k = log2(n)
# 
# # of calls: C2(1 + 2 + 4 + ... + 2^[log2(n)]) + C1n[log2(n)+1]
#               = C2(2n-1) + C1n[log2(n)+1]
#               ~ nlog2(n)
# O(nlogn)

def fact_while(n):
    i = 1
    cur_prod = 1
    while i != n+1:
        cur_prod *= i
        i += 1
    return cur_prod

def fact_inter(n, cur_prod, i):
    if i == n+1:
        return cur_prod
    return fact_inter(n, cur_prod, i+1)

# default Argument:
def fact_inter(n, cur_prod = 1, i = 1):
    if i == n+1:
        return cur_prod
    return fact_inter(n, cur_prod, i+1)

def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)