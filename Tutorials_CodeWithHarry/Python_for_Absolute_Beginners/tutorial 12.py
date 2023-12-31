# Tutorial 12 - Sets in Python
print ('\t Tutorial 12', 'https://youtu.be/iVJv3zdgkD4', '\n')
s0= set ()     # empty set
s1 = set ()
s2= set ([5,8,9,7,5,3])
print (s0, s2, type (s1), len(s1), len(s0), min (s2))  # one element is used one time only
s1.add (1)
s1.add (1)
s1.add (2)
print (s1)  # one element is added one time only
s3 = s1.union ({5,9,'abc'})
s4 = s1.union (s2)
print (s3,s4)
s5= s4. intersection ({1,2,3,4,5,6})
print (s5)
print (s4.isdisjoint (s5), s0.isdisjoint (s4)) # disjoint test
s5.remove (2)
print (s5)
exit

