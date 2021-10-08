def list_to_str(lis):
    string = "["

    for i in range(len(lis)-1):
        string += str(lis[i]) + ", "

    string += str(lis[-1]) + "]"

    return string


print(list_to_str([1, 2, 3]))
