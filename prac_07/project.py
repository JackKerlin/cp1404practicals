"""
CP1404 Prac 7 Jack Kerlin
"""

DATE_STRING = "%d/%m/%Y"

class Project:
    """Represent a project object"""

    def __init__(self, name="", date=0, priority=0, cost=0, completion=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return (f"{self.name}, start: {self.date.strftime(DATE_STRING)}, priority {self.priority},  estimate: ${self.cost:.2f}, "
                f"completion: {self.completion}%")

    def is_complete(self):
        return self.completion >= 100

    def __lt__(self, other):
        return self.priority < other.priority
