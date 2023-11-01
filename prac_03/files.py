"""
CP1404 Prac 3 Jack Kerlin
"""

# 1.
name = input("Enter name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.
out_file = open("name.txt", "r")
name = out_file.read()
print(f"Your name is {name.strip()}.")
out_file.close()

# 3.
out_file = open("numbers.txt", 'r')
result = int(out_file.readline()) + int(out_file.readline())
print(result)
out_file.close()

# 4.
out_file = open("numbers.txt", 'r')
total = 0
for line in out_file:
    total += int(line)
print(total)
out_file.close()
