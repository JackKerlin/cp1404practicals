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
        """Return a string representation of a band."""
        return str(vars(self))

    def __str__(self):
        """Return a string representation of a band."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Append an object to list of musicians"""
        self.musicians.append(musician)

    def play(self):
        """Return a string of every musician playing."""
        play_string = [musician.play() for musician in self.musicians]
        return "\n".join(play_string)
