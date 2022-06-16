# ------------------------- Pattern Searching ----------------

# we will use the find method to complete this achievement

txt = input('Enter the Sentence: ')
pat = input('Enter the Pattern: ')

pos = txt.find(pat)
# print(pos) #? --> Just for the One Occurance

#? --> For getting ever occurance in the loop
while pos >=0:
    print(pos)
    pos = txt.find(pat,pos+1)

