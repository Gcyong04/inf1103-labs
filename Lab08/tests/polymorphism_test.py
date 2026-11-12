from entity import PhysicalProduct, DigitalProduct
from entity.supplier import Supplier
from inventory import Inventory

supplier = Supplier(supplier_id="S001", name="TechSource Pte Ltd", contact_email="contact@techsource.com")
laptop = PhysicalProduct(product_id="P001", name="Laptop", price=1500.00, stock=10, supplier=supplier, weight=2.1)
ebook = DigitalProduct(product_id="D001", name="Python eBook", price=25.00, stock=999, supplier=supplier, download_size=5.4)
phone = PhysicalProduct(product_id="P002", name="Phone", price=900.00, stock=20, supplier=supplier, weight=0.2)

inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(ebook)
inventory.add_product(phone)

# One loop, one collection, no isinstance()
for product in inventory.products:
  product.display_information()
  print(product.get_fulfilment_info())
  print()