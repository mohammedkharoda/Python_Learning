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

#!