from items import Item
from perishable_item import PerishableItem
from electronic_item import ElectronicItem
from inventory import Inventory

print("Welcome to the Inventory Management System")
MENU = """-----INVENTORY SYSTEM-----
      1. Add Item
      2. Restock Item
      3. Sell Item
      4. Search Item
      5. Display all Items
      6. Total Inventory Value
      7. Exit"""    


store = Inventory()

def get_float(prompt, default=0.0):
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return default
        try:
            return float(raw)
        except ValueError:
            print(" Please enter a valid number.")


def get_int(prompt, default=0):
     while True:
        raw = input(prompt).strip()
        if raw == "":
            return default
        try:
            return int(raw)
        except ValueError:
            print(" Please enter a whole number.")

def add_item_menu():
    print("\nItem types: [1] Basic  [2] Perishable  [3] Electronic")
    item_type = input("Choose item type (1-3): ").strip()
 
    if item_type not in ("1", "2", "3"):
        print(" Invalid item type. Item not added.")
        return
 
    name = input("Item name: ").strip()
    if not name:
        print(" Item name cannot be empty. Item not added.")
        return
 
    quantity = get_int("Initial quantity (or press Enter for 0): ", 0)
    if quantity < 0:
        print(" Quantity cannot be negative. Using 0 instead.")
        quantity = 0
 
    price = get_float("Price per unit (or press Enter for 0): ", 0.0)
    if price < 0:
        print(" Price cannot be negative. Using 0 instead.")
        price = 0.0
 
    if item_type == "1":
        item = Item(name, quantity, price)
 
    elif item_type == "2":
        days = get_int("Days until expiry (or press Enter for 0): ", 0)
        if days < 0:
            print(" Days cannot be negative. Using 0 instead.")
            days = 0
        item = PerishableItem(name, quantity, price, days)
 
    else:  # "3"
        warranty = get_int("Warranty period in months (or press Enter for 0): ", 0)
        if warranty < 0:
            print(" Warranty cannot be negative. Using 0 instead.")
            warranty = 0
        item = ElectronicItem(name, quantity, price, warranty)
 
    store.add_item(item)
 
 
def restock_menu():
    name = input("Item name to restock: ").strip()
    qty = get_int("Quantity to add: ", None)
    if qty is None:
        print(" Restock cancelled.")
        return
    item = store.search(name)
    if item is None:
        print(f" No item named '{name}' found.")
        return
    item.restock(qty)
 
 
def sell_menu():
    name = input("Item name to sell: ").strip()
    qty = get_int("Quantity to sell: ", None)
    if qty is None:
        print(" Sale cancelled.")
        return
    item = store.search(name)
    if item is None:
        print(f" No item named '{name}' found.")
        return
    item.sell(qty)
 
 
def search_menu():
    name = input("Item name to search for: ").strip()
    item = store.search(name)
    if item is None:
        print(f" No item named '{name}' found.")
    else:
        print(" Found:")
        item.display()
 
 
def display_all_menu():
    store.display_all()
 
 
def total_value_menu():
    total = store.total_inventory_value()
    print(f" Total inventory value: ₱{total:,.2f}")
 
 
def main():
    print("Welcome to the Inventory System!")
 
    actions = {
        "1": add_item_menu,
        "2": restock_menu,
        "3": sell_menu,
        "4": search_menu,
        "5": display_all_menu,
        "6": total_value_menu,
    }
 
    while True:
        print(MENU)
        choice = input("Choose an option (1-7): ").strip()
 
        if choice == "7":
            print("Thank you for using the Inventory System. Goodbye!")
            break
 
        action = actions.get(choice)
        if action is None:
            print(" Invalid option. Please choose a number from 1 to 7.")
            continue
 
        try:
            action()
        except Exception as error:
                print(f" Something went wrong, but the program will continue: {error}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
    except EOFError:
        print("\n\nNo more input received. Goodbye!")