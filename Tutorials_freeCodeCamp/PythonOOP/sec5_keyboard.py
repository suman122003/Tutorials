from sec5_item import Item

class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self, name: str, item_price: float, item_quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, item_price, item_quantity)

