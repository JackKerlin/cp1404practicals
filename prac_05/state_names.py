"""
CP1404 Prac 5 Jack Kerlin
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

print("\n".join([f"{code:<3} is {CODE_TO_NAME[code]}" for code in CODE_TO_NAME]))

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
