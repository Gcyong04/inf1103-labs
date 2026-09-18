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

# Update total inventory function
def process_delivery(current_total, new_value):
  return current_total + new_value

# Calculate tax amount function
def calculate_tax(amount):
  return amount*0.10

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

  # Update new total inventory
  inventory = process_delivery(inventory, delivery_amount)

  # Calculate tax
  tax = calculate_tax(delivery_amount)
  print("Tax for this delivery: ", tax)

  # Trigger overstock alert when inventory > 500
  if inventory > 500:
    print("Overstock Alert: Inventory exceeds 500 units.")
    break

# Reporting
print("Total Units Processed: ", inventory)
print("Number of Failed/Rejected Entries: ", failed_entries)