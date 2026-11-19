from entity import DigitalProduct, PhysicalProduct
from entity.supplier import Supplier
from entity.order import Order
from inventory import Inventory
from file_handling import FileHandling


# ---- Prompt/Display Functions ----
def display_menu() -> None:
  print(f"\n{'-' * 10} MENU {'-' * 10}")
  print("1. Display all products")
  print("2. Add product")
  print("3. Update stock")
  print("4. Search product")
  print("5. Save inventory")
  print("6. Remove product")
  print("7. Create order")
  print("8. Exit")
  print(f"{'-' * 26}")

def prompt_non_empty_str(prompt: str) -> str:
  while True:
    text = input(prompt).strip()
    if text:
      return text
    print("\nInput cannot be empty!")

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


# ---- Helper Functions ----
def prompt_supplier() -> Supplier:
  supplier_id = prompt_non_empty_str("Supplier ID: ")
  name = prompt_non_empty_str("Supplier name: ")
  contact_email = prompt_non_empty_str("Supplier Contact Email: ")
  return Supplier(supplier_id=supplier_id, name=name, contact_email=contact_email)


# ---- Menu Action Functions ----
def menu_add_product(inventory: Inventory) -> None:
  weight: float = 0
  download_size: float = 0

  print("\nAdd a new product\n")
  print("1. Physical product")
  print("2. Digital product")
  choice = input("\nSelect product type: ").strip()

  if choice not in ("1", "2"):
    print("\nInvalid Choice!")
    return

  product_id = prompt_non_empty_str("Product ID: ")
  name = prompt_non_empty_str("Product Name: ")
  price = prompt_float("Price: ")
  stock = prompt_int("Stock: ")
  if choice == "1":
    weight = prompt_float("Weight: ")
  elif choice == "2":
    download_size = prompt_float("Download Size: ")

  print("\nSupplier details")
  supplier = prompt_supplier()

  try:
    if choice == "1":
      inventory.add_product(PhysicalProduct(product_id=product_id, name=name, price=price, stock=stock, supplier=supplier, weight=weight))
    elif choice == "2":
      inventory.add_product(DigitalProduct(product_id=product_id, name=name, price=price, stock=stock, supplier=supplier, download_size=download_size))
    print("\nProduct added successfully.")
  except Exception as err:
    print(f"\nFailed to add product: {err}")


def menu_update_stock(inventory: Inventory) -> None:
  product = inventory.search_product(prompt_non_empty_str("Product ID: "))
  if product is None:
    print("\nProduct not found.")
    return
  new_stock = prompt_int("New stock quantity: ")
  try:
    product.update_stock(new_stock)
    print(f"\nStock quantity updated successfully for {product.product_id}")
  except ValueError as err:
    print(f"\nFailed to update stock quantity: {err}")


def menu_search_product(inventory: Inventory) -> None:
  product = inventory.search_product(prompt_non_empty_str("Product ID: "))
  if product is None:
    print("\nProduct not found.")
  else:
    print(f"\n{'-' * 60}")
    print("Product Found\n")
    product.display_information()
    print(product.get_fulfilment_info())
    print("\nSupplier")
    product.supplier.display_information()
    print(f"{'-' * 60}")


def menu_remove_product(inventory: Inventory) -> None:
  product_id = prompt_non_empty_str("Product ID: ")
  if inventory.remove_product(product_id):
    print(f"\nProduct {product_id} removed from inventory.")
  else:
    print("\nProduct not found.")


def menu_create_order(inventory: Inventory, orders: list[Order]) -> None:
  order_id = prompt_non_empty_str("Order ID: ")
  if any(order.order_id.lower() == order_id.lower() for order in orders):
    print(f"\nOrder with ID ({order_id}) already exists!")
    return

  order = Order(order_id=order_id)
  print("\nAdd products to the order (leave Product ID blank to finish)")

  while True:
    product_id = input("\nProduct ID: ").strip()
    if product_id == "":
      break

    product = inventory.search_product(product_id)
    if product is None:
      print("Product not found.")
      continue

    quantity = prompt_int("Quantity: ")
    if quantity <= 0:
      print("Quantity must be greater than 0.")
      continue

    order.add_order_line(product=product, quantity=quantity)  # Order creates the OrderLine itself
    print(f"Added {quantity} x {product.name}")

  if not order.order_lines:
    print("\nNo items added, order not created.")
    return

  orders.append(order)

  print(f"\n{'-' * 60}")
  print(f"Order {order.order_id}\n")
  for line in order.order_lines:
    print(f"{line.product.name} x{line.quantity} @ ${line.product.price:.2f} = ${line.calculate_subtotal():.2f}")
  print(f"\nTotal: ${order.calculate_total():.2f}")
  print("-" * 60)


def main():

  # Create new inventory class instance and load inventory from file into instance
  inventory = Inventory()
  orders: list[Order] = []
  file_handler = FileHandling(inventory=inventory)
  file_handler.load()

  while True:
    display_menu()
    choice = prompt_non_empty_str("Select an option (1-8): ")
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
        menu_remove_product(inventory=inventory)
      case "7":
        menu_create_order(inventory=inventory, orders=orders)
      case "8":
        file_handler.save()
        print("\nThank you for using Inventory Management System!")
        print("Program terminated.")
        break
      case _:
        print("\nPlease select a valid option!")


if __name__ == "__main__":
  main()