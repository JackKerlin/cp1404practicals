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
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        else:
            distance = 0
        return distance
