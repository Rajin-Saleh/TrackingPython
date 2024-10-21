# Write a program to find the greatest of four numbers
# entered by the user.


num1 = int(input("Enter the number: "))

num2 = int(input("Enter the number: "))

num3 = int(input("Enter the number: "))

num4 = int(input("Enter the number: "))


if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    greatest = num1
    print(num1)
if (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    greatest = num2
    print(num2)
if (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    greatest = num3
    print(num3)
else:
    greatest = num4
    print(num4)
