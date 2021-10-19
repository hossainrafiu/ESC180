def list1_starts_with_list2(list1, list2):
    if len(list2) <= len(list1):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
        return True
    else:
        return False

print(list1_starts_with_list2([1,2,3,4,5], [1,2,3]))