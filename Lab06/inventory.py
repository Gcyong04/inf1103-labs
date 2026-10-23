from product import Product

class Inventory:

  # ---- Constructor ----
  def __init__(self):
    self.__products = []


  # ---- Methods ----
  def add_product(self, product: Product) -> None:
    pass


  def search_product(self, product_id: str) -> Product | None:
    pass


  def display_all(self) -> list:
    pass