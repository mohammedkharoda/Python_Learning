# Additional Operators
value1 = 2
value2 = 3
res = value1+value2
print('Addition result: ',res)

# Subtraction Operations
val1 = 2
val2 = 3
res = val1 + val2
print('subtraction: ',res)

# Multiplication
val1 = 5
val2 = 6
resM = val1*val2
print(resM)

# Division Operator
val1 = 10;
val2 = 25;
res = val1 + val2
print(res)

# Modulus Operator
val1 = 3
val2 = 4
res=val1%val2
print(res)

# Exponention Operator
val1 = 10
val2 = 20
res = val1 ** val2
print(res)

# Floor Division
val1 = 25
val2 = 96
res = val1 // val2
print(res)

#
#! Operator	Description	Syntax
#? (+)	Addition: adds two operands	x + y
#? (-)	Subtraction: subtracts two operands	x - y
#? (*)	Multiplication: multiplies two operands	x * y
#? (/)	Division (float): divides the first operand by the second	x / y
#? (//)	Division (floor): divides the first operand by the second	x // y
#? (%)	Modulus: returns the remainder when first operand is divided by the second	x % y
#? (**)	Power : Returns first raised to power second	x ** y

#! =================== Logical Operator =====================
#* AND Operator : True if the operands are true x & y
#* OR Operator : False if the operands are false x & y
#* not Operator : True if Operands is false

#! ------------- AND OPERATOR ----------------
#? Logical operator returns True if both the operands are True else it returns False.
#? Note: If the first expression evaluated to be false while using and operator, then the further expressions are not evaluated.

a = 10
b = 10
c = -10

if(a>0 and b>0):
    print('The Number are greater than 0')

if (a>0 and b>0 and c>0):
    print('The number are greater than 0')

else:
    print('Atleast oe number is not greater than 0')

#! ------- Logical OR Operator ---------
a = 10
b = -10
c = 0
if a>0 or b>0:
    print('Either of the number is greater than 0')
else:
    print('No number is greater than 0')

if(b>0 or c>0):
    print('Eithe of the number is greater than 0')
else:
    print('No number is greater than 0')

#! ------- Logical NOT Oprator ----------
a = 10
if not a:
    print('Boolean value a is true')

if not (a%3==0 or a%5 ==0):
    print('10 is not divisible by either 3 or 5 ')
else:
    print('10 is divisible by either 3 or 5')

#! =================== Identity Operator =====================
#* is Operator : check if the id of both the operator are equal or not
x = 10
y = 10
print('The is operator',x is y)

x = [10,20,30,40]
y = [10,20,30,40]
print('The is operator in the list assignment: ',x is y)

#? (Thought here in the list both the list are being same but the problem occur due to they both have different ids and they will have different id's as they are being placed into different format in memeory)

#* is not Operator : True if Operands is false
x = 'geeks'
y = 'geeks'
print('The is not operator',x is not y)

#! =============== Membership Operator ===================
# ? It is used to validation of the value and test that the memeber is present in the sequence or not. Evaulation to true if it find it and to false if it not able to find it.

#! ----- In Operator ---------------
# * in operator: The ‘in’ operator is used to check if a value exists in a sequence or not. Evaluate to true if it finds a variable in the specified sequence and false otherwise.

list1 = [1,1,3,5,8,9,74]
list2 = [8,75,6,83,2,10]
for item in list2:
    if(item in list1):
        print('Overlaping: ', item)
    else:
        print('Not Overlaping: ',item)

#* 'not in' operator- Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

x = 20
y = 35
list = [10,25,35,45,20]
if(x not in list):
    print('X is not found in the list: ' , x)
else:
    print('X is found in the list: ', x)

if(y not in list):
    print('Y is not found in the list: ' , y)
else:
    print('Y is found in the list: ', y)

#! ===================== BITWISE OPERATOR ======================
#? In Python, bitwise operators are used to performing bitwise calculations on integers. The integers are first converted into binary and then operations are performed on bit by bit

#* Bitwise AND Operator : Returns 1 if both the bits are 1 else 0.
a = 10
b = 20
print('Bitwise and  Operation: ',a&b)

#* Bitwise or operator: Returns 1 if either of the bit is 1 else 0.
a = 10
b = 4
print('Bitwise or Operation: ',a|b)

#* Bitwise not operator: Returns one's complement of the number
a = 20
print('Not Operator: ',~a)

#* Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.
a = 10
b = 4
print('The Bitwise operator: ',a^b)

#! ------------------ Shift Operator -------------------
# *These operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by two respectively. They can be used when we have to multiply or divide a number by two.

#* Bitwise right shift

a = 10
res = a >> 1
print('Shift Right Operator: ',res)

b = -10
res = b << 1
print('Shift left: ', res)

# ! ------------------ Program for Nth term of Arithmetic Progression series (AP) ------------------------
#? The Arithmetic Progression Series is nothing but we can say that the difference
#* {a+(n-1)d } Series of nth term is need to find
#* Data To be used: a = 5000(First Month salary) , d = 2000 , n = 12

a = int(input('Enter Monthly Salary: '))
d = int(input('Enter your Increment : '))
n = int(input('Amount of months: '))
res = a+(n+1)*d
print('Salary after',n,'Months: ', res)

#! ------------------ Program for Nth term of Geometeric Progression series (GP) ------------------------
#? The adjustance number ratio will always be equal/common for all number in the series
#? For Example {d = c*r} [d = Previous Number , c = current number , r = ratio between them]
#* a*r^n-1 (a = first term , r = ratio , n = nth term need to find)

a = int(input('Salary amount: '))
r = int(input('common ratio: '))
n = int(input('Nth term to find: '))
res = a*r^n-1
print('Geometery Progressions: ',res)

#! ------------------ Program for Natural Number Sum Up ------------------------
# * n*(n+1)/2 -> The Formaula for the total of the natural number in the series
# * n = 10
n = 10
res = n*(n+1)/2
print('Money Saved: ',res)

#! ------------------ Program for finding First and Last number ------------------------
def firstNumber(n):
    while(n>9):
        n=n//10
    return print('First Number is : ',n)

def lastNumber(n):
    if(n>abs(0)):
        res = n%10
        print('Last number',res)

n = 98574
firstNumber(n)
lastNumber(n)