from sec5_item import Item
from sec5_phone import Phone
from sec5_keyboard import Keyboard

item1 = Item('Item1', 600)
# item1.price = -500  # we can't change
print(item1.name, item1.price)
item1.apply_increment(0.2)
print(item1.price)
item1.apply_discount()
print(item1.price)

item1.send_email()

item2 = Phone('Phone1', 900)
print(item2.name, item2.price)
item2.apply_increment(0.2)
print(item2.price)
item2.apply_discount()
print(item2.price)

name1 = 'Devdas'    # e.g. of Polymorphism
nameList = ['Devdas', 'Paro', 'Chunni Babu', 'Chandramukhi']
print(len(name1), len(nameList))

item3 = Keyboard('Keyboard1', 90, 7)
print(item3.name, item3.price)
item3.apply_discount() # different discount for Keyboards
print(item3.price)

