# UNIT 3: Functions and Modular Programming (Complete)

## Topics Covered
1. Functions
2. Parameters and Return Values
3. Default Arguments
4. Variable-Length Arguments (`*args` and `**kwargs`)
5. Variable Scope (Local, Global, and Nonlocal)
6. The Mutable Default Argument Pitfall
7. Docstrings
8. Pass by Reference vs Pass by Value in Python
9. Lambda Functions
10. Higher-Order Functions (`map`, `filter`, `reduce`, and Functions as Objects)
11. Recursion
12. Shallow Copy and Deep Copy
13. Modules and Importing
14. The `__name__ == "__main__"` Idiom
15. Package Structure
16. Installing and Using Third-Party Packages (pip)
17. Standard Library Overview
18. Decorators (Introduction)
19. Generator Functions (Introduction)
20. Type Hints (Introduction)

---

## 1. Functions

A function is a named, reusable block of code that performs a specific task. Instead of writing the same logic repeatedly, a function lets you define it once and call it whenever needed.

### Why Use Functions?
- **Reusability** — write the logic once, use it many times.
- **Readability** — breaks a large program into smaller, understandable pieces.
- **Maintainability** — a fix or change only needs to happen in one place.
- **Avoids repetition** — follows the principle of not repeating the same code block.

### Defining and Calling a Function

A function is defined using the `def` keyword, followed by a name, parentheses `()`, and a colon `:`. The function body is indented.

```python
def greet():
    print("Hello, welcome to Python!")

greet()      # calling the function
greet()      # can be called again, as many times as needed
```

**Output:**
```
Hello, welcome to Python!
Hello, welcome to Python!
```

### Function Naming Rules
Function names follow the same rules as variable names: they must start with a letter or underscore, can contain letters, digits, and underscores, and cannot be a Python keyword.

```python
def calculate_total():    # valid, descriptive name
    pass

def 2times():              # invalid, starts with a digit -> SyntaxError
    pass
```

### Example: A Function with Multiple Statements

```python
def display_info():
    print("Course: Python Programming")
    print("Semester: 1")
    print("Topic: Functions")

display_info()
```

### The `pass` Statement

`pass` is a placeholder that does nothing. It is used when a function (or any block) is required syntactically but you are not ready to write its logic yet.

```python
def future_feature():
    pass    # to be implemented later

future_feature()    # runs without error, does nothing
```

---

## 2. Parameters and Return Values

### Parameters (Arguments)

A function can accept input values, called **parameters**, so it can work with different data each time it is called.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ravi")     # Hello, Ravi!
greet("Priya")    # Hello, Priya!
```

**Multiple Parameters:**

```python
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(5, 3)     # Sum: 8
add_numbers(10, 20)   # Sum: 30
```

**Parameters vs Arguments:**
- **Parameter** — the variable name listed in the function definition (e.g., `name` in `def greet(name):`).
- **Argument** — the actual value passed when calling the function (e.g., `"Ravi"` in `greet("Ravi")`).

### Return Values

A function can send a value back to the caller using the `return` statement. This is different from `print()`, which only displays output and does not give the value back for further use.

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)          # 8
print(result * 2)      # 16, since result holds an actual usable value
```

**Difference Between `print()` and `return`:**

```python
def add_print(a, b):
    print(a + b)       # only displays the value

def add_return(a, b):
    return a + b        # sends the value back

x = add_print(5, 3)     # prints 8, but x becomes None
y = add_return(5, 3)    # does not print anything, but y becomes 8

print(x)    # None
print(y)    # 8
```

### Returning Multiple Values

A function can return more than one value, separated by commas. Python packs them into a tuple automatically.

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([4, 8, 15, 16, 23, 42])
print("Minimum:", low)     # Minimum: 4
print("Maximum:", high)    # Maximum: 42
```

### A Function Without `return`

If a function has no `return` statement, it automatically returns `None`.

```python
def say_hello():
    print("Hello")

result = say_hello()
print(result)    # None
```

### `return` Exits the Function Immediately

As soon as a `return` statement executes, the function stops running — any code after it in that path is skipped.

```python
def check_sign(num):
    if num > 0:
        return "Positive"
    if num < 0:
        return "Negative"
    return "Zero"

