# Initialize inventory
inventory = 0

# Continuous loop for user input
while True:

  stock_quantity = input("Enter stock quantity (or type 'quit' to exit): ")

  # Exit loop if user quits
  if stock_quantity.lower() == "quit":
    break

  # Handle invalid string inputs and negative numbers
  if not stock_quantity.isdigit():
    print("Error: Please enter a valid positive integer.")
    continue

  # Convert stock quantity input from string to integer
  stock_quantity = int(stock_quantity)