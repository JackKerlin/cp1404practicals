"""
CP1404 Prac 3 Jack Kerlin
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1. Anytime the numerator or denominator inputs aren't a valid integer, e.g. a float or text
2. If the denominator input is 0
3. Error check the denominator input until it isn't 0
"""
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
while denominator == 0:
    denominator = int(input("Enter the denominator: "))
fraction = numerator / denominator
print(fraction)