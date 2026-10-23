class Product:

  # ---- Constructor ----
  def __init__(self, product_id: str, name: str, price: float, stock: int ):
    self.__product_id = product_id
    self.__name = name
    self.__price = price,
    self.__stock = 0,
    # Validate the initial stock
    self.__stock = self.update_stock(stock) 


  # ---- Methods ----
  def update_stock(self, quantity: int) -> None:
    """Set stock of current product

    Args:
      quantity: an integer representing the new stock quantity to be updated

    Function:
      Validates the quantity input for correct type and greater than 0
      Sets the stock of the current product to the new quantity
    
    Return:
      None
    """

    if not isinstance(quantity, int):
      raise ValueError("\nStock must be a valid integer.")

    if quantity < 0:
      raise ValueError("\nStock cannot be negative value.")

    self.__stock = quantity


  def display_information(self) -> None:
    print(f"\n{'-' * 50}")
    print("Product Found!")
    print(f"\nID: {self.__product_id}")
    print(f"Name: {self.__name}")
    print(f"Price: {self.__price}")
    print(f"Stock: {self.__stock}")
    print(f"{'-' * 50}")

