#! --------------------- WHILE LOOP ----------------------------
#* while expression
    # * Statement
#? All the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code

count = 0
while(count < 3):
    count = count + 1
    print('Geeks for Geeks')

#* ============ Using else statement with while loops: ===================
#? The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won't be executed

count = 0
while count < 3:
    count = count + 2
    print('Count is Increasing!!')
else:
    print('Oops!! Problem has arise')

#* =================== Single while statement (INFINITY LOOP) ==========================
workHr = 5
while (workHr > 3): print('Too Much!!')

#! { It is suggested not to use this type of loops as it is a never ending infinite loop where the condition is always true and you have to forcefully terminate the compiler. }

#! =================== for in loop ==========================
#? For Loop are used for squence of traversals In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). There is "for in" loop which is similar to for each loop in other languages
#* for iterator_var in sequence:
    #* statements(s)

n = 4
for i in range(0,n):
    print(i)

# Iterating over a list
listIterat = [5,10,25,63,87]
for list in listIterat:
    print(list)

# Iterating over a tuple
tupleIteration = (85,96,85,24,630)

for Tuple in tupleIteration:
    print('Tuple:',Tuple)

# Iterating over String
stringIteration = 'Beluga'
for string in stringIteration:
    print(string)

#! =================== Using else statement with for loops ===================
#* But as there is no condition in for loop based on which the execution will terminate so the else block will be executed immediately after for block finishes execution.

list = ['geek','for','geeks']
for index in range(len(list)):
    print (list[index])
else:
    print('Inisde the else block')

# ! ====================== Nested Loops ==========================
# * Python programming language allows to use one loop inside another loop
# * A final note on loop nesting is that we can put any type of loop inside of any other type of loop

for i in range (1,5):
    for j in range(i):
        print(i,end=" ")
    print()

#* Continue Statement
#? It return the control in the beginning of the loop

for letter in 'BelugaLoveSkittle-Chan':
    if letter == '-' or letter == 'S':
        continue
    print('Message: ',letter)


# #* Break Statement
#? It brings the control out of the loop
for letter in 'geeksforgeeks':
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
         break
print ('Current Letter :', letter)

# * Pass Statement
# ? We use pass statement to write empty loops. Pass is also used for empty control statements, functions and classes.
# An empty loop
for letter in 'geeksforgeeks':
    pass
print ('Last Letter :', letter)
