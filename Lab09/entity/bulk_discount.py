from .discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):

  def __init__(self, threshold: float, amount: float):
    self.__threshold: float = threshold
    self.__amount: float = amount

  def apply(self, total: float) -> float:
    if total >= self.__threshold:
      return max(total - self.__amount, 0)
    return total