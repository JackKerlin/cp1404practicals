"""
CP1404 Prac 5 Jack Kerlin
Expected: 50 minutes
Actual: 40 minutes
"""


def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        # makes a list of lists
        lines = format_file(in_file)
        del lines[0]
        champions_to_count = count_champions(lines)
        print("Wimbledon Champions: ")
        [print(f"{champion} {champions_to_count[champion]}") for champion in champions_to_count]
        countries = count_countries(lines)
        print(f"These {len(countries)} have won Wimbledon:\n" + ", ".join(countries))


def format_file(in_file):
    lines = in_file.readlines()
    return [line.split(',') for line in lines]


def count_champions(lines):
    champions_to_count = {}
    for line in lines:
        champion = line[2]
        champions_to_count[champion] = champions_to_count.get(champion, 0) + 1
    return champions_to_count


def count_countries(lines):
    countries = set()
    [countries.add(line[1]) for line in lines]
    return sorted(countries)


main()
