from product import Product

class DigitalProduct(Product):

  # ---- Constructor ----
  def __init__(self, product_id, name, price, stock, download_size: float):
    super().__init__(product_id, name, price, stock)
    self.__download_size = download_size


  # ---- Methods ----
  def display_information(self) -> str:
    super().display_information()
    print(f" | Download Size: {self.__download_size} MB")


  def get_fufilment_info(self) -> str:
    return "This product is delivered digitally"