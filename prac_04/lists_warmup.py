"""
CP1404 Prac 4 Jack Kerlin
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]: 3, numbers[-1]: 2, numbers[3]: 1, numbers[:-1]: [3, 1, 4, 1, 5, 9]
numbers[3:4]: 1, 5 in numbers: TRUE, 7 in numbers: FALSE, "3" in numbers: FALSE
numbers + [6, 5, 3]: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]"""

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
