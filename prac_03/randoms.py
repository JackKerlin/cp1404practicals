"""
CP1404 Prac 3 Jack Kerlin
"""
import random

print(random.randint(5, 20))  # line 1
"""this code generates random integers between 5 and 20 inclusive, so 5 and 20 are the smallest and largest generated"""
print(random.randrange(3, 10, 2))  # line 2
"""this code generates random integers from 3 to 10 in steps of 2, so 3, 5, 7, 9 could have been generated
so 3 is the smallest that could be generated but 10 can't, so 9 is the largest. 4 also can't."""
print(random.uniform(2.5, 5.5))  # line 3
"""this code generates random floats to 16 decimal places from 2.5 to 5.5, which both could have been randomly generated
so they are the smallest and largest possible"""
print(random.uniform(1,100))