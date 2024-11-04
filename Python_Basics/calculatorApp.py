# Calculator Function Definitions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def power(x, y):
    return x**y


def modulus(x, y):
    return x % y


# Main Calculator Loop
def calculator():
    print("Welcome to the Intermediate Calculator!")
    operations = {
        "1": "Addition",
        "2": "Subtraction",
        "3": "Multiplication",
        "4": "Division",
        "5": "Exponentiation (Power)",
        "6": "Modulus",
        "7": "Exit",
    }

    while True:
        print("\nAvailable Operations:")
        for key, value in operations.items():
            print(f"{key}. {value}")

        # Take user input for the operation
        choice = input("\nSelect operation (1-7): ")

        if choice == "7":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in operations:
            # Take user inputs for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the selected operation
            if choice == "1":
                print(f"The result of addition: {add(num1, num2)}")
            elif choice == "2":
                print(f"The result of subtraction: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"The result of multiplication: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"The result of division: {divide(num1, num2)}")
            elif choice == "5":
                print(f"The result of exponentiation: {power(num1, num2)}")
            elif choice == "6":
                print(f"The result of modulus: {modulus(num1, num2)}")
        else:
            print("Invalid input, please choose a valid option.")


# Run the calculator
calculator()

#
