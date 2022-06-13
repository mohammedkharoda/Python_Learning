# !-------------------------- BASIC FUNCTION SYNTAX ------------------
def functionCall():
    print('Working With Function')

print('Before calling Function: ')
functionCall()
print('Funtion is being called: ')

#! ------------------------------ global vs local scope ---------------
def price(amount,discount,tax):
    final = amount-discount+tax
    return final # --> Global scope due to return statement
    #  print(final) # --> Local scope due to it will print the result statement direct

totalValue = price(500,20,250)
print(totalValue)

# !----------------------------------- Argument Type ---------------------
def studentName(firstName,lastName):
    print(firstName,lastName)
# this is called as the keyword args
studentName(firstName="Jeremy",lastName="Hanks")


def myFixed(x,y=85):
    print('x',x)
    print('y',y)


myFixed(74) #-> Default params
myFixed(63,74) # -> Overwriting default params

#! ------------------------------- Pass by value or Pass by refernce ------------------------
def passRef(x):
    x[0] = 20

lst = [19,30,88,96,78]
passRef(lst)
print(lst)  # ==> Change happen after the change on the function parameters.

#? reference link is broken if we assign a new value (inside the function)
def function(x):
    x=20

x=10
function(x)
print(x)

#! -------------------------------------- Anonymus Funtions ----------------------------------
def cube(x):
    return x*x**x

cubeV2 = lambda x : x**x*x

print(cube(7))
print(cubeV2(7))
















#! ---------------------------------- Misc problem -----------------------
# def vowelCount(s):
#     vowel = 'aeiouAEIOU'
#     vc=0
#     for charc in s:
#         if(charc in vowel):
#             vc = vc+1
#     return vc
#
# print(vowelCount('Working on the goals'))


