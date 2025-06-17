from sec4_item import Item

class Phone(Item):
    def __init__(self, name: str, item_price: float, item_quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, item_price, item_quantity)

        # Validations of arguments
        assert broken_phones >= 0, f'Broken phones {broken_phones} is not greater than or equal to 0'

        # assign self object
        self.broken_phones = broken_phones

