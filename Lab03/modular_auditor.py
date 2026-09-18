# Initialize inventory
inventory = 0

#Initialize failed/rejected entries
failed_entries = 0

# Continuous loop for user input
while True:

  stock_quantity = input("Enter stock quantity (or type 'quit' to exit): ")

  # Exit loop if user quits
  if stock_quantity.lower() == "quit":
    break

  # Handle invalid string inputs and negative numbers
  if not stock_quantity.isdigit():
    print("Error: Please enter a valid positive integer.")
    # Update state of failed entries
    failed_entries += 1
    continue

  # Convert stock quantity input from string to integer
  stock_quantity = int(stock_quantity)

  # Update state of inventory
  inventory += stock_quantity

  # Trigger overstock alert when inventory > 500
  if inventory > 500:
    print("Overstock Alert: Inventory exceeds 500 units.")
    break

# Reporting
print("Total Units Processed: ", inventory)
print("Number of Failed/Rejected Entries: ", failed_entries)