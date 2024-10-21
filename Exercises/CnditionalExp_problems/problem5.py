"""
Write a program which finds out whether a given name is present in a list or not.
"""

names = ["Alice", "Robert", "James", "Charlie"]

username = input("Guess a name on the list: ")

if username in names:
    print(f"{username} is available in the list")
else:
    print(f"{username} is not available in the list")
