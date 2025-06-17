import csv

class Item():
    all = []
    pay_rate = 0.8  # 20 % discount
    def __init__(self, name: str, item_price: float, item_quantity=0):
        # Validations of arguments
        assert item_price > 0, f'Price {item_price} is not grater than 0'
        assert item_quantity >= 0, f'Quantity {item_quantity} is not greater than or equal to 0'

        # assign self object
        self.__name = name
        self.price = item_price
        self.quantity = item_quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):     # property decorator: read only attribute
        # print('Property decorator is used here.')
        return self.__name
    @name.setter
    def name(self, new_name):
        print('name setter is used')
        if len(new_name) > 15:
            raise Exception('The new name is too long! (greater than 15 characters)')
        else:
            self.__name = new_name
    
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
    
    @property
    def read_only_name(self):
        return 'AABBCCabc'

