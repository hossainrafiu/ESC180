# swapping values without using temp or multiple assignments
a = 1
b = 2

a = a + b
b = a - b
a = a - b

# boolean values
a = True
b = False

a = (5 > 4)

# boolean operators
not (1 > 2)

(5 == 5) and (3 > 2)
(5 == 5) and (2 > 3)

(1 == 2) or (2 == 2)
(1 == 2) or (2 == 3)

# xor
pie = True
ice_cream = False

if (pie or ice_cream) and not (pie and ice_cream):
    print("xor")

if (pie != ice_cream):
    print("xor")

if pie ^ ice_cream:
    print("xor")

# order of operations: not, and, or
# True <=> 1, False <=> 0
# A and B is kind of like A*B
# A or B is kind of like A+B