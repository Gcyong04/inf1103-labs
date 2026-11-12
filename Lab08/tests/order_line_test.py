from entity import PhysicalProduct, DigitalProduct
from entity.supplier import Supplier
from entity.order import Order
from inventory import Inventory

supplier = Supplier(supplier_id="S001", name="TechSource Pte Ltd", contact_email="contact@techsource.com")
laptop = PhysicalProduct(product_id="P001", name="Laptop", price=1500.00, stock=10, supplier=supplier, weight=2.1)
ebook = DigitalProduct(product_id="D001", name="Python eBook", price=25.00, stock=999, supplier=supplier, download_size=5.4)

# Product also lives in an Inventory (independent of orders)
inventory = Inventory()
inventory.add_product(laptop)

# Order 1: add two products
order1 = Order("O001")
order1.add_order_line(laptop, 2)
order1.add_order_line(ebook, 3)

print("Order 1 lines:")
for line in order1.order_lines:
    print(" ", line)
print("Order 1 total:", order1.calculate_total())     # 2*1500 + 3*25 = 3075.0

# Order 2: same Product, different Order
order2 = Order("O002")
order2.add_order_line(laptop, 1)

# Check the prediction
line1 = order1.order_lines[0]
line2 = order2.order_lines[0]
print("Same OrderLine object?", line1 is line2)                # False
print("Same Product object?", line1.product is line2.product)  # True
print("Product is the inventory's one too?",
      inventory.search_product("P001") is line1.product)         # True

# Remove a line through the Order
order1.remove_order_line("D001")
print("Order 1 lines after removal:", len(order1.order_lines))  # 1
print("Order 1 new total:", order1.calculate_total())           # 3000.0

# Product is unaffected
print("Ebook still exists:", ebook.name, ebook.price)

# Remove the whole Order from the scenario
del order1
print("Order 2 unaffected:", order2.calculate_total())          # 1500.0
print("Laptop still exists:", laptop.name)