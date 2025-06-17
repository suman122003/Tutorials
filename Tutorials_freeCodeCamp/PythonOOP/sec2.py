import csv

class Item():
    all = []
    pay_rate = 0.8  # 20 % discount
    def __init__(self, name: str, item_price: float, item_quantity=0):
        # Validations of arguments
        assert item_price > 0, f'Price {item_price} is not grater than 0'
        assert item_quantity >= 0, f'Quantity {item_quantity} is not greater than or equal to 0'

        # assign self object
        self.name = name
        self.price = item_price
        self.quantity = item_quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod   # decorator
    def instantiate_from_csv(cls):  # cls as 1st argument
        with open('items.csv', 'r') as f:
            reader_ = csv.DictReader(f)
            items = list(reader_)
        
        for item_ in items:
            # print(item_)
            Item(name = item_.get('name'),
                 item_price = float(item_.get('price')),
                 item_quantity = int(item_.get('quantity')),)

    @staticmethod       # decorator        
    def is_integer(num):   # no cls unlike @classmethod
        'This checks 5.0 or 10.0 as an integer'
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


# DIFFERENCES BETWEEN CLASS AND STATIC METHODS

class Item:
    @staticmethod
    def is_integer(num):
        '''This should do something that has a relationship with the class, 
        but not somethng that must be uique per instance!'''

    @classmethod
    def instantiate_from_something(cls):
        '''This should alos do something that has a relationship with the class, 
        but usually, those are used to manipulate different structures of data 
        to instantiate objects, like we have done with csv'''


# Calling class and static methods from both class and instance level

Item.instantiate_from_csv()
print(Item.all)

print('is_integer:', Item.is_integer(7), 
      Item.is_integer(3.5), Item.is_integer(6.0), Item.is_integer('abc'))

item1 = Item()
item1.is_integer(10.0)
item1.instantiate_from_something()

