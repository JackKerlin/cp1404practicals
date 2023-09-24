"""
CP1404 Prac 2 Jack Kerlin
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_c_to_f(float(input("Celsius: ")))
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = convert_f_to_c(float(input("Fahrenheit: ")))
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_c_to_f(celsius):
    return celsius * 9.0 / 5 + 32


main()
