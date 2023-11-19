"""CP1404 Practical
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_MESSAGE = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    chosen_taxi = None
    bill = 0.0
    user_choice = input(MENU_MESSAGE).lower()
    while user_choice != "q":
        if user_choice == "c":
            display_taxis(taxis)
            chosen_taxi = choose_taxi(taxis)
        elif user_choice == "d":
            if chosen_taxi is not None:
                drive_taxi(taxis, chosen_taxi)
                bill += taxis[chosen_taxi].get_fare()
                taxis[chosen_taxi].start_fare()
            else:
                print("You must choose a taxi before you can drive.")
        else:
            print("Invalid option.")
        print(f"Bill to date: ${bill:.2f}")
        user_choice = input(MENU_MESSAGE).lower()
    print(f"Total trip cost: {bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Get valid input for a taxi index"""
    try:
        chosen_taxi = int(input("Choose taxi: "))
        if chosen_taxi < 0 or chosen_taxi >= len(taxis):
            print("Invalid taxi choice.")
        else:
            return chosen_taxi
    except ValueError:
        print("Taxi choice must be integer.")


def drive_taxi(taxis, chosen_taxi):
    """"""
    distance = get_distance()
    taxis[chosen_taxi].drive(distance)
    print(f"Your {taxis[chosen_taxi].name} trip cost you ${taxis[chosen_taxi].get_fare():.2f}")


def get_distance():
    """Get valid input for distance to drive"""
    is_valid_input = False
    while not is_valid_input:
        try:
            distance = float(input("Drive how far? "))
            while distance < 0:
                print("Distance must more than or equal to zero.")
                distance = float(input("Drive how far? "))
            is_valid_input = True
        except ValueError:
            print("Distance must be a number.")
    return distance


main()
