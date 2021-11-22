def power2A(n):
    if n == 0:
        return 1
    return 2*power2A(n-1)
    #        log10(2^(n-1)) decical digits
    # *** Note: multiplication with integers take longer with larger numbers
    # *** Note: python can have integers of unlimited digits
    # *** Note: multiplication with floats take a constant number of time
    # Runtime: C1*(n-1) 

# n -> n-1 -> ... -> 0
# => n+1 calls 
# but...
# C1(n-1) -> C1*(n-2) -> ... -> C1 
# => C1(1+2+...+(n-1)) + (n+1)C2
# => C1(n(n-1))/2 + C2(n+1)
# O(n^2)

###################
# Something Faster???
# 2^n = (2^(n//2))^2 * (1 if n is even, 2 if n is odd)

def power2B(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    halfpower = power2B(n//2)
    if n/2 == 0:
        extra = 1
    extra = 2
    return halfpower*halfpower*extra

# n -> n/2 -> n/4 -> ... -> 1
# # of calls: log2(n)
# If * takes const time, runtime is O(log(n))
# Assume * takes time proportional to the # of digits,
# C1*n + C2 -> C1*n/2 + C2 -> ...
# C1(1+2+4+...+n/2 + n) + C2*log2(n)
# = C1(2n-1) + C2*log2(n)
# O(n)

#########################
# Fibunachi Number

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# Upper bound on the # of calls,
# pretend all branches are of length n
# # of calls: 1 + 2 + 4 + ... + 2^n = [2^(n+1)-1]/(2-1)
# O(2^n)
# 
# Lower bound on the # of calls, 
# pretend all branches are of length n/2
# # of calls: 1 + 2 + 4 + ... + 2^(n/2) = [2^(n/2+1)-1]/(2-1)
# O(2^[n/2]) =>
# O(sqrt(2)^n)
# 
# Calls(n) : The # of calls to fib to compute fib(n)
# Calls(n) = 1 + calls(n-1) + calls(n-2)
#          ~= C3*fib(n)
#           = C3(phi^n/sqrt(2))
# O(phi^n)
