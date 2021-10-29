"""
Matrix =[0 1 0 1 0]
        [0 0 0 0 5]
        [2 0 0 0 0]
Dict_Matrix = { (0,1): 1, (1,4): 5, (0, 3): 1, (2,0): 2}

What is:[0 1 0 1 0]     [1]     [0 + 1*2 + 1*4]
        [0 0 0 0 5]  x  [2] =   [0 + 5*5]
        [2 0 0 0 0]     [3]     [0 + 1*2]
                        [4]
                        [5]
"""

def mult_M_by_v(M, Mdim, v): # M is the dictionary of Matrix Entries
    res = [0]*Mdim[0]
    
    for cords, value in M.items():
        res[cords[0]] += value*v[cords[1]]
    
    return res

M = { (0,1): 1, (1,4): 5, (0, 3): 1, (2,0): 2}
Mdim = (3, 5)
v = [1, 2, 3, 4, 5]
res = mult_M_by_v(M, Mdim, v)
print(res)

#############################################

dict1 = {11: 1, 22: 2, 33: 3}
print(dict1)
del dict1[22]
print(dict1)
dict1.clear()
print(dict1)

def correct_transcript_bad(grades):
    #for course in grades: # Can't do this, can't change size of dict while iterating
    for course in list(grades.keys()):
        if grades[course] not in ["A+", "A"]:
            del grades[course]

def drop_everything(dict1): # doesn't work...
    dict1 = {} # changes what the local variable refers too, doesn't change dictionary outside variable

# file reading
f = open("C:\\Users\\hossa\\OneDrive - University of Toronto\\Courses\\ESC180\\Python Code\\Lectures\\Oct25\\text.txt", encoding="latin1")
s = f.read()

lines = s.split("\n")

def num_words(text):
    return len(text.split(" "))

def num_sentences(text):
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    return len(text.split("."))

print(num_words(s)/num_sentences(s))

print(s)