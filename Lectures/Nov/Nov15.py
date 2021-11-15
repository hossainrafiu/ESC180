# Note: Any variable assigned inside a function is local
# unless explicitly declared as global.
#  ##

# Want to know how efficient the function f is
# For an input of size n, in the worst case, what is the runtime
# of f proportional to, for large n
# ##

def f(L):
    # Const1
    if L[0] == 5:
        return

    # Const2*len(L)*(len(L)//2)
    for i in range(len(L)):
        for j in range(len(L)//2):
            # Const2
            print("hi")

# Runtime: Const1 + Const2*len(L)*(len(L)//2)
#           const1 + (const2/2)*n^2 (n = len(L))
# O(n^2)

###########################

# Pythagorean Triple:
# (i, j, k) s.t. i^2 + j^2 = k^2
#
# Want to find a triple s.t. i^p + j^p = k^p, for some p

def fermat(p):
    n = 1
    while True:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    if i**p + j**p == k**p:
                        return i, j, k
        n += 1

# Fermat's Last Theorem:
# i^p + j^p = k^p has no integer solutions for p>=3
# LOLOLOL

#######################

# Recursion: Functions that call themselves
# n! = 1*2*...*n 
# (0! = 1)
# n! = {(n-1)! * n , n>=2}
#      { 1         , n<=1}

def fact(n):
    """Return n!"""
    # Base Case
    if n <= 1:
        return 1
    # Recursive Step
    else:
        return fact(n-1)*n

def is_winning_sum(s):
    # base case
    if s == 21:
        return True
    Moves=[1,2]
    for move in Moves:
        if is_winning_sum(s + move):
            return False
    return True

for i in range(1,22):
    print(i,is_winning_sum(i))