print(check_sign(5))    # Positive  (stops here, never checks further)
print(check_sign(-3))   # Negative
print(check_sign(0))    # Zero
```

### Example: Function to Check Even or Odd

```python
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))     # Odd
print(check_even_odd(10))    # Even
```

---

## 3. Default Arguments

A default argument allows a parameter to have a pre-set value, which is used if the caller does not provide one.

### Basic Default Argument

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ravi")                 # Hello, Ravi!    (uses default greeting)
greet("Priya", "Good morning") # Good morning, Priya!   (overrides default)
```

### Rule: Default Arguments Must Come After Non-Default Ones

In a function definition, parameters without default values must be listed before parameters with default values.

```python
def example(a, b=10):    # valid
    pass

def example(a=10, b):    # invalid -> SyntaxError
    pass
```

### Example: Function with Multiple Default Arguments

```python
def calculate_price(item, price, discount=0, tax=5):
    final_price = price - discount + (price * tax / 100)
    print(f"{item}: Final Price = {final_price}")

calculate_price("Book", 200)                 # uses default discount and tax
calculate_price("Pen", 50, 5)                 # custom discount, default tax
calculate_price("Bag", 1000, 100, 12)          # all custom values
```

### Using Keyword Arguments

Arguments can also be passed by explicitly naming the parameter, which allows skipping the normal left-to-right order.

```python
def student_info(name, age, course="Python"):
    print(f"Name: {name}, Age: {age}, Course: {course}")

student_info(name="Ravi", age=20)
student_info(age=22, name="Priya", course="Java")   # order does not matter with keyword arguments
```

### Positional vs Keyword Arguments — Summary

| Type | How it works | Example |
|---|---|---|
| Positional argument | Matched to parameters by order | `add(5, 3)` |
| Keyword argument | Matched to parameters by name | `add(a=5, b=3)` |
| Default argument | Used only if caller provides no value | `def add(a, b=0):` |

---

## 4. Variable-Length Arguments (`*args` and `**kwargs`)

Sometimes the number of arguments a function will receive is not known in advance. Python allows a function to accept any number of extra positional or keyword arguments using `*args` and `**kwargs`.

### `*args` — Variable Number of Positional Arguments

`*args` collects any extra positional arguments into a **tuple**.

```python
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(5, 10, 15, 20))  # 50
print(add_all())                 # 0, works even with no arguments
```

**Note:** The name `args` is just a convention — the important part is the `*`. You could write `*numbers` instead, and it would work the same way.

### `**kwargs` — Variable Number of Keyword Arguments

`**kwargs` collects any extra keyword arguments into a **dictionary**.

```python
def print_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="Ravi", age=20, course="Python")
# name: Ravi
# age: 20
# course: Python
```

### Combining Normal Parameters, `*args`, and `**kwargs`

When combined, the order must be: normal parameters, then `*args`, then `**kwargs`.

```python
def student_report(name, *subjects, **details):
    print("Name:", name)
    print("Subjects:", subjects)
    print("Other details:", details)

student_report("Ravi", "Python", "Math", grade="A", age=20)
# Name: Ravi
# Subjects: ('Python', 'Math')
# Other details: {'grade': 'A', 'age': 20}
```

### Why This Is Useful
`*args` and `**kwargs` are especially useful when writing flexible functions whose exact number of inputs cannot be predicted in advance, such as a function that needs to sum any list of numbers, or log any combination of named settings.

---

## 5. Variable Scope (Local, Global, and Nonlocal)

Scope refers to the region of a program where a variable is accessible. Python determines scope based on where a variable is created.

### Local Scope

A variable created inside a function is **local** to that function — it exists only while the function runs and cannot be accessed from outside it.

```python
def my_function():
    x = 10    # local variable
    print(x)

my_function()    # 10
print(x)          # NameError: name 'x' is not defined
```

### Global Scope

A variable created outside any function is **global** — it can be accessed (read) from anywhere in the program, including inside functions.

```python
x = 100    # global variable

def show_value():
    print(x)    # can read the global variable

show_value()    # 100
print(x)          # 100
```

### Modifying a Global Variable Inside a Function

By default, assigning to a variable inside a function creates a **new local variable**, even if a global variable with the same name exists. To modify the actual global variable, the `global` keyword must be used.

```python
counter = 0

def increment_wrong():
    counter = counter + 1    # UnboundLocalError: counter treated as local, but used before assignment

def increment_correct():
    global counter
    counter = counter + 1    # now refers to the global variable

increment_correct()
increment_correct()
print(counter)    # 2
```

### The `nonlocal` Keyword

`nonlocal` is used in a nested function (a function defined inside another function) to modify a variable from the **enclosing function's scope**, which is neither local to the inner function nor fully global.

