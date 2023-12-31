# Tutorial 13 - If Else & Elif Conditionals in python
print('\t Tutorial 13', 'https://youtu.be/3VejIihDfwU', '\n')
var1 = 4
var2 = 12
var3 = int(input('enter your number: '))  # string to integer
if var3 > var2:
    print('greater than 12')
elif var3 == var2:  # if used - statement is checked always. elif used - statement is checked only when previous statement is false.
    print('equal to 12')
else:
    print('lesser than 12')
exit

list1 = [55, 71, 6, 78, 64, 41]
print('\n', 71 not in list1)
if 71 not in list1:
    print('not in list')
else:
    print('in list')

exit

