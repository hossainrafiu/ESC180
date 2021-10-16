def match_pattern(list1, list2):
    diff_in_lists = len(list1)-len(list2)
    
    if diff_in_lists < 0:
        return False
    
    for i in range(diff_in_lists):
        same = True
        for j in range(len(list2)):
            if list1[j+i] != list2[j]:
                same = False
                break
        if same:
            return True
    return False

if __name__ == "__main__":
    print(match_pattern([1,2,3,4,5] , [6]))