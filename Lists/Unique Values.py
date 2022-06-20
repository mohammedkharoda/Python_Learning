#! => There are many ways to tackel this problem the first is too used "BRUTE FORCE"

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
list1 = []
count=  0
for item in input_list:
    if item not in list1:
        list1.append(item)
        count+=1
print('No of Unique Count is: ',count)

#? => But the approach takes more time and space complexity and due to this the method of being iteration is not possible the best one

#! => Using the "Counter method" to solve the issues
#? Using the Counter function we will create a dictionary. The keys of the dictionary will be the unique items and the values will be the number of that key present in the list.  We will create a list using the keys, the length of the list will be our answer.

from collections import Counter
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
items = Counter(input_list).keys()
print('No of Unique Items are: ', len(items))

#! => Using the "Sets" to solve the issues
input_list = [1,2,2,3,3,3,4,8,5,6]
new_list = set(input_list)
print('Unique Values: ',len(new_list))
