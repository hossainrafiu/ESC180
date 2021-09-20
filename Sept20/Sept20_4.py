def artsie_math(arg1, arg2, op):
    '''Return arg1 op arg2, where arg 1 and arg 2 are numbers,
    and op is one of "+" or "-" (else print error message)
    '''
    if op=="+":
        return arg1 + arg2
    elif op=="-":
        return arg1 - arg2
    else:
        print("I am artsie, I don't know ops that are not + or -")
        # Returns None

def artsie_math2(arg1, arg2, op):
    '''Return arg1 op arg2, where arg 1 and arg 2 are numbers,
    and op is one of "+" or "-" (else print error message)
    '''
    if op != "+" and op != "-":
        return None

    if op=="+":
        return arg1 + arg2
    elif op=="-":
        return arg1 - arg2

if __name__ == "__main__":
    res = artsie_math2(4, 5, "*")
    if res != None:
        print(res)
    