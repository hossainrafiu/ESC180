# Google Interview Question: Write a function that receives N strings in order, 
# and returns one of the strings uniformly at random after the Nth call.
# Cannot store more than a constant number of strings

# Sorting
# Given a list, mutate the list so that it's sorted in ascending order
# [5, 2, 10, 2] -> [2, 2, 5, 10]

# Selection Sort
# Find the (n-1)st largest element, put it in L[n-1] (put L[n-1] in the location
#                                   of the (n-1)st largest element location)
# Find the (n-2)largest element, put it in L[n-2] ...

def max_i_loc(L, end):
    cur_max = L[0]
    cur_max_loc = 0
    # Const 1 ^^
    for i in range(end+1):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_loc = i
        # Const 2 ^^
    return cur_max_loc

# Runtime: Const1 + (end * Const2)

def selection_sort(L):
    for i in range(len(L) - 1):
        max_loc = max_i_loc(L, len(L) - 1 - i)
        L[max_loc], L[len(L) - 1 - i] = L[len(L) - 1 - i], L[max_loc]
        
# Total Runtime:
# Const1 + Const2 * (len(L) - 1)
# Const1 + Const2 * (len(L) - 2)
# Const1 + Const2 * (len(L) - 3)
# ...
# Const1 + Const2 * (2)
# 2 + 3 + 4 + ... + (n-1)
# (n-1)(n-1+1)/2 - 1
# ...
# O(n^2)

# Bubble Sort

def bubble_sort(L):
    for i in range(len(L) - 1):
        swapped = False
        for j in range(len(L) - 1 - i):
            if L[j+1] < L[j]:
                L[j], L[j+1] = L[j+1], L[j]
                swapped = True
        if not swapped:
            break
    return L

print(bubble_sort([5,3,2,4,1]))
