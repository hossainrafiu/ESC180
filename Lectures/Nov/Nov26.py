# 1 million Integers
# Bubblesort: a1*10^12
# Mergesort: a2*10^6 *log2(10^6) + a2(2*10^6 - 1)
# Countingsort: O(n+m)

# All possible Sort??? if L[i]>L[j] then i>j for future permutations ???
# n!
# n!/2 n!/2
# ....
#
# log2(n!) steps

###########

# NOTE!!!!!!!!!!!!!!!!!!!!
# Nothing is better than O(n) for sorting
# Merge sort is best (maybe???)
# Works for shorter and longer lists

def merge(L1, L2):
    i, j = 0, 0
    merged =[]
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L2[j])
            i+=1
        else:
            merged.append(L1[i])
            j+=1
    merged.append(L1[i:])
    merged.append(L2[j:])

    return merged

L = [1, 2, 10, 3, 4, 5, 2, 3]

def merge_sort(L):
    step = 2
    while step <= len(L)*2:
        
        for i in range(0, len(L), step):
            begin = i
            mid = i + step//2
            end = i + step
            L[begin:end] = merge(L[begin:mid], L[mid:end])
        step*=2
    return L

print(merge_sort(L))
