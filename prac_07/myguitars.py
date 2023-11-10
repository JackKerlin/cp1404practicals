"""
CP1404 Prac 7 Jack Kerlin
estimate (for guitar and guitar_test): 30 mins
actual: 50 mins
"""

from guitar import Guitar

in_file = open("guitars.csv", "r")
parts = [line.strip().split(',') for line in in_file]
in_file.close()
guitars = sorted([Guitar(part[0], int(part[1]), float(part[2])) for part in parts])
print("Enter new guitars:")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(guitar, " added.")
    guitars.append(guitar)
    name = input("Name: ")

guitars = sorted(guitars)

for guitar in guitars:
    print(guitar)

out_file = open("guitars.csv", "w")
out_file.write("\n".join([",".join([guitar.name, str(guitar.year), str(guitar.cost)]) for guitar in guitars]))
out_file.close()
