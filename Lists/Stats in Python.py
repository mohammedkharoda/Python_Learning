# ! --------- Important Measure and control of functions--------------
#? mean() - This function returns the mean or average of the data passed in its arguments. If passed argument is empty, StatisticsError is raised.

#? mode() - This function returns the number with maximum number of occurrences. If passed argument is empty, StatisticsError is raised.

#? median() - This function is used to calculate the median, i.e middle element of data. If passed argument is empty, StatisticsError is raised.

#!========= PreRequ =====================
import statistics

li = [1, 2, 2, 2, 3, 3, 1, 2, 1, 2]

print('The mean average is the value: ', end="")
print(statistics.mean(li))

print('The mode occurance is the value: ', end="")
print(statistics.mode(li))

print('The middle occurance is the value: ', end="")
print(statistics.median(li))

#! ==> Average in the lists

def avrg(list):
    return sum(list)/len(list)

lst=[8,4,21,36,20,11]
total = avrg(lst)
print(round(total,2))

#! -> Using Reduce and Lambda
from functools import reduce

def avrg(list):
    return reduce(lambda a,b:a+b,list)/len(list)
lst=[8,4,21,36,20,11]
total = avrg(lst)
print(round(total,2))

#! -> Using the mean Function:

from statistics import mean
def avrg(list):
    return mean(list)

lst=[8,4,21,36,20,11]
total = avrg(lst)
print(round(total,2))