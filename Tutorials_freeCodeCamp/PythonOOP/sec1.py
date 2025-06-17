item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price*item1_quantity
print(type(item1), type(item1_price), type(item1_quantity), type(item1_price_total))

class Item:
    pass

class Item:
    def __init__(self):
        print('An item is CREATED!')
    def calculate_total_price(self, x, y):
        return x * y

item1 = Item()
item1.name = 'Bottle'
item1.price = 100
item1.quantity = 5
print(type(item1), type(item1.name), type(item1.price), type(item1.quantity))
print(f'item1: {item1.calculate_total_price(item1.price, item1.quantity)}')

class Item():
    def __init__(self, name: str, item_price: float, item_quantity=0):
        print(f'An instance created: {name.upper()}')
        self.name = name
        self.price = item_price
        self.quantity = item_quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Bottle', 100, 5)
print(item1.name, item1.price, item1.quantity, item1.calculate_total_price())

item2 = Item('Earphone', 900)
print(item2.quantity)

item3 = Item('Calculator', 1000, 2)
item3.has_matrix = False

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

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

item1 = Item('Phone', 15000, 2)
print('Class attribute: pay_rate', Item.pay_rate, item1.pay_rate)
print(Item.__dict__, item1.__dict__)
item1.apply_discount()
print('Price after discount:', item1.price)

item2 = Item('Calculator', 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

item3 = Item('Mouse', 400, 5)

for instance in Item.all:
    print(f'{instance.name} - Price: {instance.price}, Quantity: {instance.quantity}')
print(Item.all)

