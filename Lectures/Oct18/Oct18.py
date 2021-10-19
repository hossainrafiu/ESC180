# str.lower()
# str.replace(s1, s2)

# "praxis forever" , "a prefix rovers"
# is_anagram

def is_anagram(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == \
    sorted(s2.lower().replace(" ", ""))
    
num = 180
name = "ESC"

print(name + str(num))

course = "%s %d" % (name ,num)

print(course)

course = "{}{}".format(name,num)

print(course)

course = f"{name}{num}"

print(course)

s = "x = 2"
exec(s)
print(x)

s = "def f(): \n    return 42"
exec(s)
print(f())

# print all strings of length n over the alphabet

def gen_nested_loop(n):
    """Generate a nested for loop thhat prints all strings of
    length n over alphabet"""

    res = "def gen_passwords(alphabet):\n"
    for i in range(n):
        res += " " * (i + 1)
        res += f"for letter{i} in alphabet: \n"
    res += " " * (n + 1)
    res += "print("
    for i in range(n-1):
        res += f"letter{i} + "
    res += f"letter{n-1})\n"

    return res

    """
    for letter0 in alphabet:
        for letter 1 in alphabet:
            '''
            '''
            '''
                print(letter0 + letter 1 + ...)
    """

alphabet = "abcd"
code = gen_nested_loop(4)
exec(code)
gen_passwords(alphabet)

def longest_run(s,c):
    """Return the length of the longest fun of the character c in the string s
    >>> longest_run("abbdbbbef", "b")
    3
    >>> longest_run("abbdbbbef", "e")
    1
    """

    # for i in range(len(s), 0, -1):
    #     if c*i in s:
    #         return i
    # return 0

    # State Variables: 
    # run: the length of the current run
    # max_run: the length of the longest run

    run = 0
    max_run = 0

    for char in s:
        if char != c:
            run = 0
        else:
            run += 1
            max_run = max(run, max_run)
    
    return max_run

def n_as_plus_b(s, n):
    """Return True iff s contains a substring of exactly n "a"s followed by 
    exactly one b
    
    >>> n_as_plus_b("zaaabc",3)
    True
    >>> n_as_plus_b("zaaaabc",3)
    False
    >>> n_as_plus_b("zaaabbc",3)
    False
    """

    cur_run_a = 0
    for i in range(len(s)):
        if s[i] == "a":
            cur_run_a += 1
        elif s[i] == "b":
            if cur_run_a == n:
                if i == len(s) - 1: #end of str
                    return True
                if s[i+1] != "b": #no extra 'b'
                    return True
            cur_run_a = 0
        else:
            cur_run_a = 0
    return False