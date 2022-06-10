#! ------------------ NOTES TO BE TAKEN ----------------------
#? First Row: i = 0
#? Last Row: i = n-1
#? First Column: j = 0
#? Last Column: j = n-1
#? Middle Row or Col: n//2
#? Major Diagonal: i == j
#? Left Diagonal: i+j == n-1


#! ========= Square pattern Method ============
# n = int(input('Enter the number: '))
#
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()

#! =========== Triangle Pattern Method ==========
#
# n = int(input('Enter the number: '))
#
# for row in range(n):
#     for cols in range(n-row):
#         print('*',end=" ")
#     print()

#! ================== Pyramid of Triangle ==================
#
# n = int(input('Enter the Number: '))
#
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print('*',end="")
#     print()

#! ================== Square Parallel Bar ==================

# n = int(input('Enter the Number: '))
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1):
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

#! ========================= Plus Pattern Program ===================
# n = int(input('Enter the Number: '))
# for i in range(n):
#     for j in range(n):
#         if(i==n//2 or j==n//2):
#             print('*',end="  ")
#         else:
#             print(' ',end="  ")
#     print()

#! ========================= Cross Pattern Program ===================
# n =int(input('enter a number: '))
# for i in range(n):
#     for j in range(n):
#         if(i+j==n-1 or i==j):
#             print('*',end="  ")
#         else:
#             print(' ',end="  ")
#     print()

#! ========================= Hollow Square Program ===================
# n=int(input('Enter a number: '))
# for i in range(n):
#     for j in range(n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print('*',end="  ")
#         else:
#             print(' ',end="  ")
#     print()