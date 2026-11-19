from entity import PhysicalProduct
from entity.supplier import Supplier
from entity.order import Order
from entity.bulk_discount import BulkDiscount
from entity.percentage_discount import PercentageDiscount

supplier = Supplier(supplier_id="S1", name="Test Supplier", contact_email="s@test.com")
item_a = PhysicalProduct(product_id="P1", name="Item A", price=100.0, stock=10, supplier=supplier, weight=1.0)
item_b = PhysicalProduct(product_id="P2", name="Item B", price=50.0, stock=10, supplier=supplier, weight=1.0)

# Order whose lines add up to 250 (2 x 100 + 1 x 50)
order = Order(order_id="O1")
order.add_order_line(product=item_a, quantity=2)
order.add_order_line(product=item_b, quantity=1)

print(f"Total with no discount:        {order.calculate_total()}  (predicted 250)")

order.set_discount(BulkDiscount(200, 20))
print(f"Total with BulkDiscount(200, 20):  {order.calculate_total()}  (predicted 230)")

order.set_discount(PercentageDiscount(10))
print(f"Total after PercentageDiscount(10): {order.calculate_total()}  (predicted 225)")