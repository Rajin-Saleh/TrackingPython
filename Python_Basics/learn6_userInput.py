# Taking Input from user in python

name = input("What is your name? ").capitalize()
print(f"Good to see you {name}.")

age = int(input("What is your age? "))
if age >= 18:
    print(f"Being {age} years old, makes you eligible for voting.")
else:
    print(f"{age} years old is not eligible for voting.")

food = input("What is your favorite food? ").capitalize()
if food == "Burger":
    print("Good choice but you should look after health.")
elif food == "Pizza":
    print("Original Italian pizzas are good for health.")
elif food == "Sandwich":
    print("Subway style sandwiches are great for breakfast.")
elif food == "Ramen":
    print("Hot Ramen in a freezing day, Ah. Joy of life.")
else:
    print("Have a feast of yourself.")


print(f"It felt very good to know you {name}")