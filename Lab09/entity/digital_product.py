from .product import Product
from .supplier import Supplier
from config import PRODUCT_TYPES

class DigitalProduct(Product):

  # ---- Constructor ----
  def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float, type: str = PRODUCT_TYPES["digital"]):
    super().__init__(type=type, product_id=product_id, name=name, price=price, stock=stock, supplier=supplier)
    self.__download_size: float = download_size


  # ---- Methods ----
  def display_information(self) -> None:
    super().display_information()
    print(f" | Download Size: {self.__download_size} MB")


  def to_dict(self) -> dict:
    data = super().to_dict()
    data["download_size"] = self.__download_size
    return data


  def get_fulfilment_info(self) -> str:
    return "This product is delivered digitally"