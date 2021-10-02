def cube_sum(n):
    total = 0

    for i in range(1, n+1):
        total += i ** 3
    
    return total

def cool_cube_sum(n):
    return n**2*(n+1)**2 / 4

def check_sum(n):
    return cube_sum(n) == cool_cube_sum(n)

def check_sums_up_to_n(N):
    for i in range(1, N+1):
        if not check_sum(i):
            return False
    
    return True
