"""
CP1404 Prac 5 Jack Kerlin
Estimate: 40 minutes
Actual: 29 minutes
"""

words = input("Text: ").lower().split()
word_to_number = {}
for word in words:
    word_to_number[word] = word_to_number.get(word, 0) + 1
width = max([len(word) for word in word_to_number]) + 1
print("\n".join([f"{word:{width}}: {word_to_number[word]}" for word in sorted(word_to_number.keys())])
