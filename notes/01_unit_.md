# UNIT 1: Python Fundamentals

## Topics Covered
1. Python Features and Installation
2. Variables and Data Types
3. Type Conversion
4. Input and Output Functions
5. Conditional Statements
6. Logical Operators
7. for Loop
8. while Loop
9. Nested Loops
10. break and continue
11. range Function

---

## 1. Python Features and Installation

### What is Python?
Python is a high-level, interpreted, general-purpose programming language created by Guido van Rossum, first released in 1991. It is widely used in web development, data science, artificial intelligence, automation, and scripting.

### Key Features

**1. Easy to Learn and Read**
Python uses simple, English-like syntax. Indentation is used to define code blocks instead of curly braces `{}`.

```python
if True:
    print("Python uses indentation")
```

**2. Interpreted Language**
Python code is executed line by line by an interpreter, not compiled into machine code beforehand. This makes debugging easier but can make execution slower than compiled languages like C++.

**3. Dynamically Typed**
You do not need to declare the data type of a variable. Python determines it automatically at runtime.

```python
x = 10        # x is an integer
x = "hello"   # now x is a string, no error
```

**4. Interpreted and Platform Independent**
Python code written on one operating system (Windows, Linux, macOS) runs on another without modification, as long as Python is installed.

**5. Object-Oriented**
Python supports classes, objects, inheritance, and other OOP concepts (covered in Unit 4).

**6. Extensive Standard Library**
Python comes with built-in modules for file handling, math operations, date and time, networking, and more, so you often do not need external libraries for basic tasks.

**7. Large Ecosystem of Third-Party Libraries**
Libraries like NumPy, Pandas, Django, Flask, and TensorFlow extend Python for specialized use cases such as data science and web development.

**8. Free and Open Source**
Python is free to download, use, and distribute. Its source code is open for modification.

### Installation

**Step 1: Download Python**
Visit `python.org/downloads` and download the latest stable release for your operating system.

**Step 2: Install**
Run the installer. On Windows, make sure to check the box **"Add Python to PATH"** before clicking Install.

**Step 3: Verify Installation**
Open Command Prompt (Windows) or Terminal (Linux/macOS) and type:

```bash
python --version
```

or on some systems:

```bash
python3 --version
```

This should display the installed Python version, for example `Python 3.12.0`.

**Step 4: Running Python Code**

There are three common ways to run Python code:

- **Interactive Mode (Python Shell):** Type `python` in the terminal to open an interactive shell where you can run one line at a time.
- **Script Mode:** Write code in a `.py` file (e.g., `program.py`) and run it using:
  ```bash
  python program.py
  ```
- **IDE/Code Editor:** Tools like VS Code, PyCharm, or Jupyter Notebook provide a full environment to write, run, and debug Python code.

---

## 2. Variables and Data Types

### Variables

A variable is a named location in memory used to store data. In Python, you do not need to declare a variable's type explicitly; it is created the moment you assign a value.

```python
name = "Ravi"
age = 20
height = 5.8
```

**Rules for Naming Variables:**
- Must start with a letter or underscore (`_`), not a digit.
- Can contain letters, digits, and underscores.
- Case-sensitive (`age` and `Age` are different variables).
- Cannot use Python reserved keywords (like `if`, `for`, `class`) as variable names.

```python
valid_name = 10      # valid
_valid = 20           # valid
2invalid = 30          # invalid, starts with a digit -> SyntaxError
```

**Multiple Assignment:**

```python
a, b, c = 1, 2, 3
x = y = z = 0
```

### Data Types

Python has several built-in data types:

**1. Numeric Types**

- `int` — whole numbers, e.g. `10`, `-5`, `0`
- `float` — decimal numbers, e.g. `3.14`, `-0.5`
- `complex` — numbers with real and imaginary parts, e.g. `2 + 3j`

```python
a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex
```

**2. String (`str`)**
A sequence of characters enclosed in single, double, or triple quotes.

```python
name = "Python"
sentence = 'Learning is fun'
multiline = """This is
a multi-line string"""
```

**3. Boolean (`bool`)**
Represents one of two values: `True` or `False`. Used in conditional logic.

```python
is_active = True
is_finished = False
```

**4. Sequence Types**

- `list` — ordered, mutable collection: `[1, 2, 3]`
- `tuple` — ordered, immutable collection: `(1, 2, 3)`

(Covered in detail in Unit 2)

**5. Mapping Type**

- `dict` — key-value pairs: `{"name": "Ravi", "age": 20}`

(Covered in detail in Unit 2)

**6. Set Types**

- `set` — unordered collection of unique items: `{1, 2, 3}`

(Covered in detail in Unit 2)

**7. None Type**
`None` represents the absence of a value.

```python
result = None
```

### Checking Data Type

The `type()` function returns the data type of a variable.

```python
x = 10
print(type(x))     # <class 'int'>

y = "hello"
print(type(y))     # <class 'str'>
```

---

## 3. Type Conversion

Type conversion is the process of converting one data type into another. Python supports two kinds:

### Implicit Type Conversion
Python automatically converts a smaller data type to a larger one to avoid data loss. This happens without the programmer's intervention.

