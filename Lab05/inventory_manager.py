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
    print("inventory.json found.\nInventory loaded successfully")
    return inventory
  except FileNotFoundError:
    print("JSON file does not exists")
    return []


def main():
  # Initialise variables
  inventory = []

  inventory = load_inventory()

if __name__ == "__main__":
  main()