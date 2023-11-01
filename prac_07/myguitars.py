"""
CP1404 Prac 7 Jack Kerlin
estimate (for guitar and guitar_test):
actual:
"""

from guitar import Guitar

in_file = open("guitars.csv", "r")
parts = [line.strip().split(',') for line in in_file]
guitars = sorted([Guitar(part[0], int(part[1]), float(part[2])) for part in parts])
for guitar in guitars:
    print(guitar)