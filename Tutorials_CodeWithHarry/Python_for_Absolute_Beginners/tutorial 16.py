# Tutorial 16 - for loops in python
print ('\t Tutorial 16', 'https://youtu.be/sSyCRQx5WM0', '/n')
list1 = [[26,8],9,(6,7),[44,7],54]
for item in list1 :
	print (item) # ordinary print = 1 line. for loop and  print = one element in one line.
list2 = [('Argentina','Messi'), ('Brazil', 'Neymar'), ('Portugal', 'Ronaldo')]
dict1 = dict (list2)
print (dict1)
for country, captain in list2 :
	print ('\t', country, 'is led by', captain) # tab is taken in each line
for country, captain in dict1.items () :  # function dict1.items () used here
	print ('\n', country, 'is led by', captain) # extra line is taken in each line
for item in dict1 :
	print ('\t', item)
list3 = ['SKP', 61,81,6,88,5,7,8,65,8,10,6]
for item in list3 :
	if str(item).isnumeric () and item>=10 :
		print ('item greater than 10 in list3 is', item)  # function str(item).isnumeric ()
exit
