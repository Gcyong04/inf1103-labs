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



def main():

  # Create new inventory class instance and load inventory from file into instance
  inventory = Inventory()
  load_inventory(inventory)

  while True:
    display_menu()
    choice = input("Select an option (1-6): ").strip()
    match choice:
      case "1":
        break
      case "2":
        break
      case "3":
        break
      case "4":
        break
      case "5":
        break
      case "6":
        break
      case _:
        print("\nPlease select a valid option!")



if __name__ == "__main__":
  main() 