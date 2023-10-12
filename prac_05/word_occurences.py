"""
CP1404 Prac 5 Jack Kerlin
Estimate: 40 minutes
Actual: 29 minutes
"""

text = input("Text: ")
word_to_number = {}
for word in text.lower().split():
    if word in word_to_number:
        word_to_number[word] += 1
    else:
        word_to_number[word] = 1
width = max([len(word) for word in word_to_number])+ 1
[print(f"{word:{width}}: {word_to_number[word]}") for word in sorted(word_to_number.keys())]