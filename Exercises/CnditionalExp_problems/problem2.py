"""
Write a program to find out whether a student has passed or failed if
it requires a total of 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as an input from the user.
"""

score1 = int(input("Enter Subject 1 score: "))
score2 = int(input("Enter Subject 2 score: "))
score3 = int(input("Enter Subject 3 score: "))

result = score1 + score2 + score3

max_number = 300
percentage = (result / max_number) * 100
print(percentage)
if percentage >= 40:
    print("You have passed")
elif percentage >= 33:
    print("You have barely passed")
else:
    print("You have failed")
