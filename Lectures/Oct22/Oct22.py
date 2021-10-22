# Tuples
# Like lists, but immutable

t = (1, 2, 3, 4)
print(t[1])
print(t[1:])
# t[0] = 5

t = ([1 ,2], 5)
print(t[0])
t[0][1] = 5 # changing the list, not the tuple

t = ('a', 'b', 'c')
#unpacking of tuples
x, y, z = t
print(x, y, z)
x, y = y, z
print(x, y, z)

def f():
    return 42, 43

x, y = f()

################################################

# Dictionary: 'keys' something to another 'value'

fave_dict = {"Bob" : "candy" , "Rob" : "money" , "Tom" : "punches"}

endowment = {2012: 1518 , 2014: 1881, 2015: 2142 , 2021: 3150}

grades = {"MAT": 80, "CSC": 85, "CIV": 95}
print(grades.keys())
print(list(grades.values()))
print(grades.items())

for subj in grades:
    print(f"I got {grades[subj]} in {subj}")

for subj, grade in grades.items():
    print(f"I got {grade} in {subj}")

print("MAT" in grades)
print("MAT" in grades.keys())
print(80 in grades)
print(80 in grades.values())

grades["PRA"] = 95

inv_grades = {80 : ["MAT"], 85 : ["CSC"], 95 : ["CIV", "PRA"]}

def get_inv_grades(grades):
    res = {}
    for subj, grade in grades.items():
        if grade in res:
            res[grade].append(subj)
        else:
            res[grade] = [subj]
    return res

print(inv_grades)
print(get_inv_grades(grades))

L = [1,2,3]
print(L)
del L[0]
print(L)

dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
del dict1["a"]
print(dict1)

##################################################

# It can be very TRICKY when modifying a list while iterating over it

L = [1, 2, 4, 4, 5]
for i in range(len(L)):
    if L[i] == 4:
        # del L[i]  # bad, reduces size of L, out of range of for loop
        pass

i = 0
while i < len(L): # bad, skips over consecutive 4s
    if L[i] == 4:
        # del L[i]
        pass
    i += 1

i = 0
while i < len(L):
    while L[i] == 4:
        # del L[i]
        pass
    i += 1

# OR

i = 0
while i < len(L):
    if L[i] == 4:
        del L[i]
    else:
        i += 1

# TIP: Create a new list!

L_new = []
for e in L:
    if e != 4:
        L_new.append(e)
L[:] = L_new
