class Item:

    def __init__(self, name, quantity=0, price=0.0):
        self.name = name
        self.quantity = 0
        self.price = 0.0

        self._set_price(price)
        if quantity > 0:
           self.restock(quantity)


    # Private
    def _get_quantity(self):
        return self._get_quantity

    def _set_quantity(self, value):
        self.__quantity =  value

    def _get_price(self):
        return self._price

    def _set_price(self, value):
        try:
            value = float(value)
        except (TypeError, ValueError):
            value = 0.0
        self.__price = value if value >= 0 else 0.0

    # Public

    def restock(self, qty):
        try:
            qty = int(qty)
        except (TypeError, ValueError):
            print("Invalid quantity. Quantity must be a non-negative integer.")
            return False

        if qty < 0:
            print("Restock Failed! Quantity must be a non-negative integer.")
            return False

        self.__quantity += qty
            print(f"Restock Successful! New quantity of {self.name}: {self.__quantity}")