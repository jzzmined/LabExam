from items import Item

class ElectronicItem(Item):
    def __init__(self, name, quantity=0, price=0.0, warranty_period=0):
        super().__init__(name, quantity, price)
        try:
            self.warranty_period = int(warranty_period)
        except (TypeError, ValueError):
            self.warranty_period = 0

    def display(self):
        print(f" {self.name:<20} qty: {self._get_quantity():<6} "
              f"price: ₱{self._get_price():,.2f}  "
              f"warranty: {self.warranty_period} month(s)  "
              f"total value: ₱{self.total_value():,.2f}")