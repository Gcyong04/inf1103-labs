from abc import ABC, abstractmethod
from .supplier import Supplier

class Product(ABC):

  # ---- Constructor ----
  def __init__(self, type: str ,product_id: str, name: str, price: float, stock: int, supplier: Supplier):
    self.__type = type
    self.__product_id = product_id
    self.__name = name
    self.__price = price
    self.__stock = stock
    self.__supplier = supplier


  # ---- Methods ----
  @property
  def type(self) -> str:
    return self.__type
  
  @property
  def product_id(self) -> str:
    return self.__product_id

  @property
  def name(self) -> str:
    return self.__name

  @property
  def price(self) -> float:
    return self.__price

  @property
  def stock(self) -> int:
    return self.__stock

  @property
  def supplier(self) -> Supplier:
    return self.__supplier

  def to_dict(self) -> dict:
    return {
      "type": self.__type,
      "product_id": self.__product_id,
      "name": self.__name,
      "price": self.__price,
      "stock": self.__stock,
    }

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
      raise ValueError("Stock must be a valid integer!")

    if quantity < 0:
      raise ValueError("Stock cannot be negative value!")

    self.__stock = quantity


  def display_information(self) -> None:
    print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}", end="")


  @abstractmethod
  def get_fufilment_info(self) -> str:
    pass

