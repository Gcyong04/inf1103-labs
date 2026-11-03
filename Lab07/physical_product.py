from product import Product

class PhysicalProduct(Product):

  # ---- Constructor ----
  def __init__(self, product_id, name, price, stock, weight: float):
    super().__init__(product_id, name, price, stock)
    self.__weight = weight


  # ---- Methods ----
  def display_information(self) -> str:
    super().display_information()
    print(f" | Weight: {self.__weight} kg")


  def get_fufilment_info(self) -> str:
    return "This product requires physical shipping."