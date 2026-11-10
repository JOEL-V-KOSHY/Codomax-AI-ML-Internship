# Day 4 — Find factorial using a for loop.
# Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120.
# By definition, 0! is 1.

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    print("Factorial of", number, "is", factorial)
