# Write a program to print multiplication table of a given number using for loop.


n = int(input("Enter a number: "))

for i in range(1, 11):
    multiply = n * i
    print(f"{n} X {i} = {multiply}")
