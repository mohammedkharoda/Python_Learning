# # creating List
# List = []
# print('Blank List:')
# print(List)
#
#
# # Creating a List of Number
# List = [10,20,40]
# print('\nList of Number: ')
# print(List)
#
# #Creating a List of String and accessing
# # Using index
# List = ["Geeks","For","Geeks"]
# print('\nList Items')
# print(List[0])
# print(List[2])
#
# #Creating a MultiDimension List
# List = [['Geeks' , 'For'],['Geeks']]
# print('\n Multi-dimension list: ')
# print(List)

# ! -------------- Create A list with Multiple Distinct Element ----------
#
# List = [1,2,3,4,4,5,5,6,7]
# print('\nList with the use of Repetitive  Number')
# print(List)
#
# #Creating a List with Mixed value data
# List = [1,2,3,4,"Geeks","Samusa",23.85]
# print('Mixed element List')
# print(List[4])

# ! ------------ Knowing the Size of the List -----------
# Creating a List
# List1 = []
# print('Length of the List is: ')
# print(len(List1))
#
# #Creating  a List of Number
# List2=[10,20,30]
# print('Length of the List is: ')
# print(len(List2))

# ! ---------- Adding Element to a List -----------
# # Append() Method one elem can be added into the list
# List=[]
# print('Inital blank list: ')
# print(List)
#
# #Addition of Element
# #in the List
# List.append(1)
# List.append(2)
# List.append(3)
# List.append(4)
# print("After the Append Method " , List)
# print(List)
#
# #! --------- Using Iterator adding Element ----------
# ListAppend = []
# for i in range(1,4):
#     ListAppend.append(i)
# print('\nList of the Number adding using Iterator')
# print(List)
#
# #! -------------- Adding Tuples to the List -------
# ListTuple = [1,2,3,5]
# ListTuple.append((5,6))
# print('\nList of Append element with the Tuple')
# print(ListTuple)
#
# #! -------------- Addition of List to List -----------
# ListToList = ['for','geeks']
# ListToList.append(ListTuple)
# ListToList.append(ListAppend)
# print('List in List with tuple in list')
# print(ListToList)

# ! -------------- Using the Insert Method -----------
# List = [1,2,23,4,56]
# print('Inital List :')
# print(List)
#
# # Adding using Insert
# List.insert(3,12)
# List.insert(0,'geek')
# print('\n Performing the Insert Operation at 0 Index :')
# print(List)

# ! ======== Using Extends Methods ======
# List = [1,2,3,4]
# print('Inital List')
# print(List)

# List.extend([8,'geeks','always'])
# print('\n Has been Extend using the Geeks')
# print(List)

# ! ============= Using the Remove Method ======
# List = [1,2,3,4]
# print('\n Inital List')
# List.remove(1)
# print(List)
#
# print('\n Remove of the element')
# for i in range(2,3):
#     List.remove(i)
# print("\nList after Removing a range of elements: ")
# print(List)

# ! ===================== Using the Pop Method =====
# List = [10,20,30,80,54]
# List.pop()# Removing Last Elem
# print(List)
# List.pop(3)
# print(List)

# ! ===================== Using Slice Method ==============
# List = ['G', 'E', 'E', 'K', 'S', 'F','O', 'R', 'G', 'E', 'E', 'K', 'S']
# print('\n Inital List')
# print(List)
#
# Sliced_List = List[6:9] # 6 -> Being of charc , 9 -> End of charc (9-1 = 8 print the data on 8)
# print('\n The list is being Sliced : ')
# print(Sliced_List)

# ? ============ Using to create a tuple ==========
# ! ============= CREATING TUPLES ==========
# Tuple1 = ()
# print('Intial empty tuple: ')
# print(Tuple1)
#
# #Creating a Tuple
# # with the use of string
# Tuple1 = ('Geek','For')
# print('\n Tuple wih the use of String')
# print(Tuple1)
#
# #Creating a Tuple with
# #the use of list
# list1 = [1,2,4,5,6]
# print('\n Tuple using List')
# print(tuple(list1))
#
# #creating tuple with the use of built-in
# Tuple1 = tuple('Geeks')
# print('\nTuple with the use of funtion: ')
# print(Tuple1)
#
#
# # Creating Mix dataType
# Tuple1 = (5,'Mixed','Welcome',7,'Geeks')
# print('\n Tuple with the ixed DataType: ')
# print(Tuple1)
#
# #Creating a Tuple with nested tuples
# Tuple1 = (0,1,2,3)
# Tuple2 = ('python','geek')
# Tuple3 = (Tuple2,Tuple1)
# print('\n Tuple Nested Inside Other')
# print(Tuple3)
#
# #Creating a Tuple with repetion
# Tuple1 = ('Geeks',)*3
# print('\nTuple with repetions: ')
# print(Tuple1)
#
# #Creating a Tuple with the use of loop
# TupleLoop = ('Geek')
# n=5
# print('\n Tuple with a loop')
# for i in range (int(n)):
#     Tuple1 = (Tuple1,)
#     print(TupleLoop)

# * Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.). Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing 'comma' to make it a tuple.

# ! =================== ACCESSING OF TUPLES =================
# * Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via unpacking or indexing (or even by attribute in the case of named tuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

# Tuple1 = tuple('Geek')
# print('\n First element of Tuple: ')
# print(Tuple1[0])
#
# TupleUnpacking = ('make','idli','dosa')
# print(TupleUnpacking)
# a,b,c = TupleUnpacking
# print('\nValue after unpacking')
# print(a)
# print(b)
# print(c)

# !=========== Concation of Tuple ==============
# Concatenation of tuples
# Tuple1 = (0,1,2,3)
# Tuple2 = ('Geek','For','Geek')
# Tuple3 = Tuple1+Tuple2
#
# # Printing First tuple
# print('\nTuple1 : ')
# print(Tuple1)
#
# # Printing Second tuple
# print('\nTuple2 : ')
# print(Tuple2)
#
# #Printing Final Tuple
# print('\nTuple after Concatenation: ')
# print(Tuple3)

# ! ==================== Slicing Tuple ====================
# Removing the Fist element

# Tuple1 = tuple('GeeksForGeeks')
# print('Removal of First Element')
# print(Tuple1[1:])
# print(Tuple1)

# Reversing the Tuple
# print('\nTuple after sequence of ELement is reversed: ')
# print(Tuple1[::-1])

# printing eleemtn of a range
# print('\nPricing element between Range 4-9: ')
# print(Tuple1[4:9])
# TupleCount = Tuple1.count('G')
# print(TupleCount)
#
# #! ================= Deleting a Tuple ================
# * Note- Printing of Tuple after deletion results in an Error.
# * Tuples are immutable and hence they do not allow deletion of a part of it. The entire tuple gets deleted by the use  of del() method.
# Tuple1 = (0,1,2,3,4)
# del Tuple1

# ? =================== SETS ========================
# * In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
# * The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set

# set1 = set()
# print('inital blank set:')
# print(set1)

#Creating  set with the use of a string
# String = set('Geek for Geek')
# set1 = set(String)
# print('\n set of the use object ')
# print(set1)

#Creating set with the use of List
# set1 = set(['Geeks','For','Geeks'])
# print('\nSet with the use of List: ')
# print(set1)

#Creating a set with a list of Number
# set1 = set([1,2,'Geeks',4,'For',5,'Geeks',6])
# print('\nSet is wih the use of the mix datatype','\n',set1)

#! ================ Adding Set (Add and Update method) ======================
# * --- ADDITION ---
# setAdd = set()
# print('Inital Addition Set: ', '\n', setAdd)
# using the add method
# setAdd.add(5)
# setAdd.add(85)
# setAdd.add('Adding Element')
# print('After Adding the Element in the Set: ','\n',setAdd)

# usisng the iterator
# setIterator = set()
# for i in range (1,7):
#     setIterator.add(i)
# print('\n After the Iteration','\n',setIterator)

# * --- UPDATE ----
# setUpdate = set([4,5,(6,7)])
# setUpdate.update([10,11])
# print('\nSet after the Addition of Element using Update')
# print(setUpdate)

# !====================== Accessing a Set ====================

# * Set items cannot be accessed by referring to an index, since sets are unordered the items has no index. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# * ---- In method ----
# setCheck = set([85,98,45,32,10,74])
# print('\nChecking the Value: ', 85 in setCheck)
# print('\n Checking another Value: ' , 'geeks' in setCheck)

#* ---- Iteration Method -----
# setCheck = set([48,'Geeks','In','For',856,21,10])
# for i in (i):
#     print(i)

# ! ==================== Removing the Elements =============





