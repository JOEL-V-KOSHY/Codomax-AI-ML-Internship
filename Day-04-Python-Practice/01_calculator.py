# Day 4 — Simple calculator supporting +, -, *, and /

first = float(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
second = float(input("Enter the second number: "))

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    if second == 0:
        result = None
        print("Error: division by zero is not allowed.")
    else:
        result = first / second
else:
    result = None
    print("Error: unsupported operator.")

if result is not None:
    print("Result:", result)
