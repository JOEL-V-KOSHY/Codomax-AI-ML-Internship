# Day 3 — Lists store multiple values in one variable.

skills = ["Python", "SQL", "Machine Learning"]

print("Complete list:", skills)
print("First skill:", skills[0])  # List indexing starts at 0.

skills.append("Deep Learning")
print("After adding an item:", skills)

for skill in skills:
    print("-", skill)
