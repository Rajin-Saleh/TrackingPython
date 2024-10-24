# Taking student name and score.
student_name = input("What is your name: ").title()
number_of_subject = int(input("Enter the number of subject: "))

# taking marks for each subject
total_mark = 0
for i in range(number_of_subject):
    marks = float(input(f"Enter marks for subject {i + 1} :"))
    total_mark += marks

# average number

avg_number = total_mark / number_of_subject

# Giving grade

if avg_number >= 90:
    grade = "A"
elif avg_number >= 80:
    grade = "B"
elif avg_number >= 70:
    grade = "C"
elif avg_number >= 60:
    grade = "D"
else:
    grade = "F"

# Displaying result

print(f"Student name: {student_name}")
print(f"Number of Subjects : {number_of_subject}")
print(f"Total marks: {total_mark}")
print(f"Average marks : {avg_number:.2f}")
print(f"Your Grade: {grade}")
