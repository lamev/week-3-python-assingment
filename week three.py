def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Format and display result
if discount_percent >= 20:
    print(f"After applying a {discount_percent}% discount, the final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price remains: ${original_price:.2f}")