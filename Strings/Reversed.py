#! ------------------------- Using Extended Slice Syntax ---------------------

#* We will put starting and ending as empty to access the whole length of the string and step as -1 to access the string in reverse order. Hence, we will get the whole string in reversed order. In this process, reversed version of given string is created and is assigned to our original string.

def reverse(s):
    s=s[::-1]
    return s
s = 'Mohammed'
print(reverse(s))

#! -------------------------- LOOP ---------------------------

def reverse(s):
    string=""
    for i in range(len(s)-1,-1,-1):
        string = string + s[i]
    return string

s='mohammed'
print(reverse(s))

#! -------------------------- Recurrsion ---------------------------

def reverse(s):
    if (len(s) == 0):
        return s
    else:
        return s[-1]+reverse(s[:-1])

s="Mohammed"
print(reverse(s))

