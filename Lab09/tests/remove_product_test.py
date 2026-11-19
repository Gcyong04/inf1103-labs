from entity import PhysicalProduct, DigitalProduct
from entity.supplier import Supplier
from inventory import Inventory

supplier = Supplier(supplier_id="S001", name="TechSource Pte Ltd", contact_email="contact@techsource.com")
laptop = PhysicalProduct(product_id="P001", name="Laptop", price=1500.00, stock=10, supplier=supplier, weight=2.1)
ebook = DigitalProduct(product_id="D001", name="Python eBook", price=25.00, stock=999, supplier=supplier, download_size=5.4)

inventory_a = Inventory()
inventory_b = Inventory()

# Add to A (both subtypes in the same list)
inventory_a.add_product(laptop)
inventory_a.add_product(ebook)
print("Found in A:", inventory_a.search_product("P001") is laptop)    # True

# Remove from A
print("Removed:", inventory_a.remove_product("P001"))               # True
print("Find after removal:", inventory_a.search_product("P001"))      # None
print("Remove again:", inventory_a.remove_product("P001"))          # False

# Product still works
print("Product still usable:", laptop.name, laptop.price, laptop.supplier.name)

# Same object added to B
inventory_b.add_product(laptop)
print("Found in B:", inventory_b.search_product("P001") is laptop)    # True

# Empty both inventories
inventory_a.remove_product("D001")
inventory_b.remove_product("P001")
print("Inventories empty:", len(inventory_a.products), len(inventory_b.products))  # 0 0
print("Products still exist:", laptop.name, "|", ebook.name)