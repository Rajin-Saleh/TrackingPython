"""
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”.
Write a program to detect these spams.
"""

user_comment = input("Enter a comment: ")

# Convert the comment to lowercase f
user_comment = user_comment.lower()

# Check for spam keywords
if "make a lot of money" in user_comment:
    print("This comment is spam.")
elif "buy now" in user_comment:
    print("This comment is spam.")
elif "subscribe this" in user_comment:
    print("This comment is spam.")
elif "click this" in user_comment:
    print("This comment is spam.")
else:
    print("This comment is not spam.")