```python
def outer_function():
    count = 0

    def inner_function():
        nonlocal count
        count += 1
        print("Count:", count)

    inner_function()
    inner_function()
    inner_function()

outer_function()
# Count: 1
# Count: 2
# Count: 3
```

### The LEGB Rule

When Python looks up a variable name, it searches through scopes in this order:

| Order | Scope | Meaning |
|---|---|---|
| 1 | **L**ocal | Inside the current function |
| 2 | **E**nclosing | Inside any outer function (for nested functions) |
| 3 | **G**lobal | At the top level of the file/module |
| 4 | **B**uilt-in | Python's built-in names (like `print`, `len`) |

```python
x = "global x"

def outer():
    x = "enclosing x"

    def inner():
        x = "local x"
        print(x)    # local x   (found at Local scope first)

    inner()
    print(x)        # enclosing x

outer()
print(x)            # global x
```

---

## 6. The Mutable Default Argument Pitfall

A very common beginner mistake is using a **mutable object** (like a list or dictionary) as a default argument value. Python creates the default value only **once**, when the function is defined — not every time it is called — which leads to unexpected shared state.

### The Problem

```python
def add_item(item, basket=[]):    # mutable default argument — risky
    basket.append(item)
    return basket

print(add_item("apple"))     # ['apple']
print(add_item("banana"))    # ['apple', 'banana']   <- unexpected! basket was not empty
```

Both calls used the **same list object** as the default, since it was only created once. The second call's result incorrectly includes the item from the first call.

### The Correct Fix: Use `None` as the Default

```python
def add_item(item, basket=None):
    if basket is None:
        basket = []          # a new list is created fresh on every call
    basket.append(item)
    return basket

print(add_item("apple"))     # ['apple']
print(add_item("banana"))    # ['banana']   <- correct, independent result each time
```

**Rule of Thumb:** Never use a mutable object (list, dictionary, set) directly as a default argument value. Use `None` and create the mutable object inside the function body instead.

---

## 7. Docstrings

A docstring (documentation string) is a special string placed as the first statement inside a function (or module, or class) to describe what it does. Docstrings are written using triple quotes `"""..."""`.

### Writing a Docstring

```python
def add(a, b):
    """Returns the sum of two numbers a and b."""
    return a + b
```

### Accessing a Docstring

A function's docstring can be viewed using the `__doc__` attribute or the built-in `help()` function.

```python
def add(a, b):
    """Returns the sum of two numbers a and b."""
    return a + b

print(add.__doc__)
# Returns the sum of two numbers a and b.

help(add)
# Displays the function's signature and docstring in a readable format
```

### Multi-Line Docstring

For more complex functions, docstrings can span multiple lines, often describing parameters and the return value.

```python
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float): the length of the rectangle
    width (float): the width of the rectangle

    Returns:
    float: the area of the rectangle
    """
    return length * width
```

### Why Docstrings Matter
Docstrings make code self-documenting — anyone reading the function (including the original author, months later) can understand its purpose without reading through the entire implementation.

---

## 8. Pass by Reference vs Pass by Value in Python

This describes how arguments are actually handled when passed into a function. Python's behavior is often described as **"pass by object reference"** — it does not fit neatly into either the traditional "pass by value" or "pass by reference" categories used in other languages.

### Immutable Objects (int, float, str, tuple) — Behave Like "Pass by Value"

When an immutable object is passed to a function and the function reassigns it, the original variable outside the function is **not affected**, because reassignment inside the function just points the local name to a new object.

```python
def modify_number(n):
    n = n + 10
    print("Inside function:", n)

num = 5
modify_number(num)
print("Outside function:", num)

# Inside function: 15
# Outside function: 5    (unchanged)
```

### Mutable Objects (list, dict, set) — Behave Like "Pass by Reference"

When a mutable object is passed to a function and the function modifies it **in place** (without reassigning it), the change is reflected outside the function too, because both the outer variable and the function's parameter point to the same object in memory.

```python
def modify_list(lst):
    lst.append(100)    # modifies the list in place
    print("Inside function:", lst)

numbers = [1, 2, 3]
modify_list(numbers)
print("Outside function:", numbers)

# Inside function: [1, 2, 3, 100]
# Outside function: [1, 2, 3, 100]    (changed!)
```

### But Reassigning a Mutable Object Inside a Function Does Not Affect the Original

