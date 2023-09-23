"""
CP1404 Prac 1 Jack Kerlin
"""

name = input("Enter name: ")
choice = input("(H)ello \n(G)oodbye\n(Q)uit \n>>> ")
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    choice = input("(H)ello \n(G)oodbye\n(Q)uit \n>>>")
print("Finished")