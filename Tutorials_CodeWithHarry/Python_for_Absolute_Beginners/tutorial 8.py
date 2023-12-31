# Tutorial 8 - Strings & Related Functions
print ('\t Tutorial 8 :', 'https://youtu.be/lPZn7zcGXQo', '\n')
mystr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print ( len(mystr),'\n', mystr[0:6], mystr[0:9], '\n',mystr[0:], mystr[:7])
# len (mystr) gives the total number of characters present in the string. Lower limit of string is included, but the upper limit is excluded.
print (mystr[1:7:3])
# start from 1 and end at (7-1). The last term denotes that (3-1) entries are skipped. The third term is used as 0 if we keep it empty.
print (mystr[2::2], mystr[:6:4], mystr[::], mystr[::16])
print (mystr[-5:-1], mystr[-4465:-2])
#
"""
a negative sign means that counting will be occured from the opposite direction.
The sequence of counting : (for len=7)
'0,1,2,3,4,5,6' or '-7,-6,-5,-4,-3,-2,-1'
"""
print (mystr[134:0:-1], mystr[-1:-5:-1])
# If we use negative sign in the 3rd term, we will get reversed terms in the output. In this case we must alter the 1st two terms.
print ('Functions')
print (mystr.isalnum(), mystr.isalpha())
#bif there remains any space in the string, we will get False in the output using functions isalnum and isalpha
print (mystr.endswith("xyz"), mystr.endswith("XYZ"))
print (mystr.count('A'))
# It counts no. of desired characters present in the string.
print (mystr.capitalize())
# it makes the 1st word capital and the others will be in small letters.
print (mystr.find('IJK'))
# it gives the position of the searched entry in the string.
print (mystr.lower(), mystr.upper())
# lower makes all the characters small, while upper makes all the characters capital.
print (mystr.replace('DEF', 'def'))
# by using replace, the 1st term in the string will be replaced by the second term.
print (mystr)
# After all these operations the real string remains unchanged.
print ("for more string functions, google 'string functions in python'")
exit
