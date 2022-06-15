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

#!--------------------------------------- keywords and non-keywords ----------------------------
def myFun(*args):
    for arg in args:
        print(arg)
myFun('Hello','Welcome','to')

def myFun(**kwargs):
    for key,value in kwargs.items():
        print('The value of the input is: ',key,value)
myFun(first='Working',second="with",last="kwargs")

# ? ----------------------------- *ARGS vs **ARG (CALLBACK) ------------------------
def callBack(args1,args2,args3):
    print('args1', args1)
    print('arg2', args2)
    print('arg3',args3)

args = ('working' , 'in' , 'dark')
callBack(*args)

args2  = {'args1':'Darkness','args2':"shallness","args3":"Threates"}
callBack(**args2)
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


# ! --------------------------------------- Returns Multiple ---------------------
def fun():
    str='geeksForgeeks'
    x = 20
    return str,x; # Return tuple

firstValue,secondValue = fun() #tuple unpacked here so we need to store in different variable
print(firstValue)
print(secondValue)

#!-------------------------------------- SEIVE OF ERATHOSTHENSE ------------------------
def sieveOfErathosthense(n):
    n
    prime=[] # an empty list
    for i in range(n+1):
        #Append all the number one by one from 2
        prime.append(i)

    prime[0]=0
    prime[1]=0

    p=2
    while(p*p<=n):
        # If prime[p] is not changed , then it is a prime
        if(p!=0):
            #Update all multiple of p to zero
            for i in range(p*2,n+1,p):
                prime[i]=0

        p = p+1

    print('All the number up to',n,'are:')
    for i in range(len(prime)):
        if(prime[i]!=0):
            print(prime[i])


number = int(input('Enter the number until you want to find the range: '))
sieveOfErathosthense(number)
