from entity import PhysicalProduct, DigitalProduct
from entity.product import Product
from entity.supplier import Supplier
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier(supplier_id="S001", name="TechSource Pte Ltd", contact_email="contact@techsource.com")
laptop = PhysicalProduct(product_id="P001", name="Laptop", price=1500.00, stock=10, supplier=supplier, weight=2.1)
ebook = DigitalProduct(product_id="D001", name="Python eBook", price=25.00, stock=999, supplier=supplier, download_size=5.4)

show_product_details(laptop)
show_product_details(ebook)

inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(ebook)
inventory.display_all()   # or display_all_products() if you renamed it
print(inventory.search_product("D001") is ebook)   # True

# The same Product operation works on both subtypes
for p in (laptop, ebook):
    p.update_stock(5)
    print(p.name, p.stock)                       # 5 for each

inventory.remove_product("P001")
print(len(inventory.products))                   # 1