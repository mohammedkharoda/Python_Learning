# * ---------------- Simple Loops ----------------
# #! => For loop Vs List Comprehensions
# Empty Lists
List=[]
for charcs in 'WorkingToLate':
    List.append(charcs)
print(List)

# #! => List Compreshensions
List = [charc for charc in 'WorkingToHard']
print(List)

#* --------------------------- Nested List Compherision ---------------

matrix=[]
for i in range(3):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)

print('For Loop Inner Loops',matrix)
#
# #! => List Compreshensions
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

# *---------------- Using the Conditions in the If Statement -------------
def digitSum(n):
    digitsum=0
    for element in str(n):
        digitsum+= int(element)
    return digitsum

List=[367,114,561,524,2780,220,745]
newList=[digitSum(i) for i in List if i&1]
print(newList)