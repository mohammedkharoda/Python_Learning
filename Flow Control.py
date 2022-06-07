# # ! ----------------- IF SATMENT --------------------------
# # ? if statement is the most simple decision-making statement. It is used to decide whether a certain statement or block of statements will be executed or not i.e if a certain condition is true then a block of statement is executed otherwise not

a = 10
if(a>5):
    print('The Value is greater than the 5: ', a)

# #! ---------------------------- IF-ELSE Statement ------------------
# # ? The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But what if we want to do something else if the condition is false. Here comes the else statement. We can use the else statement with if statement to execute a block of code when the condition is false.

a=20
if(a > 30):
    print('The number is greater than 30: ',a)
else:
    print('The number is less than 30')

# #! ---------------------------- Nested IF --------------------------
# #? A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement inside another if statement. Yes, Python allows us to nest if statements within if statements. i.e, we can place an if statement inside another if statement.

i = 10
if(i==10):
    print('It is 10') # Excuted

    if(i > 15):
        print('I is greater than 15')
    else:
        print('I is smaller than 15') # Also excuted as it has make the if condition false of 15

# #! -------------------- if-else-elif ladder ----------------------
# #? Here, a user can decide among multiple options. The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final else statement will be executed.

a = 20
if(a == 10):
    print('equal to 20: ',a)
elif(a > 20):
    print('Great than 20: ',a)
elif(a == 20):
    print('The number is present: ',a)
else:
    print('Is not present')

# #! ------------------------- Short-Hand Statement ---------------
# #? Whenever there is only a single statement to be executed inside the if block then shorthand if can be used. The statement can be put on the same line as the if statement.

a = 10
if a < 15:
    print('a is less than 15:',a)



# #! -------------- Short Hand if-else statement ----------
# #? This can be used to write the if-else statements in a single line where there is only one statement to be executed in both if and else block.

a = 10
print(True) if a < 10 else print(False)

##! -------------- Even or Odd method using the Recurvise ----------
##? we used to call operator that is modulus operator
##? Even Number: A number Which is completely divisible by 2 Hence remainders is 0
##? Odd Number: A number which is not divisible by 2 Hence remainders is 1

## ! ===================== APPROACH - 1 ===========================
## #* We use the concept of getting the remainder without using the modulus operator by subtracting the number by number-2
## #* If at last, we get any remainder then that number is odd and return the False for that number
## #* Else the number is even and return True for that number
def evenOdd(n):
    if(n==0):
        return True
    elif(n==1):
        return False
    else:
        return evenOdd(n-2)


n=3
if(evenOdd(n)):
    print(n,'The Number is even')
else:
    print(n,'The Number is odd')

# #! ===================== APPROACH - 2 ===========================
# #* We use the modulus operator to find the even or odd Like if num % 2 == 0 then the remainder is 0 so the given number is even and return True
# #* Else if num % 2 != 0 then the remainder is not zero so the given number is odd and return False

def evenOdd(n):
    if(n%2 == 0):
        return True
    elif(n%2!=0):
        return False
    else:
        return evenOdd(n)

n = 896563521
if(evenOdd(n)):
    print('Yup it is Even!')
else:
    print('Yup it is Odd!!')

# #! ===================== APPROACH - 3 ===========================
#* Given a range, we need to print all the even numbers in the given range.

start,end = 10,29
for num in range(start,end+1):
    if(num%2==0):
        print('\n The Even Score: ',num,end=" ")
    elif(num%2!=0):
        print('\n The Odd Score: ',num,end=" ")


#! ------------------------ MAXIMUM OF 3 ---------------------------
#! ======================== Approach 1 =============================
a = 10
b = 20
c = 30

if(a>=b) and (a>=c):
    print('Largest no: ',a)
elif(b>=a)and (b>=c):
    print('Largest no: ',b)
else:
    print('Largest no: ',c)

#! ----------------------------- The Leap Year ------------------------
#! ======================== Approach 1 =============================

#? A year is a leap year if the following conditions are satisfied:
#? The year is multiple of 400.
#? The year is multiple of 4 and not multiple of 100.

leapYear= int(input('Enter the number to check: '))

if(leapYear%400 == 0):
    print('This is a leap year!!',leapYear)
elif(leapYear%4==0) and (leapYear%100!=0):
        print('This is a leap year!!',leapYear)
else:
    print('Not a Leap year!',leapYear)

#! ======================== Approach 2 =============================
def checkYear(year):
    import calendar
    return (calendar.isleap(year))

year = 2000
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")