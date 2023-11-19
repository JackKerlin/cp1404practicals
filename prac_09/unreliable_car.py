"""
CP1404 Practical
Unreliable Car class
"""

from car import Car
import random


class UnreliableCar(Car):
    """Version of Car that represent unreliability"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if a randomly generated number is more than the unreliability.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if random.uniform(0, 100) < self.reliability:
            distance = super().drive(distance)
        else:
            distance = 0
        return distance
