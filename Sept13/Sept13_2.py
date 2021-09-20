#f(x) = x^2

def f(x):
    return x*x

def my_add(a, b):
    res = a + f(b)
    print("hi", res)
    return res

print(my_add(5, 2) * 10)
