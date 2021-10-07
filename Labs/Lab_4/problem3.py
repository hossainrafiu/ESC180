def lists_are_the_same(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

if __name__ == "__main__":
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 3, 4]
    L3 = [1, 2, 3, 4, 0]
    L4 = [4, 3, 2, 1]
    print(lists_are_the_same(L1, L2))
    print(lists_are_the_same(L1, L3))
    print(lists_are_the_same(L1, L4))