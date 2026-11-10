# Day 3 — A function is a reusable block of code.

def greet(name):
    """Return a greeting for the supplied name."""
    return "Hello, " + name + "!"

def square(number):
    """Return the square of a number."""
    return number * number

print(greet("Alex"))
print("Square of 6:", square(6))