```python
def replace_list(lst):
    lst = [99, 98, 97]    # this creates a new local list, does not modify the original
    print("Inside function:", lst)

numbers = [1, 2, 3]
replace_list(numbers)
print("Outside function:", numbers)

# Inside function: [99, 98, 97]
# Outside function: [1, 2, 3]    (unchanged, since reassignment ≠ in-place modification)
```

### Summary Table

| Argument Type | In-Place Modification Inside Function | Reassignment Inside Function |
|---|---|---|
| Immutable (int, str, tuple) | Not possible | Does not affect the original |
| Mutable (list, dict, set) | Affects the original | Does not affect the original |

---

## 9. Lambda Functions

A lambda function is a small, anonymous (unnamed) function defined using the `lambda` keyword. It can take any number of arguments but can only contain a single expression, whose result is automatically returned.

### Syntax

```python
lambda arguments: expression
```

### Basic Lambda Function

```python
square = lambda x: x * x
print(square(5))     # 25
```

**Equivalent Regular Function:**

```python
def square(x):
    return x * x

print(square(5))     # 25
```

### Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(10, 20))    # 30
```

### When to Use Lambda Functions
Lambda functions are most useful for short, simple operations, especially when a function is needed temporarily or passed as an argument to another function. For anything requiring multiple statements or complex logic, a regular `def` function is clearer.

### Using Lambda with `sorted()`

A common real use case is customizing how a sequence is sorted using the `key` parameter.

```python
students = [("Ravi", 85), ("Priya", 92), ("Aman", 78)]

# Sort by marks (the second item of each tuple)
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# [('Aman', 78), ('Ravi', 85), ('Priya', 92)]
```

### Lambda vs Regular Function

| Feature | Lambda Function | Regular Function (`def`) |
|---|---|---|
| Name | Anonymous (usually unnamed) | Has a name |
| Body | Single expression only | Can contain multiple statements |
| Return | Implicit (automatic) | Requires explicit `return` |
| Use Case | Short, one-time operations | Reusable, complex logic |

---

## 10. Higher-Order Functions (`map`, `filter`, `reduce`, and Functions as Objects)

### Functions as First-Class Objects

In Python, functions are treated like any other value — they can be assigned to variables, passed as arguments to other functions, and even returned from other functions. A function that takes another function as an argument, or returns a function, is called a **higher-order function**.

**Assigning a Function to a Variable:**

```python
def greet():
    print("Hello!")

say_hello = greet    # no parentheses, just referencing the function
say_hello()            # Hello!
```

**Passing a Function as an Argument:**

```python
def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply_operation(double, 5))    # 10
```

**Returning a Function from Another Function:**

```python
def make_multiplier(factor):
    def multiplier(num):
        return num * factor
    return multiplier    # returns a function, not a value

times_three = make_multiplier(3)
print(times_three(10))    # 30
```

### `map()` — Applying a Function to Every Item

`map()` applies a given function to every item of a sequence and returns a map object (converted to a list to view it).

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)    # [1, 4, 9, 16, 25]
```

### `filter()` — Selecting Items That Satisfy a Condition

`filter()` keeps only the items of a sequence for which a given function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)    # [2, 4, 6, 8, 10]
```

### `reduce()` — Combining All Items into a Single Value

`reduce()` is not a built-in function — it must be imported from the `functools` module. It repeatedly applies a function to pairs of items in a sequence, reducing it to a single cumulative value.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)    # 15

product = reduce(lambda a, b: a * b, numbers)
print(product)    # 120
```

### `map`, `filter`, `reduce` — Summary

| Function | Purpose | Returns |
|---|---|---|
| `map(func, seq)` | Transforms every item | A new sequence of transformed items |
| `filter(func, seq)` | Keeps items that satisfy a condition | A new sequence of selected items |
| `reduce(func, seq)` | Combines all items into one value | A single value |

---

## 11. Recursion

Recursion occurs when a function calls itself in order to solve a problem by breaking it down into smaller sub-problems of the same type.

### Structure of a Recursive Function

Every recursive function needs two essential parts:
1. **Base Case** — a condition that stops the recursion (without it, the function would call itself forever).
2. **Recursive Case** — the part where the function calls itself with a smaller or simpler input.

```python
def countdown(n):
    if n == 0:               # base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)       # recursive case

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Done!
```

### Example: Factorial Using Recursion

```python
def factorial(n):
    if n == 0 or n == 1:     # base case
        return 1
    else:
        return n * factorial(n - 1)    # recursive case

print(factorial(5))    # 120
```

