# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
L = ["Harry", "Soham", "Sachin", "Rahul"]

for name in L:
    if name.startswith("S"):
        print(f"Hello {name}")
