from product import Product
from config import PRODUCT_TYPES

class DigitalProduct(Product):

  # ---- Constructor ----
  def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, type: str = PRODUCT_TYPES["digital"]):
    super().__init__(type, product_id, name, price, stock)
    self.__download_size = download_size


  # ---- Methods ----
  def display_information(self) -> str:
    super().display_information()
    print(f" | Download Size: {self.__download_size} MB")


  def to_dict(self):
    data = super().to_dict()
    data["download_size"] = self.__download_size
    return data


  def get_fufilment_info(self) -> str:
    return "This product is delivered digitally"