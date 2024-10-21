#  Check that a tuple type cannot be changed in python.


l = (23, 34, "Hello")
l[2] = "Hola"
print(l)
