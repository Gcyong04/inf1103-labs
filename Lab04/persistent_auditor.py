# Global Constant
MAX_CAPACITY = 500
TAX_RATE = 0.1 # 10% tax rate

# Input Function
def get_valid_input(inventory_length):
  failed_attempts = 0
  while True:
    name = input("Enter product name (type 'quit' to exit): ")

    # Exit loop if user quits
    if name.strip().lower() == 'quit':
      return "quit"

     # Inner loop just for quantity, so invalid input doesn't re-ask for name
    while True:
      quantity = input("Enter quantity (type 'quit' to exit): ")

      if quantity.strip().lower() == 'quit':
        return "quit"

      if not quantity.isdigit():
        print("Error: Please enter a valid positive integer.")
        failed_attempts += 1
        continue 

      return [[inventory_length + 1, name, int(quantity)], failed_attempts]

# Update total inventory function
def process_delivery(inventory, new_item):
  new_inventory = inventory + [new_item]
  return new_inventory

# Calculate total quantity of inventory
def calculate_inventory_total(inventory):
  return sum(item[2] for item in inventory)

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
      parts[0] = int(parts[0])
      parts[2] = int(parts[2])
      items.append(parts)
  return items

def display_inventory(inventory):
  print("Current Inventory: ")
  for item in inventory:
    print(", ".join(str(x) for x in item))


def main():

  # Initialise variables
  inventory = []
  failed_entries = 0
  tax_amount = 0

  # Read file and load items into inventory
  inventory = load_inventory()
  display_inventory(inventory)

  while True:

    # Get & Validate User Input
    result = get_valid_input(len(inventory))

    if result == 'quit':
      break

    failed_entries += result[1]

    # Update inventory state
    inventory = process_delivery(inventory, result[0])

    if calculate_inventory_total(inventory) > MAX_CAPACITY:
      print("Overstock Alert: Inventory has exceed 500 units")
      break

    # Calculate tax amount
    tax_amount += calculate_tax(result[0][2])

  return generate_report(inventory, failed_entries)

# Program Entry Point
if __name__ == "__main__":
  main()