"""
CP1404 Prac 5 Jack Kerlin
Expected: 50 minutes
Actual: 40 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    lines = format_file()
    del lines[0]  # delete header
    champions_to_count = count_champions(lines)
    print("Wimbledon Champions: ")
    # join list comp to print out champs
    print("\n".join([f"{champion} {champions_to_count[champion]}" for champion in champions_to_count]))
    countries = count_countries(lines)
    print(f"These {len(countries)} countries have won Wimbledon:\n" + ", ".join(countries))


def format_file():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        # returns a list of lists
        return [line.split(',') for line in lines]


def count_champions(lines):
    champions_to_count = {}
    # counts champs in the lines
    for line in lines:
        champion = line[CHAMPION_INDEX]
        champions_to_count[champion] = champions_to_count.get(champion, 0) + 1
    return champions_to_count


def count_countries(lines):
    countries = set()
    # adds countries to set, set automatically ignores duplicates
    for line in lines:
        countries.add(line[COUNTRY_INDEX])
    return sorted(countries)


main()
