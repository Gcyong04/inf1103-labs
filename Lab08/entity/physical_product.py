from .product import Product
from .supplier import Supplier
from interface import CanBeShipped
from config import PRODUCT_TYPES

class PhysicalProduct(Product, CanBeShipped):

  # ---- Constructor ----
  def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier, type: str = PRODUCT_TYPES["physical"]):
    super().__init__(type, product_id, name, price, stock, supplier)
    self.__weight = weight


  # ---- Methods ----
  def display_information(self) -> str:
    super().display_information()
    print(f" | Weight: {self.__weight} kg")


  def to_dict(self):
    data = super().to_dict()
    data["weight"] = self.__weight
    return data


  def get_fufilment_info(self) -> str:
    return "This product requires physical shipping."


  def calculate_shipping_cost(self) -> float:
    return self.__weight * 1.50