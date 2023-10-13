"""
CP1404 Prac 5 Jack Kerlin
Expected: 30 minutes
Actual: 33 mins
"""

emails_to_name = {}
email = input("Email: ")
while email != "":
    # splits email in two, then splits name in two then joins and title cases it
    name = " ".join(email.split("@")[0].split(".")).title()
    response = input(f"Is your name {name}? ").lower()
    if response in ["", "y"]:
        emails_to_name[email] = name
    else:
        emails_to_name[email] = input("Enter name: ")
    email = input("Email: ")
[print(f"{emails_to_name[email]} ({email})") for email in emails_to_name.keys()]
