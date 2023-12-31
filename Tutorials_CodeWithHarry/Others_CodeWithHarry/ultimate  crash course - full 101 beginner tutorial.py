print('\n THE ULTIMATE PYTHON CRASH COURSE - FULL PYTHON 101 BEGINNER TUTORIAL (CODE WITH HARRY) \n')
print('\t Video Link: https://youtu.be/vxHUFFiT0OI')

#
'''
multiline comment
print('ctrl+d for multiple cursors (or alt ?)')
print('ctrl+d for multiple cursors (or alt ?)')
'''
print('it\'s 18th may')
print('google escape characters to know more')
print(12+6)

#
print('\n VARIABLES AND DATATYPES \n')

a, b, c, d = 45, 1.25, 1.2j, '3rd variable'
print('datatype', type(a), type(b), type(c))
d, e = False, None
print(type(d), type(e))
# python can change the datatypes

#
print('\n STRINGS \n')

a = 'abcdefgh'
print(len(a), a[2:5])
#a[1] = 'c' elements of a string are immutable
print(a.replace('def','DEF'))
print(a.capitalize(), a.upper())

#
print('\n IF ELSE IN PYTHON \n')

age = int(input('input your age for driving: ')) # input function (str by default)
if age>18:
    print('you can drive')
elif age==18:
    print('make your lisence and drive')
else:
    print('you can\'t drive')

num = int(input('guess an integer between 0-50 (win for 5 numbers): '))
if num==9:
    print('you won')
elif num==14:
    print('you won')
elif num==26:
    print('you won')
elif num==30:
    print('you won')
elif num==44:
    print('you won')
else:
    print('you lose')

#
print('\n LOOPS IN PYTHON \n')

print('while loop')
i = 3
while(i<10):
    print(i)
    i = i+1
print('for loop')
for i in range(2,10):
    print(i)
    if i==4:
        continue
    if i==6:
        break

#
print('\n FUNCTIONS IN PYTHON \n')

def plus1(number):
    return number +1
print(plus1(10))
print(abs(12.654)) # built in python

#
print('\n MODULES IN PYTHON \n')

import math
print(math.ceil(5.36)) # greatest integer function
print(math.factorial(4))
print('google python built in modules')
print('install the modules (django, sklearn) (44:00)')

#
print('\n LISTS IN PYTHON \n')

list1 = [12,1,0,8,'skp',7,3]
print(type(list1))
list1.append('added1')
for l in list1:
    print(l)
list1[2] = 5
print(list1[1:5])

#
print('\n TUPLES IN PYTHON \n')

# tuples are immutable unlike lists (no append, edit etc.)
tup1 = (1,3,5,'g',5.1)
print(tup1, type(tup1))
print(tup1[1:4])

#
print('\n SETS IN PYTHON \n')

set1 = {2,3,1.5,2,0.5}
print(set1)
set1.add(10)
set1.add(0.5) # already present, not added
print(set1)
set2 = {2,7,6,2.5,0,1,3}
print(set2)
print('union', set1.union(set2))
print('intersection', set1.intersection(set2))
print('check out other operations on sets')

#
print('\n DICTIONARY IN PYTHON \n')

dict1 = {
    'v': 'violet', 'i': 'indigo', 'b': 'blue',
    'g': 'green', 'y': 'yellow', 'o': 'orange', 'r': 'red'
    }
print(type(dict1))
print(dict1['b'])
dict1['w'] = 'white' # adding an element
print(dict1)
print(len(dict1))

#
print('\n EXCEPTION HANDLING \n')

try:
    a1 = t.upper()
except Exception as e:
    print(e)
print('the error is skipped and the code is kept running')

#
print('\n FILE HANDLING \n')

file1 = open('open file 1 (cwh).txt', 'w') # 'w' for write mode
file1.write('it\'s the first file created by python code.')
file1.close()
file1 = open("open file 1 (cwh).txt", 'r')
read1 = file1.read()
print(read1)
file1 = open('open file 1 (cwh).txt', 'a')
file1.write('try to do more...')  # check

#
print('\n CLASSES AND OBJECTS IN PYTHON \n')

class data1:
    # constructor which will get executed everytime an object is created
    def __init__(self, topic, starting, name) -> None:
        self.topic = topic
        self.starting = starting
        self.name = name
        print(f'data created: {topic} in {starting} by {name}')

    def data1display(self):
        print(f'{self.topic} was explained in the year {self.starting} by {self.name}')

bbr = data1('black body radiation', '1900', 'Max Planck')
qm = data1('quantum mechanics', '1925', 'Heisenberg and Schrodinger')
str = data1('special relativity', '1905', 'Einstein')
peeff = data1('photo-electric effect', '1905', 'Einstein')
qm.data1display()
