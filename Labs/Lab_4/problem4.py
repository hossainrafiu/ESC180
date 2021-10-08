def simplify_fraction(n, m):
    for i in range(n, 1, -1):
        print("simple")
        if n % i == 0 and m % i == 0:
            print(f"{n // i}/{m // i}")
            return
