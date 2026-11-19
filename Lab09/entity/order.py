from .order_line import OrderLine
from .product import Product

class Order:

  def __init__(self, order_id: str):
    self.__order_id: str = order_id
    self.__order_lines: list[OrderLine] = []

  @property
  def order_id(self) -> str:
    return self.__order_id

  @property
  def order_lines(self) -> list[OrderLine]:
    return self.__order_lines

  def add_order_line(self, product: Product, quantity: int) -> None:
    line = OrderLine(product=product, quantity=quantity)
    self.__order_lines.append(line)

  def remove_order_line(self, product_id: str) -> None:
    for line in self.__order_lines:
      if line.product.product_id == product_id:
        self.order_lines.remove(line)

  def calculate_total(self) -> float:
    return sum(line.calculate_subtotal() for line in self.__order_lines)