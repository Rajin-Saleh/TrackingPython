# Methods in Tuple


a = (1, 23, 23, 23, 45, 34, 34, 45, 657, 657, "Rohan")


# 1 count() method || Returns the number of occurrences of a specified value in the tuple.

print(a.count(23))
print(23 in a)
# index()  method || Returns the index of the first occurrence of a specified value in the tuple.

print(a.index(23))

# Tuple Operations ||
# Concatenation()  ||  concatenate two or more tuples using the + operator.

b = (1, 2, 3, "Rohan", "Somoy")
c = ("Ram", "Rom", 345, 435)
combine = b + c
print(combine)

# Repetition()     ||  can repeat a tuple using the * operator.
repet = c * 4
print(repet)

# Length of Tuple   ||  can get the length of a tuple using the len() function.

print(len(b))

# Slicing          ||  can slice a tuple to get a subset of it.

print(a[2:6])

# Membership        ||  can test if an element is present in the tuple using the in operator.

print(23 in a)

# Unpacking         || can unpack the elements of a tuple into individual variables.

a, b, c, d, e = b
print(a, b, c, d, e)
