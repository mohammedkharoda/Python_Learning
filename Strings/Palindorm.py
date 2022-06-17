#! ------------------------- Approach - 1 (Number) ---------------------
#? Taking the Number to check the palindorm string
n = int(input('Enter the Number: '))

#? Making a copy of the input number
temp = n

#? Declaring the Value to store the reversal of the input number
reverse = 0

#? Reversing the number using the while loop
while(n>0):
    digit = n%10
    reverse = reverse*10+digit
    n = n//10

if(temp==reverse):
    print('It is palindorm')
else:
    print('not a palindorm')

#!---------------------------- Approach-2 (Strings & Numbers) ---------------------------

def check_Palindorm(s):
    # Convert all the letter to Lower
    s = s.lower()
    if len(s)<=1:
        print('Enter a word not a alphabet!')
        return True
    # Recurrsion
    # If same than we are removing it from the both end
    if (s[0] == s[len(s)-1]):
        # Slicing form the index 1 to the length of last index
        s[1:len(s)-1]
        print('Is Palindorm')
    else:
        print('Not a Palindorm')
        return False

data = input('Enter the word: ')
check_Palindorm(data)