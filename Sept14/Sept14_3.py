def f(x):
    x = 100
    return x**2 # x is a local variable

def plunder_grade():
    grade = 79

def actually_plunder_grade():
    global grade
    grade = 79

if __name__ == '__main__':
    res = f(5) # res is a global variable
    x = 15 # this x is a global variable
    print(res)
    print(x)

    grade = 97
    plunder_grade()
    print(grade)
    actually_plunder_grade
    print(grade)
    
