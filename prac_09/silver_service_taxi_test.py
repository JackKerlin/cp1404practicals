"""
CP1404 Practical
Test silver service taxi class
"""
from silver_service_taxi import SilverServiceTaxi

# Testing hummer
hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)

# Testing fare calculation
test_taxi = SilverServiceTaxi("Test", 200, 2)
test_taxi.drive(18)
assert test_taxi.get_fare() == 48.80
