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
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

class Phone(Item):      # parent and child classes
    # all = []
    def __init__(self, name: str, item_price: float, item_quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, item_price, item_quantity)

        # Validations of arguments
        # assert item_price > 0, f'Price {item_price} is not grater than 0'
        # assert item_quantity >= 0, f'Quantity {item_quantity} is not greater than or equal to 0'
        assert broken_phones >= 0, f'Broken phones {broken_phones} is not greater than or equal to 0'

        # assign self object
        # self.name = name
        # self.price = item_price
        # self. quantity = item_quantity
        self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)

phone1 = Item('Samsung', 45, 9)
phone1.broken_phones = 2     # not a good method to deal with constructor codes
phone2 = Item('Oppo', 30, 5)
phone2.broken_phones = 2

phone1 = Phone('iPhone', 90, 4, 1)
phone2 = Phone('Vivo', 25, 13, 3)

print(phone1.calculate_total_price())

print(Item.all, '\n', Phone.all) # __repr__ is used to print

