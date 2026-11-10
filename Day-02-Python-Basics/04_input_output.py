# Day 2 — Taking input and displaying output

name = input("Enter your name: ")
age_text = input("Enter your age: ")

# input() returns text, so convert age to an integer before arithmetic.
age = int(age_text)

print("Hello,", name)
print("Next year, you will be", age + 1)
