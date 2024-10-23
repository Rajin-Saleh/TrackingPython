# Learning Functions in Python

# Function Definition
def tnk(name, ending="Thank you"):
    # name = input("Enter you name: ").title()
    print(f"Good Days {name}.")
    print(ending)


tnk("Price")
tnk("Ray", "Thanks")


def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c) / 3
    print(average)


avg()  # Function call
print(type(avg))


# Default parameter
