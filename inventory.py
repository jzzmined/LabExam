class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        if self.search(item.name) is not None:
            print(f"Item '{item.name}' already exists in the inventory.")
            return False

        self.items.append(item)
        print(f"Item '{item.name}' added to the inventory.")
        return True

    def update_quantity(self, item_name, quantity):
        item = self.search(item_name)
        if item is None:
            print(f"Item '{item_name}' not found in the inventory.")
            return False

        if quantity < 0:
            print("Quantity must be a non-negative integer.")
            return False

        item.restock(quantity)
        return True

    def search(self, item_name):
        if not item_name:
            return None
        target = item_name.strip().lower()
        for item in self.items:
            if item.name.strip().lower() == target:
                return item
        return None

    def display_all(self):
        print("\n--- Current Inventory ---")
        if not self.items:
            print(" (inventory is empty)")
        else:
            for item in self.items:
                item.display()
        print("-" * 60)

    def total_inventory_value(self):
        return sum(item.total_value() for item in self.items)