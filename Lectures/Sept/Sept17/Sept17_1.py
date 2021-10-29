a = 5
b = a
b = 6

a1, a2 = 1, 2
#a1 = 1
#a2 = 2

a, b = b, a
# a = b
# b = a (which in now b) wouldn't work

temp = a # temp: old a, a: old a, b: old b
a = b    # temp: old a, a: old b, b: old b
b = temp # temp: old a, a: old b, b: old a

b = a + b
a = b - a
b = b - a