"""
Write a program to print the following star pattern.
"""

"""
    *
   ***
  ***** for n = 5
 *******
*********
"""
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="\n")

# It was complicated
