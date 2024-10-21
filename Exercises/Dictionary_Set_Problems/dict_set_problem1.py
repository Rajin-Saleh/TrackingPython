"""'
Write a program to create a dictionary of Hindi words with values as their English translation.
Provide user with an option to look it up!

"""

print("Write any of the word")
print("Madad, kurshi, Samosa, Mithai")


words = {
    "Madad": "Help",
    "Kursi": "Chair",
    "Samosa": "Samosa",
    "Mithai": "Sweets",
}

translate = input("Enter any of the word above you to know english meaning:").title()

print(words[translate])
