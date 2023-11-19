"""
CP1404 Practical Jack Kerlin
Unreliable Car class tests
"""

from unreliable_car import UnreliableCar

# Test 95% reliable car
reliable_car = UnreliableCar("Reliable Car", 100, 95)
# Test 5% reliable car
unreliable_car = UnreliableCar("Unreliable Car", 100, 5)
# Test 50% reliable car
semireliable_car = UnreliableCar("Semi-reliable Car", 100, 50)
test_count = [0, 0, 0]
for i in range(0, 100):
    if reliable_car.drive(1) == 1:
        test_count[0] += 1
    if unreliable_car.drive(1) == 1:
        test_count[1] += 1
    if semireliable_car.drive(1) == 1:
        test_count[2] += 1
print(test_count)
