#! --------------------- Slicing --------------
#* =========== LISTS ==============
x = [10,20,30,40,50]
print(x[1:4])
# #? Reversing the index method
print(x[4:0:-2])

#* =============== Get Smaller Elements ==============
def smallerElement(list,el):
    smallerList=[]

    for i in list:
        if(i<el):
            smallerList.append(i)
    return smallerList

userList = input('Enter a number: ')
userList_Filter = userList.split(',')
element = input('Enter the Number to find: ')
testCase = smallerElement(userList_Filter,element)
print(testCase)

#* =================== Separted Even and Odd =================

def even_odd_list(mix):
    even=[]
    odd=[]
    for i in mix:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    print('Even list is',even)
    print('Odd list is ',odd)

mixList = [25,87,55.63,24,20]
even_odd_list(mixList)