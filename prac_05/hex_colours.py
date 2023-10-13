"""
CP1404 Prac 5 Jack Kerlin
"""

COLOUR_TO_CODE = {"Acid Green": "#b0bf1a", "Aqua": "##00ffff", "Dark Violet": "#9400d3", "Denim": "#1560bd",
                  "Eggplant": "#614051", "Green Yellow": "#adff2f", "Harlequin": "#3fff00", "Lilac": "#c8a2c8",
                  "Linen": "#faf0e6"}

colour = input("Enter colour: ").lower().title()
while colour != "":
    try:
        print(f"{colour} code is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid colour.")
    colour = input("Enter colour: ").lower().title()
