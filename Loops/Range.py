#! ============= RANGE ============
#* Python range() function returns the sequence of the given number between the given range.
#* Python range() function for loop is commonly used hence, knowledge of same is the key aspect when dealing with any kind of Python code. The most common use of range() function in Python is to iterate sequence type (Python range() List, string, etc. ) with for and while loop.

#! ============= Python Range() ==============
# ? In simple terms, range() allows the user to generate a series of numbers within a given range. Depending on how many arguments the user is passing to the function, user can decide where that series of numbers will begin and end as well as how big the difference will be between one number and the next.range() takes mainly three arguments.
#
# * start: integer starting from which the sequence of integers is to be returned
# * stop: integer before which the sequence of integers is to be returned. The range of integers end at stop - 1.
# * step: integer value which determines the increment between each integer in the sequence
#
for i in range(10):
    print(i,end=" ")
print()

list = [98,28,10,22,34,58,10]
for i in range(len(list)):
    print(list[i],end = " ")
print()

sum = 0
for i in range(1,11):
    sum=sum+i
    print('Sum of numbers: ',sum)
print()

#! ----------------------------- Ways to call Python Range()----------------------
#* There are three ways you can call range() :
#* range(stop) takes one argument.
#* range(start, stop) takes two arguments.
#* range(start, stop, step) takes three arguments.

#! #################### Range(STOP) ####################
#* When user call range() with one argument, user will get a series of numbers that starts at 0 and includes every whole number up to, but not including, the number that user have provided as the stop
for i in range(10):
    print(i,end = " ")
print()

for i in range(20):
    print(i,end=" ")

#! ################### range(start, stop) ################
#* When user call range() with two arguments, user get to decide not only where the series of numbers stops but also where it starts, so user don’t have to start at 0 all the time. User can use range() to generate a series of numbers from X to Y using a range(X, Y)

for i in range(1,20):
    print(i,end=" ")
print()

for i in range(5,20):
    print(i,end=" ")
print()

#! ################### range(start, stop, step) ################
#* When the user call range() with three arguments, the user can choose not only where the series of numbers will start and stop but also how big the difference will be between one number and the next

#* divisible by 3
for i in range(0,30,3):
    print(i,end = " ")
print()

#* divisible by 5
for i in range(0,50,5):
    print(i,end=" ")
print()

#! ################### python range() backwards ################
for i in range(25,2,-2):
    print(i,end = " ")
print()

for i in range (20,3,-8):
    print(i,end = " ")
print()

#! ################### Concatenation of two range()  ################
#* The result from two range() functions can be concatenated by using the chain() method of itertools module. The chain() method is used to print all the values in iterable targets one after another mentioned in its arguments.

from itertools import chain

print('concatenation of range: ')
res = chain(range(5),range(10,20,5))

for i in res:
    print(i,end = " ")


#! %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% POINT TO BE REMEBER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#* Points to remember about Python range() function :

#* range() function only works with the integers i.e. whole numbers.
#* All arguments must be integers. Users can not pass a string or float number or any other type in a start, stop and step argument of a range().
#* All three arguments can be positive or negative.
#* The step value must not be zero. If a step is zero python raises a ValueError exception.
#* range() is a type in Python
#* Users can access items in a range() by index, just as users do with a list: