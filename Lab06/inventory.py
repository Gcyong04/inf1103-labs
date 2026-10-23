from product import Product

class Inventory:

  # ---- Constructor ----
  def __init__(self):
    self.__products = []


  # ---- Methods ----
  def add_product(self, product: Product) -> None:
    pass


  def search_product(self, product_id: str) -> Product | None:
    """Search for product in inventory product list

    Args:
      product_id: the string product_id to search for

    Function:
      Takes string product_id input and searches through the inventory list 
      for product that exist with this ID

    Return:
      Product (if exists) or None
    """

    for product in self.__products:
      if product.get_product_id().lower() == product_id.lower():
        return product

    return None


  def display_all(self) -> list:
    pass