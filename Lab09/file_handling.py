from inventory import Inventory
from entity import Supplier
from config import INVENTORY_FILE, COMMON_FIELDS
from factory import ProductFactory
import json

class FileHandling:

  def __init__(self, inventory: Inventory, filename: str = INVENTORY_FILE):
    self.__inventory: Inventory = inventory
    self.__filename: str = filename


  def load(self) -> None:
    try:
      with open(self.__filename, "r") as file:
        data = json.load(file)
    except (FileNotFoundError, ValueError) as err:
      print(f"\nCould not load file: {err}")
      return

    loaded = 0
    for item in data:
      try:
        info = item["supplier"]
        supplier = Supplier(supplier_id=info["supplier_id"], name=info["name"], contact_email=info["contact_email"])

        extra = {key: value for key, value in item.items() if key not in COMMON_FIELDS}

        product = ProductFactory.create(item["type"], product_id=item["product_id"], name=item["name"], price=item["price"], stock=item["stock"], supplier=supplier, **extra)

        self.__inventory.add_product(product)
        loaded += 1
      except (KeyError, ValueError, TypeError) as err:
        print(f"\nSkipped {item.get('product_id', '?')}: missing or invalid data ({err})")

    print(f"\nLoaded {loaded} product(s) from {self.__filename} to inventory.")

  def save(self) -> None:
    print("\nSaving inventory to file...")
    with open(self.__filename, "w") as file:
      json.dump([p.to_dict() for p in self.__inventory.products], file, indent=4)
    print("\nInventory saved successfully.")