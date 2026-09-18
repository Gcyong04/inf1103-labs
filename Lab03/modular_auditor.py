# Input Function
def get_valid_input():
  while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    # Exit loop if user quits
    if user_input.lower() == "quit":
      return 'quit'

    # Handle invalid string inputs and negative numbers
    if not user_input.isdigit():
      print("Error: Please enter a valid positive integer.")
      return None
    else:
      return int(user_input)


# Initialize inventory
inventory = 0

#Initialize failed/rejected entries
failed_entries = 0

# Main Loop
while True:

  delivery_amount = get_valid_input()

  if delivery_amount == "quit":
    break

  if delivery_amount is None:
    failed_entries += 1
    continue

  # Update state of inventory
  inventory += delivery_amount

  # Trigger overstock alert when inventory > 500
  if inventory > 500:
    print("Overstock Alert: Inventory exceeds 500 units.")
    break

# Reporting
print("Total Units Processed: ", inventory)
print("Number of Failed/Rejected Entries: ", failed_entries)