```python
a = 10        # int
b = 3.5       # float
c = a + b     # int is automatically converted to float
print(c)      # 13.5
print(type(c))  # <class 'float'>
```

### Explicit Type Conversion (Type Casting)
The programmer manually converts one data type to another using built-in functions.

**Common Conversion Functions:**

| Function | Purpose |
|---|---|
| `int()` | Converts to integer |
| `float()` | Converts to float |
| `str()` | Converts to string |
| `bool()` | Converts to boolean |
| `list()` | Converts to list |
| `tuple()` | Converts to tuple |

**Examples:**

```python
# String to int
a = "10"
b = int(a)
print(b + 5)     # 15

# Int to string
x = 25
y = str(x)
print("Value is " + y)   # Value is 25

# String to float
p = "3.14"
q = float(p)
print(q)          # 3.14

# Float to int (decimal part is truncated, not rounded)
n = 9.8
m = int(n)
print(m)           # 9

# Int to bool
print(bool(0))      # False
print(bool(5))      # True
print(bool(""))     # False (empty string is falsy)
print(bool("hi"))   # True
```

**Important Errors to Note:**

```python
a = "hello"
b = int(a)   # ValueError: invalid literal for int() with base 10: 'hello'
```

Conversion fails if the string does not represent a valid number.

---

## 4. Input and Output Functions

### Output: `print()`

The `print()` function displays output to the console.

```python
print("Hello, World!")
print(10)
print(3.14)
```

**Printing Multiple Values:**

```python
name = "Ravi"
age = 20
print("Name:", name, "Age:", age)
# Output: Name: Ravi Age: 20
```

**`sep` parameter** (separator between values, default is a space):

```python
print("Python", "Java", "C++", sep=", ")
# Output: Python, Java, C++
```

**`end` parameter** (what to print at the end, default is a newline):

```python
print("Hello", end=" ")
print("World")
# Output: Hello World
```

**String Formatting in Output:**

Using f-strings (recommended, Python 3.6+):

```python
name = "Ravi"
age = 20
print(f"My name is {name} and I am {age} years old.")
```

Using `.format()`:

```python
print("My name is {} and I am {} years old.".format(name, age))
```

### Input: `input()`

The `input()` function reads a line of text from the user. It **always returns a string**, regardless of what the user types.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Important: Converting Input**

Since `input()` returns a string, numeric input must be explicitly converted.

```python
age = input("Enter your age: ")   # age is a string, e.g. "20"
age = int(age)                     # now age is an integer 20

# Common shortcut
age = int(input("Enter your age: "))
```

**Example: Taking Multiple Inputs**

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
```

**Taking Space-Separated Input:**

```python
# Input: 10 20 30
values = input("Enter three numbers: ").split()
print(values)   # ['10', '20', '30']

# Converting all to int using list comprehension / map
values = list(map(int, input("Enter three numbers: ").split()))
print(values)   # [10, 20, 30]
```

---

## 5. Conditional Statements

Conditional statements allow a program to execute different blocks of code based on whether a condition is `True` or `False`.

### `if` Statement

```python
age = 20
if age >= 18:
    print("You are eligible to vote.")
```

### `if-else` Statement

```python
age = 15
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### `if-elif-else` Statement

Used when there are multiple conditions to check in sequence.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

Only the first matching condition's block executes; the rest are skipped.

### Nested `if` Statements

An `if` statement inside another `if` statement.

```python
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive Even number")
    else:
        print("Positive Odd number")
else:
    print("Non-positive number")
```

### Comparison Operators (used in conditions)

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

### Short-Hand `if` (Ternary-like)

```python
a = 10
b = 20
max_value = a if a > b else b
print(max_value)   # 20
```

---

## 6. Logical Operators

Logical operators are used to combine multiple conditions.

| Operator | Description | Example |
|---|---|---|
| `and` | True if both conditions are true | `a > 5 and b < 10` |
| `or` | True if at least one condition is true | `a > 5 or b < 10` |
| `not` | Reverses the result | `not(a > 5)` |

### Examples

**`and` operator:**

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Allowed to enter")
else:
    print("Not allowed")
```

**`or` operator:**

```python
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today")
else:
    print("Work day")
```

**`not` operator:**

```python
is_raining = False

if not is_raining:
    print("You can go for a walk")
```

### Truth Table Reference

| A | B | A and B | A or B | not A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

### Combined Example

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
```

---

## 7. `for` Loop

The `for` loop is used to iterate over a sequence (list, string, tuple, range, etc.) and execute a block of code for each element.

### Basic Syntax

```python
for item in sequence:
    # code to execute
```

### Iterating Over a String

```python
for ch in "Python":
    print(ch)

# Output:
# P
# y
# t
# h
# o
# n
```

### Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Iterating with `range()`

```python
for i in range(5):
    print(i)
# Output: 0 1 2 3 4
```

### Example: Sum of First N Natural Numbers

```python
n = 10
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum =", total)   # Sum = 55
```

### Example: Printing a Multiplication Table

```python
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### `for` Loop with `else`

The `else` block executes after the loop completes normally (without a `break`).

```python
for i in range(5):
    print(i)