**How it Works (Trace for `factorial(4)`):**

```
factorial(4) = 4 * factorial(3)
             = 4 * (3 * factorial(2))
             = 4 * (3 * (2 * factorial(1)))
             = 4 * (3 * (2 * 1))
             = 24
```

### Example: Fibonacci Sequence Using Recursion

```python
def fibonacci(n):
    if n <= 1:                 # base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)    # recursive case

for i in range(7):
    print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5 8
```

### Example: Sum of Digits Using Recursion

```python
def sum_of_digits(n):
    if n == 0:                # base case
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)    # recursive case

print(sum_of_digits(1234))    # 10
```

### Recursion vs Iteration

| Feature | Recursion | Iteration (loops) |
|---|---|---|
| Approach | Function calls itself | Uses `for`/`while` loops |
| Readability | Often cleaner for naturally recursive problems | Can be more verbose for the same problem |
| Memory Usage | Higher (each call uses stack memory) | Lower |
| Risk | Can cause a `RecursionError` if the base case is missing or n is too large | No such risk |

**Important:** Every recursive function must eventually reach its base case. A missing or incorrect base case leads to infinite recursion and a `RecursionError: maximum recursion depth exceeded`.

```python
def broken_countdown(n):
    print(n)
    broken_countdown(n - 1)    # no base case, never stops

broken_countdown(5)    # RecursionError after many calls
```

### Recursion Depth Limit

Python limits how many times a function can call itself (its "recursion depth"), to prevent the program from crashing the system by using up all available memory. The default limit can be checked and changed using the `sys` module.

```python
import sys

print(sys.getrecursionlimit())    # 1000 (default, may vary by system)

# sys.setrecursionlimit(2000)   # can be increased, but should be used cautiously
```

### Why Naive Recursion Can Be Slow: Repeated Work

The plain recursive Fibonacci function above recalculates the same values many times. For example, `fibonacci(5)` calls `fibonacci(3)` twice, `fibonacci(2)` three times, and so on, which makes it very slow for larger inputs.

### Memoization — Storing Previously Computed Results

Memoization is an optimization technique where results of expensive function calls are stored (cached), so that if the same input occurs again, the cached result is returned instead of recomputing it.

```python
memo = {}

def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    memo[n] = result
    return result

print(fibonacci_memo(30))    # computes almost instantly, unlike plain recursion
```

---

## 12. Shallow Copy and Deep Copy

When working with mutable objects like lists (especially nested ones), it is important to understand the difference between copying a reference, a shallow copy, and a deep copy.

### Assignment Is Not Copying

```python
original = [1, 2, 3]
reference = original    # NOT a copy — just another name for the same list

reference.append(4)
print(original)    # [1, 2, 3, 4]   <- changed too, since both names point to the same object
```

### Shallow Copy

A shallow copy creates a **new outer object**, but if the original contains nested mutable objects (like a list of lists), the inner objects are still shared between the original and the copy.

```python
import copy

original = [1, 2, [3, 4]]
shallow = copy.copy(original)          # or original.copy(), or original[:]

shallow.append(100)
print(original)    # [1, 2, [3, 4]]       <- outer list unaffected
print(shallow)      # [1, 2, [3, 4], 100]

shallow[2].append(999)                  # modifying the shared nested list
print(original)    # [1, 2, [3, 4, 999]]  <- changed! because the inner list is shared
print(shallow)      # [1, 2, [3, 4, 999], 100]
```

### Deep Copy

A deep copy creates a completely independent copy — including all nested objects — so that changes to the copy never affect the original, at any level.

```python
import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

deep[2].append(999)
print(original)    # [1, 2, [3, 4]]        <- completely unaffected
print(deep)          # [1, 2, [3, 4, 999]]
```

### Shallow Copy vs Deep Copy — Summary

| Method | Outer Object | Nested (Inner) Objects |
|---|---|---|
| Assignment (`b = a`) | Same object (no copy at all) | Same objects |
| Shallow Copy (`copy.copy()`, `.copy()`, `[:]`) | New object | Shared with the original |
| Deep Copy (`copy.deepcopy()`) | New object | Also copied independently |

**Rule of Thumb:** Use a shallow copy when the list contains only simple, immutable items (numbers, strings). Use a deep copy whenever the list contains nested mutable objects (lists within lists, dictionaries within lists, etc.) and full independence from the original is required.

---

## 13. Modules and Importing

A module is simply a Python file (`.py`) containing reusable code — functions, variables, or classes — that can be imported and used in another Python program.

