from items import Item

EXPIRY_THRESHOLD_DAYS = 3
DISCOUNT_RATE = 0.10 


class Perishable_item(Item):

    def __init__(self, name, quantity=0, price=0.0, expiry_date=None):
        super().__init__(name, quantity, price)
        try:
            self.expiry_date = int(expiry_date)
        except (TypeError, ValueError):
            self.expiry_date = None

    def is_expiring_soon(self):
        return self.expiry_date is not None and self.expiry_date <= EXPIRY_THRESHOLD_DAYS

    def total_value(self):
        base_value = self._get_quantity() * self._get_price()
        if self.is_expiring_soon():
            return base_value * (1 - DISCOUNT_RATE)
        return base_value

    def display(self):
        status = " (EXPIRING SOON - discounted)" if self.is_expiring_soon() else ""
        print(f" {self.name:<20} qty: {self._get_quantity():<6} "
              f"price: ${self._get_price():,.2f}  "
              f"expires in: {self.days_until_expiry} day(s){status}  "
              f"total value: ${self.total_value():,.2f}")