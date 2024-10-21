"""
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
"""

result = int(input("Enter your result "))

if 90 <= result <= 100:
    print("Ex")
elif 80 <= result <= 90:
    print("A")
elif 70 <= result <= 80:
    print("B")
elif 60 <= result <= 70:
    print("C")
elif 50 <= result <= 60:
    print("D")
elif result <= 50:
    print("f")
else:
    print("Your result is invalid!")
