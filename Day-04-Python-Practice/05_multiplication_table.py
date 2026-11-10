# Day 4 — Print a multiplication table.

number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)
