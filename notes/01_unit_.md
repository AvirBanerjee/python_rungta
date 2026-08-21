# UNIT 1: Python Fundamentals

## Topics Covered
1. Python Features and Installation
2. Variables and Data Types
3. Type Conversion
4. Input and Output Functions
5. Python Operators
6. Conditional Statements
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

## 5. Python Operators

Operators are special symbols in Python that perform operations on values (called operands). Operators are the building blocks used inside expressions and conditions, so it is important to understand them before moving on to conditional statements and loops.

Python organizes operators into the following categories:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison (Relational) Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

### 5.1 Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations such as addition, subtraction, multiplication, and division.

| Operator | Name | Description | Example | Result |
|---|---|---|---|---|
| `+` | Addition | Adds two operands | `5 + 3` | `8` |
| `-` | Subtraction | Subtracts right operand from left | `5 - 3` | `2` |
| `*` | Multiplication | Multiplies two operands | `5 * 3` | `15` |
| `/` | Division | Divides left operand by right, always returns a float | `5 / 2` | `2.5` |
| `//` | Floor Division | Divides and rounds down to the nearest whole number | `5 // 2` | `2` |
| `%` | Modulus | Returns the remainder of division | `5 % 2` | `1` |
| `**` | Exponentiation | Raises left operand to the power of right operand | `5 ** 2` | `25` |

**Examples:**

```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333333333333335
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000
```

```python
# Checking even or odd using modulus
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Commonly Confused: `/` vs `//`**

- `/` is **true division** — it always returns a `float`, even if the numbers divide evenly.
- `//` is **floor division** — it divides and then rounds the result **down** to the nearest whole number (towards negative infinity), returning an `int` when both operands are `int`.

```python
print(7 / 2)     # 3.5   (true division, float result)
print(7 // 2)    # 3     (floor division, whole number result)
print(-7 // 2)   # -4    (rounds down, not towards zero)
```

### 5.2 Assignment Operators

Assignment operators are used to assign values to variables. Python also provides shorthand assignment operators that combine an arithmetic operation with assignment.

| Operator | Name | Description | Example | Equivalent To |
|---|---|---|---|---|
| `=` | Assign | Assigns value on the right to variable on the left | `a = 5` | `a = 5` |
| `+=` | Add and Assign | Adds and reassigns | `a += 3` | `a = a + 3` |
| `-=` | Subtract and Assign | Subtracts and reassigns | `a -= 3` | `a = a - 3` |
| `*=` | Multiply and Assign | Multiplies and reassigns | `a *= 3` | `a = a * 3` |
| `/=` | Divide and Assign | Divides and reassigns | `a /= 3` | `a = a / 3` |
| `//=` | Floor Divide and Assign | Floor divides and reassigns | `a //= 3` | `a = a // 3` |
| `%=` | Modulus and Assign | Takes modulus and reassigns | `a %= 3` | `a = a % 3` |
| `**=` | Exponent and Assign | Raises to power and reassigns | `a **= 3` | `a = a ** 3` |

**Examples:**

```python
a = 10
a += 5      # a = a + 5
print(a)    # 15

b = 20
b -= 8
print(b)    # 12

c = 4
c **= 2
print(c)    # 16
```

**Commonly Confused: `=` vs `==`**

- `=` is the **assignment operator**. It stores a value in a variable and does **not** compare anything.
- `==` is the **comparison operator**. It checks whether two values are equal and returns `True` or `False`.

```python
x = 5        # assigns 5 to x
print(x == 5)   # True, compares x with 5

if x = 5:        # SyntaxError: invalid syntax, cannot use = inside a condition
    pass
```

A very common beginner mistake is writing `if x = 5:` instead of `if x == 5:`. Python does not allow assignment inside a condition, so this raises a `SyntaxError`.

### 5.3 Comparison (Relational) Operators

Comparison operators compare two values and always return a Boolean result: `True` or `False`. They are heavily used inside `if` conditions and loops.

| Operator | Name | Description | Example | Result |
|---|---|---|---|---|
| `==` | Equal to | True if both values are equal | `5 == 5` | `True` |
| `!=` | Not equal to | True if values are not equal | `5 != 3` | `True` |
| `>` | Greater than | True if left is greater than right | `5 > 3` | `True` |
| `<` | Less than | True if left is less than right | `5 < 3` | `False` |
| `>=` | Greater than or equal to | True if left is greater than or equal to right | `5 >= 5` | `True` |
| `<=` | Less than or equal to | True if left is less than or equal to right | `5 <= 3` | `False` |

