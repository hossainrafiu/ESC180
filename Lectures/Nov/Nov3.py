#O(n^2)
# 
# k1 * n
# 
# Bucket Sort/ Counting Sort #

'''
Bucket Sort
[1,6, 100, 150, 200, 102]

1
6           102
100         150         200
[...100, 101...200, 200...300]


Counting Sort
[3,2,2,5,7,7,7]

     2 1   1   3
[0,1,2,3,4,5,6,7]
'''

def counting_sort(L):
    # n = len(L), m = max(L)
    max_int = max(L)            #O(n) = k1*n
    counts = [0]*(1 + max_int)  #O(m) = k2*m
    
    for e in L:
        counts[e] += 1          #O(n) = k3*n

    sorted_L = []
    for i in range(0, len(counts)):     # k4*m + k5*n
        sorted_L.extend([i]*counts[i])

# Total time: (k1 + k3 + k5)*n + (k2 + k4)*m
#               O(n+m)
# If we know that m is limited, then it's just O(n)

"""
Bozosort
"""
import random
L = [1, 10, 2, 2, 3, 2]

def is_sorted_nondecreasing(L):
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False
    return True

def bozosort(L):
    while not is_sorted_nondecreasing(L):
        i,j = int(len(L)*random.random()),int(len(L)*random.random())
        L[i], L[j] = L[j], L[i]
        print(L)

#####################

# complexity of arithmetic operations

# Arithmetic operations on floats take a cont. amount of time

# x + y

# x = jfka;sdfjklsd
# y = dsakf;jsdk

# jfka;sdfjklsd + dsakf;jsdk

# Addition is O(n) where n is the number of digits in the input
# the number N has apporx log(N) digits
# Addition is O(log(N)), where N = max(x,y)

#########################

# Multiplication

#   fjkdslfjdksl
#   skfldjsklfdk
#   ------------
#           kdls
#        fdsjkl
#       jfdksl
#   ...
#fjds

# n^2 multiplications, n^2 additions

# long multiplication is O(n^2) time where n is the number o fgingits 
# in the larger of x + y