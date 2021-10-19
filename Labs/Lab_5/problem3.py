def repeats(list0):
    previous_element = None
    for element in list0:
        if element == previous_element:
            return True
        else:
            previous_element = element
    return False

print(repeats([1,1]))