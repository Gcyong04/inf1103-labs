from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from file_handling import FileHandling


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
  weight = 0
  download_size = 0

  print("\nAdd a new product\n")
  print("1. Physical product")
  print("2. Digital product")
  choice = input("\nSelect product type: ").strip()

  if choice != "1" and choice != "2":
    print("\nInvalid Choice!")
    return

  product_id = input("Product ID: ").strip()
  name = input("Name: ").strip()
  price = prompt_float("Price: ")
  stock = prompt_int("Stock: ")
  if choice == "1":
    weight = prompt_float("Weight: ")
  elif choice == "2":
    download_size = prompt_float("Download Size: ")
  
  try:
    if choice == "1":
      inventory.add_product(PhysicalProduct(product_id=product_id, name=name, price=price, stock=stock, weight=weight))
    elif choice == "2":
      inventory.add_product(DigitalProduct(product_id=product_id, name=name, price=price, stock=stock, download_size=download_size))
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
    print(f"\nStock quantity updated successfully for {product.product_id}")
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
  file_handler = FileHandling(inventory=inventory)
  file_handler.load()

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
        file_handler.save()
      case "6":
        file_handler.save()
        print("\nThank you for using Inventory Management System!")
        print("Program terminated.")
        break
      case _:
        print("\nPlease select a valid option!")



if __name__ == "__main__":
  main() 