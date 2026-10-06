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

def main():
  # Initialise variables
  inventory = []

  inventory = load_inventory()

  while True:
    selected_action = get_valid_menu_option()

    if selected_action == 1:
      display_all(inventory)

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

    elif selected_action == 6:
      break

if __name__ == "__main__":
  main()