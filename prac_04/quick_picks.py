"""
CP1404 Prac 4 Jack Kerlin
"""

import random

NUMBERS_IN_LINE = 6
MAX_NUMBERS = 45
MIN_NUMBERS = 1
def main():
    number_of_picks = int(input("How many quick picks? "))
    picks = generate_picks(number_of_picks)
    print(*picks, sep="\n")


def generate_picks(number_of_picks):
    picks = []
    for pick in range(0, number_of_picks):
        # adds nested list within picks
        picks.append([])
        for number in range(NUMBERS_IN_LINE):
            # adds numbers to nested list with while loop to no repeats
            pick_number = random.randint(1, 45)
            while pick_number in picks[pick]:
                pick_number = random.randint(1, 45)
            picks[pick].append(pick_number)
        # sorts, right aligns and joins nested lest to make it a string
        picks[pick] = " ".join([str(number).rjust(2) for number in sorted(picks[pick])])
    return picks


main()