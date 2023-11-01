"""
CP1404 Prac 6 Jack Kerlin
estimate (for guitar and guitar_test): 15 min
actual: 14 min
"""


class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
