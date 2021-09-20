def f(x):  # def is a keyword
    '''Return the square of the input x
    '''
    return x**2

help(f)

print(f(5))
print(f(5) + 12)

def pirate_print(s):
    '''Print the piratified version of s'''
    print("Ahoy! " + s + " Yarr!")

def pirate_transform(s):
    '''Return th piratified version of the string s'''
    return "Ahoy! " + s + " Yarr!"

a = pirate_transform("CIV")
print(a)

print(pirate_transform(pirate_transform("Calc")))

def has_Roots(a, b, c):
    '''Return True iff (if and only if) ax^2+bx+c has at least one real root'''
    disc = b**2 - 4*a*c
    # if disc >= 0:
    #     return True
    # else:
    #     return False
    return disc >= 0

print(has_Roots(1,2,1))

