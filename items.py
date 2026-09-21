class Item:

    def __init__(self, name, quantity=0, price=0.0):
        self.name = name
        self.__quantity = 0
        self.__price = 0.0

        self._set_price(price)
        if quantity > 0:
           self.restock(quantity)


    # Private
    def _get_quantity(self):
        return self.__quantity

    def _set_quantity(self, value):
        self.__quantity =  value

    def _get_price(self):
        return self.__price

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
        return True

    def sell(self, qty):
        try:
            qty = int(qty)
        except (TypeError, ValueError):
            print("Invalid quantity. Quantity must be a non-negative integer.")
            return False

        if qty <= 0:
            print("Sale Failed! Quantity must be a positive integer.")
            return False

        if qty > self.__quantity:
            print(f"Sale Failed! Not enough {self.name} in stock.")
            return False

        self.__quantity -= qty
        print(f"Sale Successful! New quantity of {self.name}: {self.__quantity}")
        return True

    def total_value(self):
        return self.__quantity * self.__price

    def display(self):
        print(f" {self.name:<20} Qty: {self.__quantity:<6} "
              f"Price: ₱{self.__price:,.2f}  "
              f"Total Value: ₱{self.total_value():,.2f}")

    def __str__(self):
        return (f"{self.__class__.__name__}({self.name}, "
                f"Qty={self.__quantity}, price=₱{self.__price:,.2f})")