**Examples:**

```python
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a >= 10)  # True
```

```python
marks = 40
print(marks >= 33)   # True, used commonly for pass/fail checks
```

Comparison operators are used extensively with conditional statements, covered in the next section.

### 5.4 Logical Operators

Logical operators are used to combine multiple conditions into a single Boolean result.

| Operator | Name | Description | Example |
|---|---|---|---|
| `and` | Logical AND | True only if both conditions are true | `a > 5 and b < 10` |
| `or` | Logical OR | True if at least one condition is true | `a > 5 or b < 10` |
| `not` | Logical NOT | Reverses the Boolean result | `not(a > 5)` |

**Examples:**

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Allowed to enter")
else:
    print("Not allowed")
```

```python
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today")
else:
    print("Work day")
```

```python
is_raining = False

if not is_raining:
    print("You can go for a walk")
```

**Truth Table Reference:**

| A | B | A and B | A or B | not A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

**Combined Example:**

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
```

**Commonly Confused: `and` vs `or`**

- `and` requires **both** conditions to be `True` for the overall result to be `True`. If even one condition is `False`, the result is `False`.
- `or` requires **at least one** condition to be `True` for the overall result to be `True`. It is only `False` when both conditions are `False`.

```python
age = 16
has_permission = True

print(age >= 18 and has_permission)   # False, age condition fails
print(age >= 18 or has_permission)    # True, second condition is enough
```

### 5.5 Identity Operators

Identity operators check whether two variables point to the **same object in memory**, not just whether their values are equal.

| Operator | Name | Description | Example |
|---|---|---|---|
| `is` | Identity | True if both variables refer to the same object | `a is b` |
| `is not` | Negative Identity | True if both variables do not refer to the same object | `a is not b` |

**Examples:**

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True, values are equal
print(a is b)    # False, different objects in memory
print(a is c)    # True, c refers to the same object as a
```

```python
x = None
if x is None:
    print("x has no value")
```

```python
p = 5
q = 5
print(p is q)   # True, small integers are cached by Python
```

**Commonly Confused: `==` vs `is`**

- `==` compares the **values** of two objects.
- `is` compares the **identity** (memory location) of two objects.

Two variables can hold equal values but be stored as separate objects in memory. It is best practice to use `is` only when comparing to `None`, `True`, or `False`, and use `==` for comparing values.

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)   # True, same values
print(list1 is list2)   # False, different objects
```

### 5.6 Membership Operators

Membership operators check whether a value exists within a sequence such as a string, list, or tuple.

| Operator | Name | Description | Example |
|---|---|---|---|
| `in` | Membership | True if the value is found in the sequence | `'a' in 'apple'` |
| `not in` | Negative Membership | True if the value is not found in the sequence | `'z' not in 'apple'` |

**Examples:**

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)       # True
print("mango" in fruits)        # False
print("mango" not in fruits)    # True
```

```python
sentence = "Python is fun"
print("fun" in sentence)        # True
print("Java" in sentence)       # False
```

```python
# Common use inside a condition
name = "Ravi"
if "R" in name:
    print("Name contains the letter R")
```

**Commonly Confused: `in` vs `not in`**

- `in` returns `True` if the value **is present** in the sequence.
- `not in` returns `True` if the value **is absent** from the sequence.

They are exact opposites of each other for the same check, and both are commonly used to validate whether user input or data exists in a collection before processing it further.

### 5.7 Bitwise Operators

Bitwise operators work directly on the binary (bit-level) representation of integers. They are less commonly used by beginners but are important for low-level operations, flags, and optimization.

| Operator | Name | Description | Example | Result |
|---|---|---|---|---|
| `&` | Bitwise AND | Sets each bit to 1 if both bits are 1 | `5 & 3` | `1` |
| `\|` | Bitwise OR | Sets each bit to 1 if at least one bit is 1 | `5 \| 3` | `7` |
| `^` | Bitwise XOR | Sets each bit to 1 if only one of the bits is 1 | `5 ^ 3` | `6` |
| `~` | Bitwise NOT | Inverts all the bits | `~5` | `-6` |
| `<<` | Left Shift | Shifts bits to the left, filling with zeros | `5 << 1` | `10` |
| `>>` | Right Shift | Shifts bits to the right | `5 >> 1` | `2` |

**Examples:**

```python
a = 5    # binary: 0101
b = 3    # binary: 0011

