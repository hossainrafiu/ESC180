# Scholar:
#   University: 50 eat: 10 homework: 20 (50, 10, 20)
# Dog:
#   University: 2  eat: 70 homework: 10 (2, 70 10)
# 
# angle theta between v1 and v2:
#   cos(theta) = (v1 dot v2)/(||v1|| ||v2||)
# dict.get(key, default)
# dict.update(new_key:new_item, delete_key:delete_item)
# 
# Sets - list with only unique elements
#  

obj = [[1,2], [[5,6], 2], [1, [5,6]]]

def deep_copy(obj):
    """ Return a deep copy of obj
    obj is a list of nested lists what contain an int/ ints
    """
    if type(obj) == int:
        return obj
    copy = []
    for elem in obj:
        copy.append(deep_copy(elem))

    return copy

# # of calls: the # of distinct objects in obj
# # of copies of ints: the # of ints in obj
# Overall Complexity: O([# of distinct objects] + [# of distinct ints])

############################

# Merge Sort:
# [5, 2, 3, 10, 2, 5]
# Sort 2 seperate lists:
# [2, 3, 5] [2, 5, 10]
# Merge:
# [2, 2, 3, 5, 5, 10]


# count the total number of append operations
# each append operation costs c1 time
# Total runtime: c1 * (len(L1) + len(L2))
def merge(L1, L2):
    """ Return the sorted version of L1 + L2.
    Assume that L1 and L2 are sorted in non-decreasing order
    """

    merged = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merge.append(L1[i])
            i += 1
        else:
            merge.append(L2[j])
            j += 1
    
    merged.extend(L1[i:])
    merged.extend(L2[j:])

#  
def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    mid = len(L) // 2
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))
    #       ^- C1*(len(L)) + C2*(len(L))
# [n]
# [n/2] [n/2]
# [n/4] [n/4] [n/4] [n/4] 
# ...
# [1] [1] ...
# 
# C3 + (C1 + C2)*n
# 2C3 + (C1 + C2)*n /2 *2
# nC3 + (C1 + C2)*n 
# 
# Total Runtime: Log2(n) levels
# (log2(n))(C1 + C2)n + (1+2+4+..+n)C3
# (log2(n))(C1 + C2)n + (2^0 + 2^1 + ... + 2^log2(n))C3
# (log2(n))(C1 + C2)n + ((2^log2(n)-1)/(2-1))C3
# (log2(n))(C1 + C2)n + (22^log2(n) - 1)C3
# (log2(n))(C1 + C2)n + (2n - 1)C3
# 
# O(nlogn) 