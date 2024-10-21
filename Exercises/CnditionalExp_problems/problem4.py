"""
Write a program to find whether a given username contains less than 10
characters or not.
"""

user_name = input("Enter your username: ").lower()

chr = len(user_name)
print(chr)

if chr > 10:
    print("It has more than 10 character.")
else:
    print("It has lees than 10 character.")
