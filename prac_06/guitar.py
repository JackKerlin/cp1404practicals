"""
CP1404 Prac 6 Jack Kerlin
estimate (for just guitar.py): 15 min
actual:  min
"""

class ProgrammingLanguage:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"


    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        if self.get_age(self) >= 50:
            return True
        else:
            return False