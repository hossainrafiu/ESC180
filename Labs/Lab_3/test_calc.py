import lab02
if __name__ == '__main__':
    lab02.initialize()
    lab02.add(42)
    if lab02.get_current_value() == 42:
        print("Test 1 passed")
    else:
        print("Test 1 failed")
    
    lab02.subtract(50)
    if lab02.get_current_value() == -8:
        print("Test 2 passed")
    else:
        print("Test 2 failed")
        
    lab02.multiply(3)
    if lab02.get_current_value() == -24:
        print("Test 3 passed")
    else:
        print("Test 3 failed")
    
    lab02.divide(-4)
    if lab02.get_current_value() == 6:
        print("Test 4 passed")
    else:
        print("Test 4 failed")
    
    lab02.divide(0)
    if lab02.get_current_value() == "Error":
        print("Test 5 passed")
    else:
        print("Test 5 failed")
    
    lab02.add(90)
    if lab02.get_current_value() == "Error":
        print("Test 6 passed")
    else:
        print("Test 6 failed")
    
    lab02.initialize()
    lab02.subtract(-42)
    if lab02.get_current_value() == 42:
        print("Test 7 passed")
    else:
        print("Test 7 failed")
    
    import math
    lab02.divide(math.pi)
    if lab02.get_current_value() == 13.36901521971921:
        print("Test 8 passed")
    else:
        print("Test 8 failed")

    