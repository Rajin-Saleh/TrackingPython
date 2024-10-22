# Write a program to print multiplication table
# of a given number
# using while loop


n = int(input("Enter you number:  "))

i = 1
while i <= 10:
    multiply = n * i
    print(f"{n} x {i} = {multiply}")
    i += 1
