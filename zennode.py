# list of products
listOfProducts = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount mentioned
discRules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.1),
    "tiered_50_discount": (30, 0.5)
}

# Fees mentioned
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

# Input quantity and gift wrap 
quantities = {}
gift_wraps = {}

for product in listOfProducts:
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"
    quantities[product] = quantity
    gift_wraps[product] = gift_wrap

# total amount for each product
product_totals = {}
for product, quantity in quantities.items():
    product_totals[product] = listOfProducts[product] * quantity

#subtotal
subtotal = sum(product_totals.values())

# Apply discounts
applicable_discounts = {}
for discount, (threshold, discount_amount) in discRules.items():
    if subtotal > threshold:
        applicable_discounts[discount] = discount_amount

# most beneficial discount
if applicable_discounts:
    max_discount = max(applicable_discounts, key=applicable_discounts.get)
    discount_name = max_discount
    discount_amount = applicable_discounts[max_discount]
else:
    discount_name = "No discount"
    discount_amount = 0

# total quantity
total_quantity = sum(quantities.values())

# hipping fee
shipping_fee = (total_quantity // items_per_package) * shipping_fee_per_package

# gift wrap fee
gift_wrap_total = sum(gift_wraps.values())
gift_wrap_fee_total = gift_wrap_total * gift_wrap_fee

#final total
total = subtotal - discount_amount + shipping_fee + gift_wrap_fee_total

# Output
print("\n--- Order Details ---")
for product, quantity in quantities.items():
    print(f"{product} - Quantity: {quantity} - Total Amount: ${product_totals[product]}")

print(f"\nSubtotal: ${subtotal}")
print(f"Discount Applied: {discount_name} - Discount Amount: ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee_total}")
print(f"Total: ${total}")
