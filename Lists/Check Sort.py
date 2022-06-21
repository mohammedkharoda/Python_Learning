#! => Approach 1: Using Navie Method
#* -> If we can find a smaller element after the first element if yes than the loop is not sort elese it is sorted

test_list = [25,4,5,8,9,10]
print('Original list: ' + str(test_list))

flag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i-1]):
        flag = 1
    i = i+1

if(not flag):
    print('Yes list is Sorted')
else:
    print('List is not sorted')

#! ------------------------ Using Sort() ------------------------------
test_list = [10,25,45,60,21,90]
print('Original List: ',test_list)

flag = 0
test_list1 = test_list[:]
test_list1.sort()
if(test_list1 == test_list):
    flag = 1

if(flag):
    print('yes it is sorted')
else:
    print('No it is not sorted')
