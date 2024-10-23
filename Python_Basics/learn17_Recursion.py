# Recursion of Python

"""
factorial(5) = 5x4x3x2x1

"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter number: "))
print(f"The factorial of this number is : {factorial(n)}")
