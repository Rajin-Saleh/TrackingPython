name = "Robin"

for i in name:
    print(i)
    if ( i == "b"):
        print("This is something special!")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color) # iterating the colors
    for i in color:
        print(i) # iterating the color


for k in range(50):
    print(k+1)

for j in range(1, 12, 2):
    print(j)