# Smiple While Loop
count = 0
while(count<3):
    count = count+1
    print('Hello')

#Python with the While loop List
a = [1,2,3,4,5,6]

while a:
    print(a.pop())

# Pass Statement in While Block
a = 'GeeksForGeeks'
i = 0

while i< len(a):
    i += 1
    pass
print('value of the' , i)

#! ========================= Sentinal Control Statement ==========================
# In this, we don't use any counter variable because we don't know that how many times the loop will execute. Here user decides that how many times he wants to execute the loop. For this, we use a sentinel value. A sentinel value is a value that is used to terminate a loop whenever a user enters it, generally, the sentinel value is -1.

# First, it asks the user to input a number. if the user enters -1 then the loop will not execute
# User enter 6 and the body of the loop executes and again ask for input
# Here user can input many times until he enters -1 to stop the loop
# User can decide how many times he wants to enter input

senti = int(input('Enter a number (-1 to quit): '))

while senti!= - 1:
    senti = int(input('Enter the number(-1 to quit): '))