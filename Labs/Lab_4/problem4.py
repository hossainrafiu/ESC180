def simplify_fraction(n, m):
    for i in range(n, 1, -1):
        if n % i == 0 and m % i == 0:
            print(n,"/",m, sep="")
            print(f"simple: {n // i}/{m // i}")
            return

if __name__ == "__main__":
    simplify_fraction(3,6)
    simplify_fraction(36,60)
    simplify_fraction(7362,1842)