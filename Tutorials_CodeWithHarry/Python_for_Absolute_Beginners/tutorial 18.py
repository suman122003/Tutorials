# Tutorial 18 - break & continue statements
print ('\t Tutorial 18', 'https://youtu.be/aXGC1fx6QQo', '\n')
i = 0
while (i<30) :
	i = i+2
	print (i+1, end=' ')
i=0
while (True) : # while (True) is a loop that continues to infinity until we break it
	print (i+4)
	i= i+11
	if (i>100) :
		break   # stop the loop
i=0
while (True) :
	if i+1<5 :
		i=i+1
		continue
	print (i+1, end = ' ')
	if (i==50) :
		break
	i= i+1
# making a code in which we want to check if the input is greater than 100 or not
while (True) :
	inp = float(input (" \n\nEnter a number \n"))
	if inp>100 :
		print ('Yeah ! the entered number is greater than 100')
		break
	else :
		print ('try again')
		continue
exit
