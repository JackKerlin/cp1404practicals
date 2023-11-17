"""
CP1404 Practical
Car class
"""
from unreliable_car import UnreliableCar

# Test 100% reliable car
reliable_car = UnreliableCar("Reliable Car", 1000, 100)
reliable_car.drive(100)
print(reliable_car)
assert reliable_car.fuel == 900
# Test 0% reliable car
unreliable_car = UnreliableCar("Unreliable Car", 1000, 0)
unreliable_car.drive(100)
print(unreliable_car)
assert unreliable_car.fuel == 1000
