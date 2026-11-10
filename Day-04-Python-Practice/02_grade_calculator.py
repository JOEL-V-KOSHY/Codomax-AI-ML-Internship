# Day 4 — Calculate a simple grade from a percentage.

percentage = float(input("Enter percentage (0 to 100): "))

if percentage < 0 or percentage > 100:
    print("Please enter a percentage from 0 to 100.")
elif percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")
