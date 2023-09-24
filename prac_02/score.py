"""
CP1404 Prac 2 Jack Kerlin"""


import random

def main():
    score = float(input("Enter score: "))
    print(check_score(score))
    print(check_score(random.randint(0, 100)))
def check_score(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"



main()
