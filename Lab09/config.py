PRODUCT_TYPES = {
  "physical": "physical",
  "digital": "digital"
}

COMMON_FIELDS = ("type", "product_id", "name", "price", "stock", "supplier")
DEFAULT_EXTRA_FIELDS = {
  PRODUCT_TYPES["physical"]: {"weight": 0.0},
  PRODUCT_TYPES["digital"]: {"download_size": 0.0},
}

JSON_INVENTORY_FILE = "inventory.json"
CSV_PRODUCTS_FILE = "products.csv"