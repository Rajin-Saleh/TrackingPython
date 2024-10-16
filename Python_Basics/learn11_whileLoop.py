import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = None  # Initialize guess variable
attempts = 0  # Initialize attempts counter

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Start the guessing loop
while guess != secret_number:
    guess = input("Please enter your guess: ")

    # Validate input
    if not guess.isdigit():
        print("That's not a valid number. Please try again.")
        continue

    # Convert input to integer
    guess = int(guess)
    attempts += 1  # Increment attempts counter

    # Check the guess against the secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