print(a & b)    # 1  (0001)
print(a | b)    # 7  (0111)
print(a ^ b)    # 6  (0110)
print(~a)       # -6
print(a << 1)   # 10 (1010)
print(a >> 1)   # 2  (0010)
```

```python
# Checking if a number is even using bitwise AND
num = 8
if num & 1 == 0:
    print("Even")
else:
    print("Odd")
```

Bitwise operators work on the binary form of numbers, unlike arithmetic operators, which work directly on the decimal values.

---

### Practice Questions: Python Operators

**Arithmetic Operators**

1. What will `print(15 / 4)` output?
2. What will `print(15 // 4)` output?
3. Identify the operator used in the expression `10 % 3` and state what it returns.
4. Find the result of `2 ** 5`.
5. Write a program that takes two numbers as input and prints their sum, difference, product, and quotient.

**Assignment Operators**

1. What is the value of `x` after the following code runs?
   ```python
   x = 10
   x += 5
   x *= 2
   ```
2. Rewrite `a = a - 4` using a shorthand assignment operator.
3. What is the output of the following code?
   ```python
   y = 20
   y //= 3
   print(y)
   ```
4. Identify the operator used in `count **= 2` and explain what it does.
5. Write a program that starts with a variable `total = 0` and uses `+=` inside a loop to add numbers from 1 to 5.

**Comparison Operators**

1. What will `print(10 != 10)` output?
2. Find the result of `7 <= 7`.
3. Identify the operator that checks whether two values are NOT equal.
4. What is the output of the following code?
   ```python
   a = 5
   b = 8
   print(a > b)
   ```
5. Write a program that checks whether a user-entered number is greater than, less than, or equal to 100.

**Logical Operators**

1. What will `print(True and False)` output?
2. Find the result of `(5 > 2) or (3 > 10)`.
3. Identify the operator that reverses a Boolean value.
4. What is the output of the following code?
   ```python
   age = 20
   has_license = False
   print(age >= 18 and has_license)
   ```
5. Write a program that checks if a number is between 10 and 50 (inclusive) using logical operators.

**Identity Operators**

1. What is the difference between `==` and `is`? Explain in one or two lines.
2. What will the following code print?
   ```python
   a = [1, 2]
   b = [1, 2]
   print(a is b)
   ```
3. Identify the operator that checks whether two variables refer to the same object in memory.
4. What is the output of the following code?
   ```python
   x = None
   print(x is None)
   ```
5. Write a short program using `is` to check whether a variable is `None`.

**Membership Operators**

1. What will `print("e" in "hello")` output?
2. Find the result of `10 not in [1, 2, 3, 4, 5]`.
3. Identify the operator used to check whether a value is absent from a list.
4. What is the output of the following code?
   ```python
   colors = ["red", "green", "blue"]
   print("yellow" in colors)
   ```
5. Write a program that checks whether a user-entered fruit name exists in a given list of fruits.

**Bitwise Operators**

1. What will `print(6 & 3)` output?
2. Find the result of `6 | 3`.
3. Identify the operator used to invert all bits of a number.
4. What is the output of the following code?
   ```python
   print(4 << 2)
   ```
5. Write a program that uses the bitwise AND operator (`& 1`) to check whether a number is even or odd.

---

## 6. Conditional Statements

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

Conditions in `if` statements are commonly built using comparison and logical operators, covered in the Python Operators section above (Section 5).

### Short-Hand `if` (Ternary-like)

```python
a = 10
b = 20
max_value = a if a > b else b
print(max_value)   # 20
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
- Python operators are grouped into seven categories: arithmetic, assignment, comparison, logical, identity, membership, and bitwise, each used for a different kind of operation on values.
- Conditional statements (`if`, `elif`, `else`) control program flow based on conditions built using comparison and logical operators.
- `for` loops iterate over sequences; `while` loops repeat based on a condition; nested loops place one loop inside another.
- `break` exits a loop entirely, while `continue` skips to the next iteration.
- `range()` generates a sequence of numbers commonly used for controlling loop iterations.