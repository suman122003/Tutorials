# Tutorial 9 - Lists in python
print ('Tutorial 9', 'https://youtu.be/neTsPE9XFsQ', '\n')
list1 = ['a', 'b', 'c', 'd', 'e']
print (len(list1), list1[3])
list1.append('f')
list1.remove('f')
list1.insert(0,0)
print (list1)
nums=[3,9,9,6,18,9,3,3,7,6,81,3,6,8]
print (nums)
nums.sort()
print (nums)
nums.reverse()
print (nums)
print (nums [1:6], nums [:19], '\n', nums [::3], nums [::-3], nums [1:9:2], nums [9:1:-2])
# sort and reverse functions change the original list but SLICING keeps the list unchanged.
nums.append (6)  # add element at the end
nums.insert (7,'random numbers')   # the 1st term denotes the position of list and the 2nd term contains the element to insert.
print (nums)
nums. remove (6)
print (nums)    # if the element we want to remove is present at multiple positions of the list, the element at the least position will be removed only.
nums.pop()    # remove 1 element from the end
print (nums)
nums [0] = 5.0    # to change the elements
nums [3] = 2.0
print (nums)
# mutable - can change, immutable - cannot change. List is mutable but Tuple is immutable.
tp1 = (61,5,76,8)    # tuples. different from lists. parenthesis
print (tp1)
tp2= (6)
print (tp2)  # for 1 element in tuple, only the element is printed without brackets. (unlike list)
a = 5
b = 6
t = a
a = b
b = t   # to interchange the values of a and b
print (a,b)
c = 7
d = 4
c,d = d,c   # to interchange the values of c and d
print (c,d)
print ('google python list functions and explore')
exit ()
