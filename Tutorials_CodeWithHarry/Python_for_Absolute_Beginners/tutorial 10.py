# Tutorial 10 - Dictionary in python
print ('\t Tutorial 10', 'https://youtu.be/5y1sh0-oKTE', '\n')
# Dictionary is nothing but key value pairs
d1 = {}    # type - dictionary. immutable
print (type(d1))
d2 = {"PE effect" : "Einstein", "Compton effect" : "Compton", "Black body radiation" : "Planck", "Quantum mechanics" : {'1st' : 'Planck', '2nd' : 'De Broglie', '3rd' : 'Schrödinger', '4th' : 'Heisenberg'}}
print (d2['PE effect'], d2['Quantum mechanics'], d2['Quantum mechanics']['2nd'])
d2['Gravity'] = 'Newton'
d2 [12] = 'SKP'
print (d2)
del d2[12]
print (d2)
d3 = d2
del d3 ['Quantum mechanics']
print (d2)  # d3=d2 doesn't make a copy. If we delete an element from d3, that element will also be deleted from d2.
print (d2.get ('Quantum mechanics')) # to get a deleted element.
d2.update ({'Laws of motion' : 'Newton'})  # to update a new element
print (d2)
print (d2.keys(), '\n', d2.items())
print ('google dictionary functions and explore.')
exit
