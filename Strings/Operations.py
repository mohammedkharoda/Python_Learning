#! --------------------------- Operations( part - 1 ) ---------------------

#! ==> Checking For Substring
s1 = 'geek'
s2 = 'ee'
print(s1 in s2)

#! ==> Checking for not substring
s1 = 'geek'
s2 = 'ae'
print(s2 not in s1)

#! ==> Concatination
s1 = 'geek'
s2 = 'for'
s3 = s1+s2
print(s3)

#! ==> Index of String (Position of first ocurrance)
s1 = 'geekforgeeks'
s2 = 'geek'
s3 = s1.index(s2)
print(s3)

#! ==> Rindex of (Position of the last ocurrance)
s1 = 'geekforgeek'
s2 = 'geek'
s3 = s1.rindex(s2)
print(s3)

#! ==> Length property
s1 = 'geeksForgeeks'
s2 = len(s1)
print(s2)

#! ==> Upper()
s1 = 'geeksforgeeks'
s2 = s1.upper()
print(s2)

#! ==> Lower()
s1 = 'GEEKSFORGEEKS'
s2 = s1.lower()
print(s2)

#! ==> isLower()
s1 = "geekforgeeks"
s2 = s1.islower()
print(s2)

#! ==> isUpper()
s1 = 'GEEKSFORGEEKS'
s2 = s1.isupper()
print(s2)

#! ==> startwith()
s1 = 'geeksforgeeks'
s2 = s1.startswith('geek',8,12)
print(s2) # -> True

#! ==> endsWith()
s1 = 'geeksforgeeks'
s2 = s1.endswith('for',8,13)
print(s2) # -> False

#! ==> Split
s1 = 'geeks or peaks,beats'
s2 = s1.split()
print(s2)
s3 = s1.split(",")
print(s3)
#? ['geeks', 'or', 'peaks,beats']
#? ['geeks or peaks', 'beats']
#! ==> join
s1 = ["geeks", "for" ,"geeks"]
s2 = "*".join(s1)
print(s2)
#? Don't input int in the array or else error
#! ==> strip
s1 = '__geeksforpeaks__'
s2 = s1.strip('__')
print(s2)
#? Strip from the left and right the given parameter
#! ==> find
s1 = 'peak in meats'
s2 = s1.find('meats')
print(s2)
#? Same as index method  but if not found in the string it will return (-1) but the index will return error




