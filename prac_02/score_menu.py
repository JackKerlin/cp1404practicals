"""
CP1404 Prac 2 Jack Kerlin
"""


def main():
    score = get_score()
    choice = input("(G)et a valid score\n(P)rint result\n(S)how score stars\n(Q)uit \n>>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(check_score(score))
        elif choice == "S":
            display_score(score)
        else:
            print("Invalid choice.")
        choice = input("(G)et a valid score\n(P)rint result\n(S)how score stars\n(Q)uit \n>>> ").upper()
    print("Goodbye")


def get_score():
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Score: "))
    return score


def check_score(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def display_score(score):
    print("*" * int(score))


main()
