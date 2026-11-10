# Module 01 — Complete Learning Notes
## Introduction to AI & Python (Day 1–Day 4)

These notes consolidate the four-day beginner module. The detailed Day 1 notes are in `../Day-01-AI-ML-DL/learning_notes.md`.

# Day 1 — AI, ML and DL
- AI is the broad field of creating systems that perform tasks associated with human intelligence.
- ML is a subset of AI that learns patterns from data.
- DL is a subset of ML that uses neural networks with multiple layers.
- Relationship: AI ⟶ ML ⟶ DL.
- Applications include healthcare, banking, education, transport, e-commerce, agriculture, and cybersecurity.
- AI can help automate work and identify patterns, but outputs can be inaccurate or biased. Human oversight matters.

# Day 2 — Python fundamentals

## Python
Python is a high-level, general-purpose programming language known for readable syntax. It is used in web development, automation, data analysis, AI, and ML.

## Variables
A variable is a name referring to a value.

```python
student_name = "Alex"
age = 20
```

Use descriptive names. A variable name cannot begin with a number and should not contain spaces.

## Basic data types
| Type | Purpose | Example |
|---|---|---|
| `str` | Text | `"Python"` |
| `int` | Whole number | `25` |
| `float` | Decimal number | `89.5` |
| `bool` | True/False value | `True` |

Use `type(value)` to inspect a value's type.

## Input and output
- `input()` receives text from the user.
- `print()` displays output.
- Convert input before numeric calculations: `age = int(input("Age: "))`.

## Operators
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`

# Day 3 — Python programming

## Conditions
Use `if`, `elif`, and `else` to choose which block of code runs.

```python
if marks >= 40:
    print("Pass")
else:
    print("Try again")
```

## Loops
A loop repeats a block of code.
- `for` is commonly used to iterate over a sequence or range.
- `while` repeats while a condition remains true.
- Update the loop condition correctly to avoid an infinite loop.

```python
for value in range(1, 6):
    print(value)
```

## Lists
A list stores an ordered collection of items. Indexing starts at zero.

```python
subjects = ["AI", "Python", "SQL"]
print(subjects[0])
subjects.append("ML")
```

## Functions
A function is a reusable block of code. Define it using `def`. Parameters receive inputs; `return` sends a result back.

```python
def add(a, b):
    return a + b
```

# Day 4 — Practical programs
The practical folder contains:
1. Simple calculator
2. Grade calculator
3. Factorial calculator
4. Student details using a dictionary
5. Multiplication table
6. Number guessing game

## How to practise
1. Read the comments in each program.
2. Run the program in a terminal.
3. Try at least three different inputs.
4. Predict the output before running it.
5. Change one part of the program and observe what happens.
6. Explain the program in your own words.

# Final revision questions
1. What is AI? Give two examples.
2. Explain ML and DL.
3. What is a variable?
4. Name four basic Python data types.
5. What is the difference between `=` and `==`?
6. What is the purpose of `if` and `else`?
7. Differentiate between `for` and `while`.
8. What is a list? What does `append()` do?
9. What is a function? Explain `return`.
10. What is type conversion and why is it needed with `input()`?
