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

# Display select menu options and get valid user input
def get_valid_menu_option():
  while True:
    print("------------------------------------- MENU -------------------------------------")
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
        print("Invalid option, please select a valid option from menu\n")
        continue
      return choice
    except ValueError:
      print("Invalid option, please select a valid option from menu\n")

def main():
  # Initialise variables
  inventory = []

  inventory = load_inventory()

  selected_action = get_valid_menu_option()

if __name__ == "__main__":
  main()