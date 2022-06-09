# Printing a Table

number = int(input('Enter a Number to get the table: '))
upper = int(input('Enter a Upper to get the table: '))
lower = int(input('Enter a Lower to get the table: '))


inital = lower
while( inital <= upper):
    total = inital*number
    print(total)
    inital = inital+1