### Why Use Modules?
- Organizes code into logical, manageable files.
- Allows code reuse across multiple programs.
- Avoids rewriting the same functionality repeatedly.
- Makes large projects easier to maintain.

### Importing a Built-in Module

Python comes with many built-in modules. The `math` module, for example, provides mathematical functions and constants.

```python
import math

print(math.sqrt(25))      # 5.0
print(math.pi)              # 3.141592653589793
print(math.factorial(5))    # 120
```

### Different Ways to Import

**1. Importing the Whole Module:**

```python
import math
print(math.sqrt(16))    # 4.0
```

**2. Importing Specific Items from a Module:**

```python
from math import sqrt, pi

print(sqrt(16))    # 4.0, no need to write math.sqrt
print(pi)            # 3.141592653589793
```

**3. Importing with an Alias:**

```python
import math as m
print(m.sqrt(16))    # 4.0
```

**4. Importing Everything from a Module (generally avoided):**

```python
from math import *
print(sqrt(16))    # works, but can cause naming conflicts in larger programs
```

### Creating Your Own Module

Any `.py` file can be used as a module. If you create a file named `calculator.py` with the following content:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

It can then be imported and used in another file (as long as both files are in the same folder):

```python
# main.py
import calculator

print(calculator.add(10, 5))        # 15
print(calculator.subtract(10, 5))   # 5
```

### The `random` Module (Another Commonly Used Built-in Module)

```python
import random

print(random.randint(1, 10))     # random integer between 1 and 10 (inclusive)
print(random.choice(["apple", "banana", "cherry"]))   # randomly picks one item
```

### Checking What a Module Contains

The built-in `dir()` function lists all the names (functions, variables) available in a module.

```python
import math
print(dir(math))    # lists everything available inside the math module
```

---

## 14. The `__name__ == "__main__"` Idiom

Every Python file has a built-in variable called `__name__`. When a file is run directly, `__name__` is automatically set to `"__main__"`. When the same file is imported into another file as a module, `__name__` is instead set to the module's filename.

### Why This Matters

This allows a Python file to behave differently depending on whether it is being run directly or imported elsewhere — most commonly, to prevent certain code (like test code or a demo) from running automatically when the file is only meant to be imported.

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # This block only runs when calculator.py is executed directly,
    # NOT when it is imported into another file.
    print(add(5, 3))
    print(subtract(5, 3))
```

If another file does `import calculator`, the `print()` statements inside the `if __name__ == "__main__":` block will **not** run — only the function definitions become available for use.

### Why This Is Considered Good Practice
It keeps a module's "demo" or "test" code separate from its reusable functions, so the module behaves purely as a toolbox when imported, without unexpectedly printing or executing things.

---

## 15. Package Structure

A package is a way of organizing related modules together into a single directory. While a module is a single `.py` file, a package is a **folder** containing multiple related modules (and a special file that marks it as a package).

### Structure of a Simple Package

```
mypackage/
    __init__.py
    calculator.py
    converter.py
```

- `mypackage/` — the package (a folder).
- `__init__.py` — a special, often empty, file that tells Python this folder should be treated as a package. (In modern Python, packages can work without it, but including it is still common practice for clarity and compatibility.)
- `calculator.py` and `converter.py` — individual modules within the package.

### Example Package Contents

```python
# mypackage/calculator.py
def add(a, b):
    return a + b
```

```python
# mypackage/converter.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
```

### Importing from a Package

```python
from mypackage import calculator
print(calculator.add(5, 10))    # 15

