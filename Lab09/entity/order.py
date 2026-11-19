from .order_line import OrderLine
from .product import Product
from .discount_strategy import DiscountStrategy
from .no_discount import NoDiscount

class Order:

  def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
    self.__order_id: str = order_id
    self.__order_lines: list[OrderLine] = []
    self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

  @property
  def order_id(self) -> str:
    return self.__order_id

  @property
  def order_lines(self) -> list[OrderLine]:
    return self.__order_lines

  @property
  def discount(self) -> DiscountStrategy:
    return self.__discount

  def add_order_line(self, product: Product, quantity: int) -> None:
    line = OrderLine(product=product, quantity=quantity)
    self.__order_lines.append(line)

  def remove_order_line(self, product_id: str) -> None:
    for line in self.__order_lines:
      if line.product.product_id == product_id:
        self.order_lines.remove(line)

  def set_discount(self, discount: DiscountStrategy) -> None:
    self.__discount = discount

  def calculate_total(self) -> float:
    total = sum(line.calculate_subtotal() for line in self.__order_lines)
    return self.__discount.apply(total = total)