# #! ------------------------ Update of String -------------
String1 = 'geeksForgeeks'
print('Intial String: ')
print(String1)

String1 = 'Geek is Here'
print('Update String: ')
print(String1)

# # ! --------------------- Deletion of string -------------
del String1[2] #? -> Throw errors
del String1
print('Deleted String')
print(String1) #! => Will throw an Error

#! ------------------------ Formatting of String ----------
#? Method---1 (Using the "%" operation old schl)
name = 'Yash'
age=21
wt=70.42
s='Welcome to %s , Your age is %s and your weight is %s'%(name,age,wt)
print(s)

#? Method---2 (Using the "format" keyword)
name = "Mills"
course = "Python Course"
s = "welcome {0} to {1}".format(name,course)
print(s)

#? Method---3 (Using the F keyword)
name = 'jeff'
course="Python course"
s = F'Welcome to the {course} Mr {name}'
print(s)

#* Feature of the String in the F
a = 20
b = 10
s = F'Going to add {a} and {b} = {a+b}'
print(s)
s = F'Going to multiply the {a} and {b} = {a*b}'
print(s)

#* Using the Functions -> We can also use the function the F string
a=10
b=20
print(f"max of {a} and {b} is {max(a,b)}")