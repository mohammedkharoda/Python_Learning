n = abs(int(input('Enter a number: ')))
digit = 0

while n>0:
    n = n//10
    digit = digit+1

print('Number of digits: ',digit)

# ! ------------------------------------------- Factorical Number --------------------------------------
n = int(input('Enter a number: '))
i = 1
fac = 1
while(i<= n):
    fac=fac*i
    i = i+1
print('Factorial of:',n,"=",fac)

# ans = 1
# for i in range(1,n+1):
#     ans = ans * i
# return ans
# print('Factorial of:',n,"=",ans)
#! ---------------------------------------- ALL NUMBER DIVISIOR ---------------------------------
# n = int(input('Enter a Number = '))

for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
#! --------------------------------------------------
i = 1
while (i<=n):
    if n%i==0:
        print(i,end=" ")
    i=i+1

# ! ----------------------------------------- No prime number --------------------------

n = int(input('Enter a Number = '))

if(n<2):
    print('Not Prime')
else:
    for i in range(2,n):
        if(n%i==0):
            print('Not Prime')
            break
    else:
        print('prime')

#! ----------------------------------------- Fibonnaci number --------------------------

n = int(input('Enter a Number = '))

first = 0
second = 1

if(n==1):
    print(0)
else:
    print(0,1,end=" ")

for i in range(3,n+1):
    current = first+second
    print(current,end=" ")
    first=second
    second=current

#! ----------------------------------------- Fibonnaci number --------------------------
a = int(input('Enter the 1st Number: '))
b = int(input('Enter the 2nd Number: '))
small = min(a,b)

for i in range(1,small+1):
    if(a%i==0 and b%i==0):
        gcd=i

print('GCD: ',gcd)