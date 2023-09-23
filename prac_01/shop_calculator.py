"""
CP1404 Prac 1 Jack Kerlin
"""

items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
price_total = 0
for item in range(items):
    price_total += float(input("Price of item: $"))
if price_total > 100:
    price_total = price_total * 0.9
print(f"Total price for {items} items is ${price_total:.2f}")
