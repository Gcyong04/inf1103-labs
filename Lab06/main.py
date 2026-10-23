import json
import os

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
  with open(INVENTORY_FILE, "w") as file:
    json.dump([p.to_dict() for p in inventory.get_products()], file, indent=4)
  print("\nInventory saved successfully")

def main():
  pass

if __name__ == "__main__":
  main() 