"""
CP1404 Prac 1 Jack Kerlin
Fixed version of broken program
"""

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
