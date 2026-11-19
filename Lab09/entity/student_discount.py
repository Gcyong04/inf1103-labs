from .percentage_discount import PercentageDiscount

class StudentDiscount(PercentageDiscount):
  """Takes 5% off on the total, since it is a discount with percentage, can reuse PercentageDiscount class"""

  def __init__(self):
    super().__init__(5)