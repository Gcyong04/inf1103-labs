from product import Product

class Inventory:

  # ---- Constructor ----
  def __init__(self):
    self.__products = []


  # ---- Methods ----
  def add_product(self, product: Product) -> None:
    """Append new product to inventory list

    Args:
      product: The new product to be added, an object that conforms to Product class

    Function:
      Validates the product object conforms to Product class and check
      that the product ID does not exist in the inventory list
      Append new product into inventory list if validations passed

    Return:
      None
    """

    if not isinstance(product, Product):
      raise TypeError("Input does not conform to Product class")

    if self.search_product(product_id=product.get_product_id()) is not None:
      raise ValueError(f"Product with ID ({product.get_product_id()}) already exists")

    self.__products.append(product)


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