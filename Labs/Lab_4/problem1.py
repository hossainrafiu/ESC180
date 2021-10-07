def sum_nums(L):
    s = 0
    for num in L:
        s += num

    return s

def count_evens(L):
    num_evens = 0
    
    for num in L:
        if num % 2 == 0:
            num_evens += 1
    
    return num_evens

if __name__ == "__main__":
    L1 = [1, 2, 3, 4, 5]
    print(sum_nums(L1))
    print(count_evens(L1))
    