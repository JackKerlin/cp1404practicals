"""
CP1404 Prac 6 Jack Kerlin
estimate (for just this program): 30 min
actual: 45 min
"""

from prac_06.guitar import Guitar

guitars = []

print("Enter guitars:")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(guitar, " added.")
    guitars.append(guitar)
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512))
guitars.append(Guitar("Fender Stratocaster", 2014, 765.40350340609346039))
# find formatting width
guitar_name_width = max([len(guitar.name) for guitar in guitars])
# use f-string formatting as otherwise doesn't consider width change of rounding to 2 decimals
guitar_cost_width = max([len(f"{guitar.cost:,.2f}") for guitar in guitars])
for i, guitar in enumerate(guitars):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{guitar_name_width}} ({guitar.year}), "
          f"worth ${guitar.cost:>{guitar_cost_width},.2f}{vintage_string}")
