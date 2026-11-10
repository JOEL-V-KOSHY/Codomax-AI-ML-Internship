# Day 4 — Store student details in a dictionary.

student = {
    "name": input("Enter student name: "),
    "course": input("Enter course: "),
    "age": int(input("Enter age: "))
}

print("\\n--- Student Details ---")
for key, value in student.items():
    print(key.title() + ":", value)
