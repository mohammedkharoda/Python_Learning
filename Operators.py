# Additional Operators
value1 = 2
value2 = 3
res = value1+value2
print('Addition: ',res)

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