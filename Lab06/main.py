import json

from product import Product
from inventory import Inventory

INVENTORY_FILE = "inventory.json"

# ---- File Handling ----
def load_inventory(inventory: Inventory) -> None:
  try:
    with open(INVENTORY_FILE, "r") as file:
      data = json.load(file)
    for item in data:
      inventory.add_product(Product(item["product_id"], item["name"], item["price"], item["stock"]))
    print(f"\nLoaded {len(data)} product(s) from {INVENTORY_FILE} to inventory.")
  except (FileNotFoundError, KeyError, ValueError, TypeError) as err:
    print(f"\nCould not load file: {err}")


def save_inventory(inventory: Inventory) -> None:
  print("\nSaving inventory to file...")
  with open(INVENTORY_FILE, "w") as file:
    json.dump([p.to_dict() for p in inventory.get_products()], file, indent=4)
  print("\nInventory saved successfully.")


# ---- Prompt/Display Functions ----
def display_menu():
  print(f"\n{'-' * 10} MENU {'-' * 10}")
  print("1. Display all products")
  print("2. Add product")
  print("3. Update stock")
  print("4. Search product")
  print("5. Save inventory")
  print("6. Exit")
  print(f"{'-' * 26}")


def prompt_int(prompt: str) -> int:
  while True:
    try:
      return int(input(prompt).strip())
    except ValueError:
      print("\nPlease enter a valid integer!")


def prompt_float(prompt: str) -> float:
  while True:
    try:
      return float(input(prompt).strip())
    except ValueError:
      print("\nPlease enter a valid number!")


# ---- Menu Action Functions ----
def menu_add_product(inventory: Inventory) -> None:
  print("\nAdd a new product\n")
  product_id = input("Product ID: ").strip()
  name = input("Name: ").strip()
  price = prompt_float("Price: ")
  stock = prompt_int("Stock: ")

  try:
    inventory.add_product(Product(product_id=product_id, name=name, price=price, stock=stock))
    print("\nProduct added sucessfully.")
  except ValueError as err:
    print(f"\nFailed to add product: {err}")


def menu_update_stock(inventory: Inventory) -> None:
  product = inventory.search_product(input("Product ID: ").strip())
  if product is None:
    print("\nProduct not found.")
    return
  new_stock = prompt_int("New stock quantity: ")
  try:
    product.update_stock(new_stock)
    print(f"\nStock quantity updated successfully for {product.get_product_id()}")
  except ValueError as err:
    print(f"\nFailed to update stock quantity: {err}")


def menu_search_product(inventory: Inventory):
  product = inventory.search_product(input("Product ID: ").strip())
  if product is None:
    print("\nProduct not found.")
  else:
    print(f"\n{'-' * 60}")
    print("Product Found\n")
    product.display_information()
    print(f"{'-' * 60}")

def main():

  # Create new inventory class instance and load inventory from file into instance
  inventory = Inventory()
  load_inventory(inventory)

  while True:
    display_menu()
    choice = input("Select an option (1-6): ").strip()
    match choice:
      case "1":
        inventory.display_all()
      case "2":
        menu_add_product(inventory=inventory)
      case "3":
        menu_update_stock(inventory=inventory)
      case "4":
        menu_search_product(inventory=inventory)
      case "5":
        save_inventory(inventory=inventory)
      case "6":
        save_inventory(inventory=inventory)
        print("\nThank you for using Inventory Management System!")
        print("Program terminated.")
        break
      case _:
        print("\nPlease select a valid option!")



if __name__ == "__main__":
  main() 