from mypackage.converter import celsius_to_fahrenheit
print(celsius_to_fahrenheit(30))    # 86.0
```

### Module vs Package

| Feature | Module | Package |
|---|---|---|
| Definition | A single `.py` file | A folder containing multiple modules |
| Example | `math.py` | `mypackage/` containing several `.py` files |
| Import Example | `import math` | `import mypackage.calculator` |
| Purpose | Groups related functions/variables | Groups related modules together |

### Why Packages Matter
As a project grows larger, keeping all code in a single file becomes unmanageable. Packages allow large codebases (like NumPy or Django) to be organized into logical sub-sections, each handling a specific part of the functionality.

---

## 16. Installing and Using Third-Party Packages (pip)

Not all useful Python code comes built into the standard library. Third-party packages — written by other developers and published for public use — can be installed using Python's package manager, `pip`.

### Installing a Package

Run this command in the terminal (not inside a Python script):

```bash
pip install requests
```

This downloads and installs the `requests` package (commonly used for making HTTP requests), along with any dependencies it needs, from the Python Package Index (PyPI).

### Using an Installed Package

Once installed, a third-party package is imported the same way as a built-in module:

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

### Checking Installed Packages

```bash
pip list              # lists all installed packages and their versions
pip show requests     # shows detailed information about a specific package
```

### How Python Finds Modules: `sys.path`

When you write `import module_name`, Python searches through a list of directories to find it. This list is stored in `sys.path`.

```python
import sys
print(sys.path)
```

`sys.path` typically includes the current script's directory, the standard library's location, and the folder where pip-installed packages are stored — which is why both your own modules and pip-installed packages can be imported the same way.

### Built-in Modules vs Third-Party Packages

| Type | Source | Needs Installation? | Example |
|---|---|---|---|
| Built-in (Standard Library) | Comes with Python itself | No | `math`, `random`, `os` |
| Third-Party | Published by other developers on PyPI | Yes, via `pip install` | `requests`, `numpy`, `pandas` |

---

## 17. Standard Library Overview

The Python Standard Library is the collection of built-in modules that come packaged with every Python installation, requiring no separate installation. It provides ready-made solutions for many common programming tasks.

### Commonly Used Standard Library Modules

**`math` — Mathematical operations:**

```python
import math

print(math.sqrt(49))        # 7.0
print(math.ceil(4.2))        # 5    (rounds up)
print(math.floor(4.8))       # 4    (rounds down)
print(math.pow(2, 3))        # 8.0
```

**`random` — Generating random values:**

```python
import random

print(random.random())           # random float between 0.0 and 1.0
print(random.randint(1, 100))     # random integer between 1 and 100
print(random.choice([1, 2, 3]))   # random item from a sequence
```

**`datetime` — Working with dates and times:**

```python
import datetime

today = datetime.date.today()
print(today)                 # e.g., 2026-10-05

now = datetime.datetime.now()
print(now)                   # current date and time
```

**`os` — Interacting with the operating system:**

```python
import os

print(os.getcwd())           # prints the current working directory
print(os.listdir("."))       # lists files/folders in the current directory
```

**`sys` — System-specific parameters and functions:**

```python
import sys

print(sys.version)           # prints the installed Python version
```

**`string` — Common string constants:**

```python
import string

print(string.ascii_lowercase)    # abcdefghijklmnopqrstuvwxyz
print(string.digits)              # 0123456789
```

**`functools` — Tools for working with functions:**

```python
from functools import reduce

numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, numbers))    # 10
```

**`itertools` — Tools for working with iterators efficiently:**

```python
import itertools

# Generates all possible pairs from the list
pairs = list(itertools.combinations([1, 2, 3], 2))
print(pairs)    # [(1, 2), (1, 3), (2, 3)]
```

### Why the Standard Library Matters
Because these modules come pre-installed with Python, they allow a programmer to perform common tasks (math operations, random values, date handling, file system access) without writing that logic from scratch or installing anything extra. This is often summarized by Python's philosophy of being a "batteries included" language.

### Example: Using Multiple Standard Library Modules Together

```python
import random
import datetime

name = "Ravi"
lucky_number = random.randint(1, 100)
today = datetime.date.today()

print(f"Hello {name}, today is {today}. Your lucky number is {lucky_number}.")
```

---

## 18. Decorators (Introduction)

A decorator is a function that takes another function as input, adds some extra behavior to it, and returns a new function — without permanently changing the original function's own code. Decorators build directly on the "functions as objects" and "returning a function" ideas from Section 10.

### A Simple Decorator Example

```python
def my_decorator(func):
    def wrapper():
        print("Something happens before the function runs.")
        func()
        print("Something happens after the function runs.")
    return wrapper

def say_hello():
    print("Hello!")

decorated_hello = my_decorator(say_hello)
decorated_hello()

# Something happens before the function runs.
# Hello!
# Something happens after the function runs.
```

### Using the `@` Symbol (Syntactic Sugar)

Python provides a cleaner way to apply a decorator using the `@` symbol directly above the function definition, instead of manually reassigning it.

```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before the function runs.
# Hello!
# After the function runs.
```

`@my_decorator` above `def say_hello():` is exactly equivalent to writing `say_hello = my_decorator(say_hello)`.

### Practical Example: A Timing Decorator

```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken: {end - start:.4f} seconds")
    return wrapper

@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total += i

