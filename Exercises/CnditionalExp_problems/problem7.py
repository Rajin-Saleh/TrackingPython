# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter you post: ").lower()

name = "harry"

if name in post:
    print("Harry exist!")
else:
    print("Harry doesn't exist.")
