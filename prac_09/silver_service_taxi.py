"""
CP1404 Practical Jack Kerlin
Silver service taxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Version of Taxi that includes flagfall and fanciness"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0
