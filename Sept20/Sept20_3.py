def has_roots(a, b, c):
    '''Return True iff ax^2+bx+c has at least one real root
    '''
    return b**2-4*a*c >= 0

def has_no_roots(a, b, c):
    '''Return True iff ax^2+bx+c has at least one real root
    '''
    return b**2-4*a*c < 0

def has_no_roots2(a, b, c):
    return not has_roots(a, b, c)

if __name__ == "__main__":
    print(has_no_roots2(1, 2, 3))