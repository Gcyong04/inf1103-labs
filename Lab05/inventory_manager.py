import json

# Global Constants
INVENTORY_FILE = "inventory.json"

# Load inventory from file to list
def load_inventory():
  # Initialise variables
  inventory = []

  # Try open file and read, print error if file does not exists
  try:
    with open(INVENTORY_FILE, "r") as file:
      inventory = json.load(file)
    print("\ninventory.json found.\nInventory loaded successfully")
    return inventory
  except FileNotFoundError:
    print("JSON file does not exists")
    return []


# Display all items in current inventory
def display_all(inventory):
  print("\nCurrent Inventory")
  print("--------------------------------------------------------------------------------")
  if not inventory:
    print("\nNo products in inventory\n")
  else:
    for item in inventory:
      print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']} | Stock: {item['stock']}")
  print("--------------------------------------------------------------------------------")


# Search for product by ID
def search_product(inventory, product_id):
  for product in inventory:
    if product['id'].upper() == product_id.upper():
      return product

  return None


# Validate stock quantity input is an int
def get_valid_stock_quantity(prompt):
  while True:
    try:
      stock_quantity = int(input(f"{prompt}: ").strip())
      if stock_quantity < 0:
        print("Invalid stock quantity, cannot be negative")
        continue
      return stock_quantity
    except ValueError:
      print("Invalid stock quantity, please enter a valid integer")


# Validate price input is correct format
def get_valid_price():
  while True:
    try:
      price = float(input(f"Price: ").strip())
      if price < 0:
        print("Invalid price, cannot be negative")
        continue
      return round(price, 2)
    except ValueError:
      print("Invalid price, please enter a valid number")


# Input and validation for new product to be added
def get_valid_new_product():
  print("\nAdd new product")
  product_id = input("Product ID: ").strip().upper()
  product_name = input("Product Name: ").strip()
  product_price = get_valid_price()
  product_stock = get_valid_stock_quantity("Stock Quantity")

  return {
    "id": product_id,
    "name": product_name,
    "price": product_price,
    "stock": product_stock
  }


# Add new product to inventory list
def add_product(inventory, new_product):
  existing_product = search_product(inventory, new_product['id'])
  if existing_product:
    print("\nProduct with ID already exists in database")
    return False
  inventory.append(new_product)
  return True


# Update stock of existing product in inventory list
def update_stock(inventory, product_id, new_stock):
  product = search_product(inventory, product_id)
  if product is None:
    print("\nProduct not found, please select action and enter valid ID")
    return False
  product['stock'] = new_stock
  return True


# Save inventory list into json file
def save_inventory(inventory):
  with open(INVENTORY_FILE, "w") as file:
    json.dump(inventory, file, indent=4)


# Display select menu options and get valid user input
def get_valid_menu_option():
  while True:
    print("\n------------------------------------- MENU -------------------------------------")
    print("1. Display all products")
    print("2. Add product")
    print("3. Update stock")
    print("4. Search product")
    print("5. Save inventory")
    print("6. Exit")
    print("--------------------------------------------------------------------------------")

    try:
      choice = int(input("Enter option: ").strip())
      if choice <= 0 or choice > 6:
        print("\nInvalid option, please select a valid option from menu")
        continue
      return choice
    except ValueError:
      print("\nInvalid option, please select a valid option from menu")


# Program Entry Point
def main():
  # Initialise variables
  inventory = []

  inventory = load_inventory()

  while True:
    selected_action = get_valid_menu_option()

    # Display all inventory
    if selected_action == 1:
      display_all(inventory)

    # Add product
    elif selected_action == 2:
      new_product = get_valid_new_product()
      add_status = add_product(inventory, new_product)
      if add_status:
        print("\nProduct added successfully")
      else:
        print("\nFailed to add product, please select action and try again")

    # Update stock 
    elif selected_action == 3:
      product_id = input("Enter product ID: ").strip()
      new_stock = get_valid_stock_quantity("Enter new stock quantity")
      update_status = update_stock(inventory, product_id, new_stock)
      if update_status:
        print("\nProduct stock updated successfully")
      else:
        print("Failed to update product stock, please select action and try again")

    # Search product
    elif selected_action == 4:
      product_id = input("Enter product ID: ").strip()
      product = search_product(inventory, product_id)
      if product is None:
        print("\nProduct not found.")
        continue
      print("\nProduct Found")
      print("--------------------------------------------------------------------------------")
      print(f"ID: {product['id']}")
      print(f"Name: {product['name']}")
      print(f"Price: ${product['price']}")
      print(f"Stock: {product['stock']}")
      print("--------------------------------------------------------------------------------")

    # Save inventory
    elif selected_action == 5:
      print("\nSaving inventory...")
      save_inventory(inventory)
      print("Inventory saved successfully")

    # Save and exit
    elif selected_action == 6:
      print("\nSaving inventory before exit...")
      save_inventory(inventory)
      print("\nInventory saved successfully")
      break

if __name__ == "__main__":
  main()