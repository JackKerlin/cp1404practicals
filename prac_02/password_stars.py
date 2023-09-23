"""
CP1404 Prac 2 Jack Kerlin
"""

min_length = 5

password = input("Password: ")
while len(password) < min_length:
    print("Invalid Password")
    password = input("Password: ")
print("*" * len(password))