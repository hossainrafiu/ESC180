from problem4 import simplify_fraction
import time


def gcd(a, b):
    print("euclid")
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def euclid_simplify_fraction(n, m):
    g = gcd(n, m)
    print(f"{n // g}/{m // g}")


def test1():
    simplify_fraction(3, 6)
    print()
    euclid_simplify_fraction(3, 6)
    print()
    simplify_fraction(8, 4)
    print()
    euclid_simplify_fraction(8, 4)
    print()
    simplify_fraction(48, 120)
    print()
    euclid_simplify_fraction(48, 120)


def test2():
    t0 = time.time()
    simplify_fraction(48, 120)
    t1 = time.time()
    print("time for simple version:", t1 - t0)

    t2 = time.time()
    euclid_simplify_fraction(48, 120)
    t3 = time.time()
    print("time for euclidean version:", t3 - t2)


if __name__ == '__main__':
    test1()
    test2()
