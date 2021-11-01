def longest_run1(s, c):
    run = 0
    max_run = 0

    if c == "z":
        s += "y"
    else:
        s += "z"

    for ch in s:
        if ch != c:
            max_run = max(max_run, run)
            run = 0
        else:
            run += 1

    return max_run

# Runtime:  const1 + len(s) * const2 ( O(len(s)) )
#           O(n) , n = len(s)

def longest_run2(s, ch):
    # Runs at most len(s)+1 times
    for longest in range(len(s), -1, -1): 
        cur_run = 0
        # Runs at most len(s) times
        for i in range(len(s)): 
            # Const time
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0
                
            if cur_run == longest:
                return longest
    return 0

# Total runtime: at most (n+1)*n*const times
#                         const*n^2 + const*n
#                         O(n^2) -> ignore constants and lower orders

# Sending functions to arguments

def f1(x):
    return x*2

def f2(x):
    return x*3

def apply(f, x):
    return f(x)

def timeit(f, x):
    N = 500000
    import time
    t0 = time.time()
    for i in range(N):
        f(x)
    t1 = time.time()
    return (t1-t0)/N

print(timeit(f1, 5))
