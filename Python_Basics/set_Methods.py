s = {1, 5, 32, 54, 5, 5, 5}

print(s, type(s))
s.add(566)  # Add element
print(s)
s.remove(1)  # remove an element
print(s)


s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}
print(s2.union(s1))  # union()
print(s2.intersection(s1))  # intersection()
