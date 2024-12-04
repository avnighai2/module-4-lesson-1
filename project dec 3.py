# Function to calculate the change
def calculate_change(total_bill, amount_paid):
    return amount_paid - total_bill

# Total bill and amount paid
total_bill = 2.50
amount_paid = 4.00

# Calculate and display the change
change = calculate_change(total_bill, amount_paid)
print(f"The shopkeeper should return: ${change}")
