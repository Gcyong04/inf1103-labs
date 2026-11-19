from entity import Supplier, PhysicalProduct, DigitalProduct, Product
from config import PRODUCT_TYPES

class ProductFactory:

  @staticmethod
  def create(product_type: str, product_id: str, name: str, price: float, stock: int, supplier: Supplier, **extra) -> Product:
    if product_type == PRODUCT_TYPES["physical"]:
      return PhysicalProduct(product_id = product_id, name = name, price = price, stock = stock, supplier = supplier, **extra)
    elif product_type == PRODUCT_TYPES["digital"]:
      return DigitalProduct(product_id = product_id, name = name, price = price, stock = stock, supplier = supplier, **extra)
    else:
      raise ValueError(f"Unknown product type: {product_type}")