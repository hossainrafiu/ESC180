import math

a = 1
b = 2
c = 5

disc = b**2 - 4*a*c

if disc > 0:
    r1 = (-b - math.sqrt(disc))/(2*a)
    r2 = (-b + math.sqrt(disc))/(2*a)
elif disc == 0:
    r = 0

