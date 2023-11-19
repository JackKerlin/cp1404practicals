"""
CP1404 Practical Jack Kerlin
Band class
"""


class Band:
    """Represent a Band object"""

    def __init__(self, name):
        """Initialise a Guitar."""
        self.name = name
        self.musicians = []

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        play_string = [musician.play() for musician in self.musicians]
        return "\n".join(play_string)
