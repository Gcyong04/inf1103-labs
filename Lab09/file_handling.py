from inventory import Inventory
from entity import Supplier
from config import JSON_INVENTORY_FILE, COMMON_FIELDS, DEFAULT_EXTRA_FIELDS
from factory import ProductFactory
import json
import csv

class FileHandling:

  def __init__(self, inventory: Inventory):
    self.__inventory: Inventory = inventory


  def load_json(self) -> None:
    try:
      with open(JSON_INVENTORY_FILE, "r") as file:
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

    print(f"\nLoaded {loaded} product(s) from {JSON_INVENTORY_FILE} to inventory.")

  def save(self) -> None:
    print("\nSaving inventory to file...")
    with open(JSON_INVENTORY_FILE, "w") as file:
      json.dump([p.to_dict() for p in self.__inventory.products], file, indent=4)
    print("\nInventory saved successfully.")


  def load_csv(self, path: str, supplier: Supplier) -> None: 
    loaded = 0
    try:
      file = open(path, "r", newline="")
    except FileNotFoundError:
      print(f"\nProducts file not found: {path}")
    else:
      with file:
        reader = csv.reader(file)
        next(reader, None)  # skip the header row
        for row in reader:
          if not row:
            continue
          try:
            product_type, product_id, name, price, stock = row
            extra = DEFAULT_EXTRA_FIELDS.get(product_type, {})
            product = ProductFactory.create(product_type, product_id=product_id, name=name, price=float(price), stock=int(stock), supplier=supplier, **extra)
            self.__inventory.add_product(product)
          except ValueError as err:
            print(f"\nSkipped line {reader.line_num} {row}: {err}")
          else:
            loaded += 1

      print(f"\n{loaded} products loaded.")
    finally:
      print("Load attempt finished.")