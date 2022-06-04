#! ------------ Input () function ----------
#! is being used for making the user input the specific Number they want it to be input.

#! Syntax:input(prompt)
#? Prompt: (optional) The string that is written to standard output(usually screen) without newline.
#? Return: String object
#
# Taking input from the user
string = input()
# output
print(string)

# Taking inpt from the user with the message
name = input('Enter your Name: ')
print('Hi',name)

# By default input() function takes the user's input in a string. So, to take the input in the form of int you need to use int() along with the input function
num = int(input('Enter a number: '))
add = num+1
print(add)

# Let's take float input along with the input function.
data = float(input('Enter a number in decimal: '))
addFloat = data + 1.36
print(addFloat)

# let's take a list and input along with the functions
li = list(input('Enter a number: '))
print(li)
# Enter a number: 12
# ['1', '2']

tuple = tuple(input("Enter a Name: "))
print(tuple)
#! ----------------- PRINT ----------------
#? The python print Function do the same thing as it say used to print the python object in python as standard output

#? Syntax: print(object(s),sep,end,file,flush)
#? Parameters:

#? Objects's - It can be any python object(s) like string, list, tuple, etc. But before printing all objects get converted into strings.

#? sep: It is an optional parameter used to define the separation among different objects to be printed. By default an empty string("") is used as a separator.

#? end: It is an optional parameter used to set the string that is to be printed at the end. The default value for this is set as line feed("\n").

#? file: It is an optional parameter used when writing on or over a file. By default,, it is set to produce standard output as part of sys.stdout.

#? flush: It is an optional boolean parameter to set either a flushed or buffered output. If set True, it takes flushed else it takes buffered. By default, it is set to False

#! Printing objects with a separator
list = [1,2,3]
tuple = (85,45,'Geeks')
string = 'DevilShadows'
print(list,tuple,string,sep=" ")

#! Specifying the string to be printed at the end!
list = [1,2,3]
tuple = (85,45,'Geeks')
string = 'DevilShadows'
print(list,tuple,string,end=" Welcome to end!!")

#! Printing and Reading contents of an external file
# Python open() function and then print its
# contents open and read the file
my_file = open("geeksforgeeks.txt", "r")

# print the contents of the file
print(my_file.read())
