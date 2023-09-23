"""
CP1404 Prac 2 Jack Kerlin
"""


def main():
    password = get_password()
    display_password(password)


def display_password(password):
    print("*" * len(password))


def get_password():
    min_length = 5
    password = input("Password: ")
    while len(password) < min_length:
        print("Invalid Password")
        password = input("Password: ")
    return password

main()