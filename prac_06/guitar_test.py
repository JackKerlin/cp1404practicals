"""
CP1404 Prac 6 Jack Kerlin
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
other_guitar = Guitar("other one", 2000, 3)
print(f"{gibson.name} get_age() - expected 101. got {gibson.get_age()}")
print(f"{other_guitar.name} get_age() - expected 23. got {other_guitar.get_age()}")
print(f"{gibson.name} is_vintage() - expected True. got {gibson.is_vintage()}")
print(f"{other_guitar.name} is_vintage() - expected False. got {gibson.is_vintage()}")