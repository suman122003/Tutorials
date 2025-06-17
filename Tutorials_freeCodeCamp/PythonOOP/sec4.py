from sec4_item import Item
from sec4_phone import Phone

Item.instantiate_from_csv()
print(Item.all)

item1 = Item('Item1', 750)
item1.name = 'Item1_modified'

print(item1.name, item1.read_only_name)
