# Day 4 — Number guessing game.
# The secret number is fixed so the beginner can focus on conditions and loops.

secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number (1 to 10): "))

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Correct! You guessed it.")
