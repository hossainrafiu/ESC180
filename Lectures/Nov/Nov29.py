"""


    \   /   \   /

    fib(n-1)  fib(n-2)

        \     /
         fib(n)


Calls(n) = 1 + Calls (n-1) + Calls (n-2) - fib(n)   O(phi^n)

"""

def fib(n, cache = {1:1, 2:1}):

    if n in cache:

        return cache[n]

    else:

        cache[n] = fib(n-1, cache) + fib(n-2, cache)

        return cache[n]

"""

Analysis

fib(n-1, cache) + fib(n-2, cache) is used O(n) times

Each call produces 2 calls (for)

   ...\  

       \         fib(n-3)

        \       /

        fib(n-1)       fib(n-2)

               \       /
                fib(n)


Approx 2*n calls, approximately n additions

In Total: O(n)
"""

###############################


def print_all(alphabet, n, start_str = ""):

    """ Print all strikgns over alphabet alphabet of length n,

    prepending start_str


    >>> print_all("abc", 2, "zz")
    zzaa
    zzab
    zzac
    zzba
    zzbb
    zzbc
    zzca
    zzcb
    zzcc
    """
    

    if n == 0:

        print(start_str)

        return
    

    for letter in alphabet:

        print_all(alphabet, n-1, start_str + letter)


#print_all("abc", 10)

def jls_extract_def():
    return """
    n: leng of the strng to print
    m: len(alphabet)
    
    abc 0 "aa" ...                       ...  abc 0 "cc"    m^2  (2 = n)
        \    |  /       \   |   /     \    |   /
        abc 1 "a"       abc 1 "b"     abc  1 "c"            m
                    \       |       /                       
                        abc 2 ""                            1
    
    (Num of layer)*(sum of Num of calls)

    m(1 + m + m^2 + .... + m^n) =  m ( ((m^n+1) + 1) / (m-1) )
    O(m^(n+1))
    """

def all_combinations(alphabet, n , start_str = ""):
    """Return al list of all the combinations of length n over the alphabet,
    with start_str, prepended.
    
    >>> all_combinations("abc", 2)
    set(["aa", "ab", "ac", ..., "cc"])
    """
    if n == 0:
        return set([start_str])
    
    res = []
    for letter in alphabet:
        res.extend(all_combinations(alphabet, n-1, start_str + letter))
    return set(res)

#########################

"""
L = [5, 6 ,7]
VVV
[[], [5], [6], [7], [5, 6], [5, 7], [6, 7], [5, 6, 7]]

For the list all subsets of [6, 7]      (all0)
append 5 to each of them
"""

def get_all_subsets(L):
    if len(L) == 0:
        return [[]]
    
    #all0: all the subsets of L that don't contain L[0]
    all0 = get_all_subsets(L[1:])
    res = []
    for subset in all0:
        res.append([L[0]] + subset)
    res.extend(all0)
    return res

print(get_all_subsets([7, 8, 9]))