slow_function()
# Time taken: 0.0XXX seconds
```

---

## 19. Generator Functions (Introduction)

A generator function is a special kind of function that produces a sequence of values one at a time, instead of computing and returning them all at once. It uses the `yield` keyword instead of `return`.

### A Simple Generator

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
# 1
# 2
# 3
# 4
# 5
```

### `yield` vs `return`

| Feature | `return` | `yield` |
|---|---|---|
| Effect | Ends the function, sends back one value | Pauses the function, sends back one value, and can resume later |
| Function Type | Regular function | Generator function |
| Memory Usage | Entire result is built and stored at once | Values are produced one at a time (more memory-efficient for large sequences) |

### Why Generators Are Useful

A generator does not store the entire sequence in memory at once, which makes it efficient for working with very large sequences or data streams.

```python
def even_numbers_up_to(n):
    for i in range(0, n + 1, 2):
        yield i

even_gen = even_numbers_up_to(10)
print(next(even_gen))    # 0
print(next(even_gen))    # 2
print(next(even_gen))    # 4

# Remaining values can still be accessed with a for loop
for num in even_gen:
    print(num)
# 6
# 8
# 10
```

---

## 20. Type Hints (Introduction)

Type hints (also called type annotations) allow a programmer to indicate the expected data type of function parameters and return values. Python does not enforce these types at runtime — they exist to improve code readability and help tools catch potential errors before running the program.

### Basic Syntax

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))    # 8
```

Here, `a: int` and `b: int` indicate that both parameters are expected to be integers, and `-> int` indicates the function is expected to return an integer.

### Type Hints Are Not Enforced

Python will not raise an error even if the actual argument type does not match the hint — type hints are purely informational unless checked by an external tool.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("5", "3"))    # "53"   <- still runs; Python does not enforce the hint
```

### Type Hints with Variables

```python
age: int = 20
name: str = "Ravi"
price: float = 99.99
is_active: bool = True
```

### Why Use Type Hints
- Makes function signatures self-documenting (what type of input is expected, what is returned).
- Helps code editors and IDEs provide better autocomplete and error-checking.
- Makes larger codebases easier to understand and maintain, especially when working in a team.

---

## Unit 3 Summary

- Functions are reusable, named blocks of code defined with `def`, improving code organization, readability, and maintainability. `return` sends a value back for further use, unlike `print()`, which only displays it.
- Default arguments provide a fallback value for a parameter, and must be declared after any non-default parameters; `*args` and `**kwargs` let a function accept any number of extra positional or keyword arguments.
- Variable scope determines where a name is accessible: local (inside a function), enclosing (in an outer function), global (module-level), and built-in, searched in that order (the LEGB rule); `global` and `nonlocal` allow modifying variables outside the current local scope.
- A mutable object (like a list) should never be used directly as a default argument value, since it is created only once and shared across calls; use `None` and create it fresh inside the function instead.
- Docstrings (`"""..."""`) document what a function does and can be viewed with `.__doc__` or `help()`.
- Python passes arguments by object reference: reassigning a parameter inside a function never affects the caller's variable, but in-place modification of a mutable object does.
- Lambda functions are small, single-expression anonymous functions, often used with `sorted()`, `map()`, and `filter()`; `reduce()` (from `functools`) combines a sequence into a single value. Functions in Python are first-class objects — they can be assigned, passed around, and returned from other functions.
- Recursion is a technique where a function calls itself, always requiring a base case to stop and a recursive case to progress toward it; Python limits recursion depth, and memoization can avoid the repeated work of naive recursive calls.
- A shallow copy duplicates only the outer object, while nested mutable objects remain shared with the original; a deep copy (`copy.deepcopy()`) duplicates everything, including nested objects, independently.
- Modules are individual `.py` files containing reusable code, imported using `import`, `from ... import`, or with an alias (`as`); the `if __name__ == "__main__":` idiom lets a file behave differently when run directly versus when imported.
- A package is a folder of related modules (optionally marked with `__init__.py`); third-party packages not included with Python are installed using `pip install` and found through `sys.path`.
- The Python Standard Library (`math`, `random`, `datetime`, `os`, `sys`, `string`, `functools`, `itertools`, and others) provides ready-to-use modules for common tasks without needing external installation.
- Decorators wrap a function to add extra behavior without changing its original code, commonly applied using the `@` syntax. Generator functions (`yield`) produce values one at a time instead of all at once, which is more memory-efficient for large sequences. Type hints annotate expected parameter and return types for readability, without being enforced by Python itself.