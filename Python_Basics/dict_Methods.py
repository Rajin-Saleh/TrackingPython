marks = {
    "Harry": 100,
    "Shiyon": 78,
    "Roman": 89,
    "Jovian": 88,
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Rimi": 100})
print(marks)

print(marks.get("Harry"))
print(marks["Harry"])


# print(marks.get("Harry2"))  # for .get() method output will be None
# print(marks["Harry2"])  # for normal way it will return error
