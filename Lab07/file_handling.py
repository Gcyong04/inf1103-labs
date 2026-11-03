from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from config import INVENTORY_FILE, PRODUCT_TYPES
import json

class FileHandling:

  def __init__(self, inventory: Inventory, filename: str = INVENTORY_FILE):
    self.__inventory = inventory
    self.__filename = filename


  def load(self) -> None:
    try:
      with open(self.__filename, "r") as file:
        data = json.load(file)
      for item in data:
        if item["type"] == PRODUCT_TYPES["physical"]:
          self.__inventory.add_product(PhysicalProduct(product_id=item["product_id"], name=item["name"], price=item["price"], stock=item["stock"], weight=item["weight"]))
        elif item["type"] == PRODUCT_TYPES["digital"]:
          self.__inventory.add_product(DigitalProduct(product_id=item["product_id"], name=item["name"], price=item["price"], stock=item["stock"], download_size=item["download_size"]))
      print(f"\nLoaded {len(data)} product(s) from {INVENTORY_FILE} to inventory.")
    except (FileNotFoundError, KeyError, ValueError, TypeError) as err:
      print(f"\nCould not load file: {err}")

  def save(self) -> None:
    print("\nSaving inventory to file...")
    with open(self.__filename, "w") as file:
      json.dump([p.to_dict() for p in self.__inventory.get_products()], file, indent=4)
    print("\nInventory saved successfully.")