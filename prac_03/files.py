"""
CP1404 Prac 3 Jack Kerlin
"""

name = input("Enter name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

out_file = open("name.txt", "r")
name = out_file.read()
print(f"Your name is {name.strip()}.")
out_file.close()

out_file = open("numbers.txt", 'r')
print(int(out_file.readline().strip()) + int(out_file.readline().strip()))
out_file.close()

out_file = open("numbers.txt", 'r')
numbers_sum = 0
for line in out_file:
    numbers_sum += int(line.strip())
print(numbers_sum)
out_file.close()
