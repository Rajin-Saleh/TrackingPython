# for i in range(1, 1000):
#     print(i)
# for loop example

# for i in range(5):
#     print(i)

print("\nThis is a new one\n")

# for i in range(5, 1000, 5):  # range(start, stop, step_size)
#     print(i)

l = [1, 65, 8, 5, 63, 54, 56, 54, 6, 4, 69, 1, 100]  # list
for i in l:
    print(i)

print("\n")

t = (6, 231, 75, 222)  # tuple
for i in t:
    print(i)

print("\n")

s = "Harry"  # String
for i in s:
    print(i)

print("\n")

# For-else loop

j = [1, 7, 8]
for item in j:
    print(item)
else:
    print("Done")  # printed with loop exhausts!

print("\n")

# Break Statement

for i in range(100):
    if i == 51:
        break  # exist the loop right now
    print(i)

print("\n")

# Continue statement

for i in range(100):
    if i == 50:
        continue  # Skip the iteration
    print(i)

print("\n")

# Pass Statement
for i in range(645):
    pass  # without pass, the program will throw an error

i = 0
while i < 45:
    print(i)
    i += 1

print("\n")

for i in range(4):
    print("printing")
    if i == 2:
        continue  # continue Example
    print(i)
