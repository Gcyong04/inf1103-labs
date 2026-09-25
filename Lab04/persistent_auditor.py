# Global Constant
MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10% tax rate
ITEM_FIELDS = {
  "id": 0,
  "name": 1,
  "quantity": 2,
}

# Input Function
def get_valid_input():
  while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    # Exit loop if user quits
    if user_input.strip().lower() == 'quit':
      return "quit"

    # Handle invalid string inputs and negative numbers
    if not user_input.isdigit():
      print("Error: Please enter a valid positive integer.")
      return
    else:
      return int(user_input)

# Update total inventory function
def process_delivery(current_total, new_value):
  new_total = current_total + new_value
  return new_total

# Calculate tax amount function
def calculate_tax(amount):
  return amount * TAX_RATE

# Generate Report function
def generate_report(total_units, failed_attempts):
  print("------------------------\nSummary Report\n------------------------")
  print("Total Units Processed: ", total_units)
  print("Number of Failed/Rejected Entries: ", failed_attempts)
  return

# Load inventory function
def load_inventory():
  items = []
  with open("inventory.txt", 'r') as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      parts = [p.strip() for p in line.split(',')]
      parts[ITEM_FIELDS["id"]] = int(parts[ITEM_FIELDS["id"]])
      parts[ITEM_FIELDS["quantity"]] = int(parts[ITEM_FIELDS["quantity"]])
      items.append(parts)
  return items


def main():

  # Initialise variables
  inventory = []
  failed_entries = 0
  tax_amount = 0

  # Read file and load items into inventory
  inventory = load_inventory()

  while True:

    # Get & Validate User Input
    result = get_valid_input()

    if result == 'quit':
      break

    if result == None:
      failed_entries += 1
      continue

    # Update inventory state
    inventory = process_delivery(inventory, result)

    if inventory > MAX_CAPACITY:
      print("Overstock Alert: Inventory has exceed 500 units")
      break

    # Calculate tax amount
    tax_amount += calculate_tax(result)

  return generate_report(inventory, failed_entries)

# Program Entry Point
if __name__ == "__main__":
  main()