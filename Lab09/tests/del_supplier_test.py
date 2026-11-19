from entity import PhysicalProduct, DigitalProduct
from entity.supplier import Supplier

# Create the Supplier independently
supplier = Supplier(supplier_id="S001", name="TechSource Pte Ltd", contact_email="contact@techsource.com")

# Create products using that Supplier
laptop = PhysicalProduct(product_id="P001", name="Laptop", price=1500.00, stock=10, supplier=supplier, weight=2.1)
ebook = DigitalProduct(product_id="D001", name="Python eBook", price=25.00, stock=999, supplier=supplier, download_size=5.4)

# Display supplier info through each product
print("Before del:")
print(laptop.supplier.name)
print(ebook.supplier.name)

# Same object shared by both products?
print(laptop.supplier is ebook.supplier)   # True
print(laptop.supplier is supplier)         # True

# Delete the variable, not the object
del supplier

print("\nAfter del:")
print(laptop.supplier.name)   # still works
print(ebook.supplier.name)    # still works