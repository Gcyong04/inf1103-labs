# Initialize inventory
inventory = 0

# Continuous loop for user input
while True:

  stock_quantity = input("Enter stock quantity (or type 'quit' to exit): ")

  # Exit loop if user quits
  if stock_quantity.lower() == "quit":
    break