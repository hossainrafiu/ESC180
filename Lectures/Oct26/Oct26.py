# Complexity Analysis

def find_i(L, e):
    """Return the index of the first appearance of e in L
    (and None if i is not in L"""

    #L.index(e)
    for i in range(len(L)): # 1 operation (a)
        if L[i] == e:       # 2 ops (b)
            return i        # 1 op (c)
    
    return None             # 1 op (d)

    # Overall number of operations
    # (a + b) * k + (c or d)
    # 3 * k + 1 , where k is the number of times the loop repeats
    # Worst-Case runtime complexity: 3*n + 1 operations, where n = len(L)

    # The runtime will be proportional to 3*n+1 seconds (in the worst case)
    # (The actual runtime will be a*(3*n + 1),where a is the number of ops per sec)
    # SAY: The worst runtime complexity is O(n) [order of n] (proportional to n)

    # In general,
    # 3n^3 - n is O(n^3)
    # 5n^7 + n^2 is O(n^7)

    #  f(n) is # of ops equation
    #  f(n) is O(g(n)) is lim sup(n->+infinity) [(f(n)/g(n)] <= C {a constant}
    #       g(n) grows at least as fast as f(n)
    #       3n + 1 is O(n) {also O(n^2 x log(n))}
    #                   ^- "tight asymtotic bound on 3n+1"
    #       5n^2 - n is O(n^2)
    # lim (n -> +infinity) [sup tn] = lim (n -> +infinity) [sup(k>=n) tk]
    # Note: sup = max...

# L is sorted
# [1, 5, 100, 102, 105, 200, 250, 500, 520, 600]
# want to find idex of 520

# binary search
def find_i_binary(L, e):
    # Current consider L[low: (high-1)]
    low = 0
    high = len(L) - 1
    while high - low >= 2: # while the size of list is at least 3
        mid = (low + high) // 2
        if L[mid] == e:
            return mid
        elif L[mid] > e:
            high = mid
        else:
            low = mid

    if L[low] == e:
        return low
    elif L[high] == e:
        return high
    
    return None