else:
    print("Loop finished without break")
```

---

## 8. `while` Loop

The `while` loop repeatedly executes a block of code as long as a given condition remains `True`.

### Basic Syntax

```python
while condition:
    # code to execute
```

### Example: Counting from 1 to 5

```python
i = 1
while i <= 5:
    print(i)
    i = i + 1
```

**Important:** The loop variable must be updated inside the loop; otherwise, it results in an **infinite loop**.

### Example: Sum of Digits of a Number

```python
num = 1234
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits =", total)   # 10
```

### Example: Reverse a Number

```python
num = 1234
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)   # 4321
```

### `while` Loop with `else`

```python
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed")
```

### `for` vs `while`

| `for` loop | `while` loop |
|---|---|
| Used when the number of iterations is known or a sequence is being traversed | Used when the number of iterations depends on a condition |
| Iterates over a sequence directly | Requires manual condition update |
| Example: iterating over a list | Example: repeating until user enters "quit" |

---

## 9. Nested Loops

A nested loop is a loop inside another loop. The inner loop completes all its iterations for each single iteration of the outer loop.

### Basic Structure

```python
for i in outer_sequence:
    for j in inner_sequence:
        # code
```

### Example: Printing a Pattern (Square of Stars)

```python
rows = 4
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

# Output:
# * * * *
# * * * *
# * * * *
# * * * *
```

### Example: Right-Angled Triangle Pattern

```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

### Example: Multiplication Table Using Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
```

### Example: Nested `while` Loop

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1
```

---

## 10. `break` and `continue`

These are loop control statements used to alter the normal flow of loop execution.

### `break` Statement

The `break` statement immediately terminates the loop, and control moves to the statement after the loop.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Output: 1 2 3 4
```

**Example: Searching for a Number**

```python
numbers = [4, 8, 15, 16, 23, 42]
target = 15

for num in numbers:
    if num == target:
        print("Number found!")
        break
else:
    print("Number not found")
```

### `continue` Statement

The `continue` statement skips the rest of the current iteration and moves to the next iteration of the loop.

```python
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# Output: 1 3 5 7 9  (even numbers are skipped)
```

**Example: Skipping Negative Numbers**

```python
numbers = [10, -5, 20, -3, 15]

for num in numbers:
    if num < 0:
        continue
    print(num)

# Output: 10 20 15
```

### `break` vs `continue`

| `break` | `continue` |
|---|---|
| Stops the loop entirely | Skips only the current iteration |
| Control exits the loop | Control moves to the next iteration |
| Used to exit early when a condition is met | Used to skip unwanted values while continuing the loop |

### Combined Example

```python
for i in range(1, 20):
    if i == 15:
        break
    if i % 2 == 0:
        continue
    print(i)

# Prints odd numbers from 1 up to 13, then stops at 15
```

---

## 11. `range()` Function

The `range()` function generates a sequence of numbers and is most commonly used with `for` loops.

### Syntax

```python
range(start, stop, step)
```

- `start` — starting value (default is `0`, inclusive)
- `stop` — ending value (exclusive, i.e., not included)
- `step` — increment/decrement value (default is `1`)

### Forms of `range()`

**1. `range(stop)`** — starts at 0, increments by 1

```python
for i in range(5):
    print(i)
# Output: 0 1 2 3 4
```

**2. `range(start, stop)`** — starts at `start`, increments by 1

```python
for i in range(2, 7):
    print(i)
# Output: 2 3 4 5 6
```

**3. `range(start, stop, step)`** — increments/decrements by `step`

```python
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8
```

**Negative Step (counting backwards):**

```python
for i in range(10, 0, -1):
    print(i)
# Output: 10 9 8 7 6 5 4 3 2 1
```

### Important Notes

- `range()` does not include the `stop` value.
- `range()` produces values lazily (it does not store the full list in memory); to view all values, convert it to a list.

```python
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(2, 10, 2)))   # [2, 4, 6, 8]
```

### Example: Sum of Even Numbers from 1 to 50

```python
total = 0
for i in range(2, 51, 2):
    total += i
print("Sum of even numbers =", total)   # 650
```

### Example: Printing Numbers in Reverse Using `range()`

```python
for i in range(10, 0, -2):
    print(i)
# Output: 10 8 6 4 2
```

---

## Unit 1 Summary

- Python is a high-level, interpreted, dynamically-typed language with simple syntax and a large standard library.
- Variables do not require explicit type declaration; data types include `int`, `float`, `complex`, `str`, `bool`, and `None`, among others.
- Type conversion can be implicit (automatic) or explicit (using functions like `int()`, `float()`, `str()`).
- `input()` always returns a string and must be converted for numeric operations; `print()` displays output with configurable `sep` and `end` parameters.
- Conditional statements (`if`, `elif`, `else`) control program flow based on conditions, and logical operators (`and`, `or`, `not`) combine multiple conditions.
- `for` loops iterate over sequences; `while` loops repeat based on a condition; nested loops place one loop inside another.
- `break` exits a loop entirely, while `continue` skips to the next iteration.
- `range()` generates a sequence of numbers commonly used for controlling loop iterations.