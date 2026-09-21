# UNIT 2: Data Structures in Python

## Topics Covered
1. Lists and Tuples
2. Indexing and Slicing
3. List Methods
4. Nested Lists
5. Strings and String Methods
6. String Formatting
7. Dictionaries and Key-Value Operations
8. Sets and Set Operations

---

## 1. Lists and Tuples

### Lists

A list is an ordered, mutable (changeable) collection that can hold items of different data types. Lists are defined using square brackets `[]`, with items separated by commas.

```python
numbers = [10, 20, 30, 40]
names = ["Ravi", "Priya", "Aman"]
mixed = [1, "hello", 3.14, True]
empty_list = []
```

**Key Properties of Lists:**
- **Ordered** — items maintain the position in which they were inserted.
- **Mutable** — items can be changed, added, or removed after creation.
- **Allows duplicates** — the same value can appear more than once.
- **Heterogeneous** — a single list can hold different data types together.

**Creating a List:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)          # ['apple', 'banana', 'cherry']
print(type(fruits))    # <class 'list'>
```

**Modifying a List:**

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"        # replacing an item by position
print(fruits)               # ['apple', 'mango', 'cherry']
```

**Length of a List:**

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))     # 3
```

**Iterating Over a List:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Checking Membership:**

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)       # True
print("mango" not in fruits)    # True
```

### Tuples

A tuple is an ordered, **immutable** (unchangeable) collection. Tuples are defined using parentheses `()`, with items separated by commas.

```python
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (5,)     # comma is required for a single-item tuple
empty_tuple = ()
```

**Key Properties of Tuples:**
- **Ordered** — same as lists, items retain their position.
- **Immutable** — once created, items cannot be changed, added, or removed.
- **Allows duplicates.**
- **Faster than lists** for fixed data, since Python does not need to allow for changes in size.

**Attempting to Modify a Tuple (Error):**

```python
colors = ("red", "green", "blue")
colors[0] = "yellow"   # TypeError: 'tuple' object does not support item assignment
```

**Tuple Unpacking:**

A very common and useful tuple feature — assigning tuple values directly to variables.

```python
point = (4, 5)
x, y = point
print(x)    # 4
print(y)    # 5
```

**Length and Membership (same as lists):**

```python
colors = ("red", "green", "blue")
print(len(colors))          # 3
print("red" in colors)      # True
```

### List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutability | Mutable (can be changed) | Immutable (cannot be changed) |
| Speed | Slower | Faster |
| Use Case | Data that may change | Data that should stay constant |
| Methods available | Many (append, remove, sort, etc.) | Very few (count, index) |

**When to use which:**
Use a **list** when the collection needs to grow, shrink, or be modified during the program (e.g., a shopping cart). Use a **tuple** when the data should remain fixed and unchanged (e.g., the coordinates of a fixed point, days of the week).

---

## 2. Indexing and Slicing

Indexing and slicing allow you to access individual items or a range of items from a sequence (list, tuple, or string) using their position.

### Indexing

Every item in a sequence has a position number called an **index**, starting from `0` for the first item. Python also supports **negative indexing**, where `-1` refers to the last item.

```python
fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])     # apple   (first item)
print(fruits[2])     # cherry  (third item)
print(fruits[-1])    # mango   (last item)
print(fruits[-2])    # cherry  (second-last item)
```

**Index Positions (Visual Reference):**

```
Value:          "apple"  "banana"  "cherry"  "mango"
Positive index:    0        1         2         3
Negative index:   -4       -3        -2        -1
```

**Accessing an Invalid Index:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[5])    # IndexError: list index out of range
```

### Slicing

Slicing extracts a portion (sub-sequence) of a list, tuple, or string using the syntax:

```python
sequence[start:stop:step]
```

- `start` — index to begin from (inclusive). Default is `0`.
- `stop` — index to stop before (exclusive, not included).
- `step` — how many positions to move each time. Default is `1`.

**Basic Slicing:**

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])     # [20, 30, 40]     (index 1 to 3)
print(numbers[:3])      # [10, 20, 30]     (start omitted, begins from 0)
print(numbers[3:])      # [40, 50, 60]     (stop omitted, goes till end)
print(numbers[:])       # [10, 20, 30, 40, 50, 60]   (full copy)
```

**Slicing with Step:**

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])     # [10, 30, 50]     (every second item)
print(numbers[1::2])    # [20, 40, 60]     (every second item, starting index 1)
```

**Negative Slicing:**

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[-3:])     # [40, 50, 60]     (last three items)
print(numbers[:-2])     # [10, 20, 30, 40] (everything except last two)
print(numbers[::-1])    # [60, 50, 40, 30, 20, 10]   (reversed list)
```

**Slicing a Tuple:**

```python
colors = ("red", "green", "blue", "yellow")
print(colors[1:3])      # ('green', 'blue')
```

**Slicing a String:**
Strings also support indexing and slicing since a string is a sequence of characters.

```python
word = "Python"
print(word[0])       # P
print(word[-1])       # n
print(word[0:3])      # Pyt
print(word[::-1])     # nohtyP  (reversed string)
```

**Important Note:** Slicing never raises an `IndexError`, even if the range goes beyond the sequence length — it simply returns as much as is available.

```python
numbers = [10, 20, 30]
print(numbers[1:10])    # [20, 30]   (no error, just returns what exists)
```

---

## 3. List Methods

Python provides many built-in methods to work with lists. These methods modify or operate on the list directly.

### Adding Elements

| Method | Description | Example |
|---|---|---|
| `append(x)` | Adds a single item to the end of the list | `lst.append(5)` |
| `insert(i, x)` | Inserts an item `x` at index `i` | `lst.insert(1, "new")` |
| `extend(iterable)` | Adds all items from another list (or iterable) to the end | `lst.extend([4, 5, 6])` |

```python
fruits = ["apple", "banana"]

fruits.append("cherry")
print(fruits)      # ['apple', 'banana', 'cherry']

fruits.insert(1, "mango")
print(fruits)      # ['apple', 'mango', 'banana', 'cherry']

fruits.extend(["kiwi", "grape"])
print(fruits)      # ['apple', 'mango', 'banana', 'cherry', 'kiwi', 'grape']
```

### Removing Elements

| Method | Description | Example |
|---|---|---|
| `remove(x)` | Removes the first occurrence of value `x` | `lst.remove("apple")` |
| `pop(i)` | Removes and returns the item at index `i` (last item if omitted) | `lst.pop()` |
| `clear()` | Removes all items from the list | `lst.clear()` |

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")
print(fruits)      # ['apple', 'cherry', 'banana']   (removes only the first match)

removed_item = fruits.pop(0)
print(removed_item)   # apple
print(fruits)          # ['cherry', 'banana']

fruits.clear()
print(fruits)      # []
```

**Difference between `remove()` and `pop()`:**
- `remove(x)` deletes by **value** and does not return anything.
- `pop(i)` deletes by **index** and returns the removed item.

### Searching and Counting

| Method | Description | Example |
|---|---|---|
| `index(x)` | Returns the index of the first occurrence of `x` | `lst.index("apple")` |
| `count(x)` | Returns how many times `x` appears in the list | `lst.count("apple")` |

```python
numbers = [10, 20, 30, 20, 40, 20]

print(numbers.index(20))    # 1   (first occurrence)
print(numbers.count(20))    # 3   (appears three times)
```

### Sorting and Reversing

| Method | Description | Example |
|---|---|---|
| `sort()` | Sorts the list in ascending order (modifies the original list) | `lst.sort()` |
| `sort(reverse=True)` | Sorts the list in descending order | `lst.sort(reverse=True)` |
| `reverse()` | Reverses the order of items in the list | `lst.reverse()` |

```python
numbers = [40, 10, 30, 20]

numbers.sort()
print(numbers)      # [10, 20, 30, 40]

numbers.sort(reverse=True)
print(numbers)      # [40, 30, 20, 10]

numbers.reverse()
print(numbers)      # [10, 20, 30, 40]
```

**Note:** `sort()` changes the original list and returns `None`. To get a **new sorted list** without changing the original, use the built-in `sorted()` function instead:

```python
numbers = [40, 10, 30, 20]
new_list = sorted(numbers)
print(new_list)    # [10, 20, 30, 40]
print(numbers)      # [40, 10, 30, 20]   (original unchanged)
```

### Copying a List

```python
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)

print(original)    # [1, 2, 3]        (unaffected)
print(copy_list)   # [1, 2, 3, 4]
```

**Important:** Simply writing `copy_list = original` does **not** create a new list — it only creates another reference to the same list. Changes to one will affect the other. Use `.copy()`, or slicing `original[:]`, to create an independent copy.

```python
original = [1, 2, 3]
not_a_copy = original          # same list, just a new name
not_a_copy.append(4)

print(original)    # [1, 2, 3, 4]   (also changed!)
```

### Summary Table of Common List Methods

| Method | Purpose |
|---|---|
| `append(x)` | Add one item to the end |
| `insert(i, x)` | Add item at a specific position |
| `extend(iterable)` | Add multiple items to the end |
| `remove(x)` | Remove first matching value |
| `pop(i)` | Remove and return item by index |
| `clear()` | Remove all items |
| `index(x)` | Find position of a value |
| `count(x)` | Count occurrences of a value |
| `sort()` | Sort the list in place |
| `reverse()` | Reverse the list in place |
| `copy()` | Create a shallow copy |

---

## 4. Nested Lists

A nested list is a list that contains other lists as its elements. Nested lists are commonly used to represent grids, tables, or matrices.

### Creating a Nested List

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Here, `matrix` is a list containing three inner lists, each representing a row.

### Accessing Elements in a Nested List

To access an element, use two sets of square brackets — the first for the outer list (row), the second for the inner list (column).

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])        # [1, 2, 3]    (entire first row)
print(matrix[0][0])     # 1            (first row, first column)
print(matrix[1][2])     # 6            (second row, third column)
print(matrix[2][-1])    # 9            (third row, last column)
```

### Modifying Elements in a Nested List

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][1] = 50
print(matrix)     # [[1, 2, 3], [4, 50, 6], [7, 8, 9]]
```

### Iterating Over a Nested List

Since a nested list contains lists inside it, a nested `for` loop is used to access every individual element.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

### Example: Sum of All Elements in a Nested List

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0

for row in matrix:
    for item in row:
        total += item

print("Sum =", total)   # Sum = 45
```

### Example: Creating a Nested List of Different Sizes (Jagged List)

A nested list does not require inner lists to be the same length.

```python
jagged = [[1, 2], [3, 4, 5], [6]]

print(jagged[0])    # [1, 2]
print(jagged[1])    # [3, 4, 5]
print(jagged[2])    # [6]
```

### Nested List of Mixed Data Types

```python
student = ["Ravi", 20, [85, 90, 78]]   # name, age, list of marks
print(student[2])         # [85, 90, 78]
print(student[2][0])      # 85
```

---

## 5. Strings and String Methods

A string is a sequence of characters enclosed in single (`'`), double (`"`), or triple (`'''` or `"""`) quotes. Strings in Python are **immutable** — once created, individual characters cannot be changed directly.

### String Immutability

```python
name = "Ravi"
name[0] = "M"    # TypeError: 'str' object does not support item assignment
```

To "change" a string, a new string must be created:

```python
name = "Ravi"
new_name = "M" + name[1:]
print(new_name)     # Mavi
```

### String Concatenation and Repetition

```python
first = "Hello"
second = "World"

print(first + " " + second)    # Hello World
print(first * 3)                # HelloHelloHello
```

### Common String Methods

**Case Conversion:**

| Method | Description | Example |
|---|---|---|
| `upper()` | Converts to uppercase | `"hi".upper()` → `"HI"` |
| `lower()` | Converts to lowercase | `"HI".lower()` → `"hi"` |
| `title()` | Capitalizes the first letter of each word | `"hello world".title()` → `"Hello World"` |
| `capitalize()` | Capitalizes only the first letter of the string | `"hello".capitalize()` → `"Hello"` |
| `swapcase()` | Swaps uppercase and lowercase | `"Hello".swapcase()` → `"hELLO"` |

```python
text = "Python Programming"

print(text.upper())        # PYTHON PROGRAMMING
print(text.lower())        # python programming
print(text.title())        # Python Programming
print(text.swapcase())     # pYTHON pROGRAMMING
```

**Whitespace Handling:**

| Method | Description | Example |
|---|---|---|
| `strip()` | Removes leading and trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `lstrip()` | Removes leading (left) whitespace | `"  hi".lstrip()` → `"hi"` |
| `rstrip()` | Removes trailing (right) whitespace | `"hi  ".rstrip()` → `"hi"` |

```python
text = "   Hello World   "
print(text.strip())    # "Hello World"
print(len(text))         # 18 (original unchanged, strip returns a new string)
print(len(text.strip()))  # 11
```

**Searching and Checking:**

| Method | Description | Example |
|---|---|---|
| `find(sub)` | Returns index of first occurrence, or `-1` if not found | `"hello".find("l")` → `2` |
| `count(sub)` | Counts occurrences of a substring | `"hello".count("l")` → `2` |
| `startswith(sub)` | Checks if string starts with `sub` | `"hello".startswith("he")` → `True` |
| `endswith(sub)` | Checks if string ends with `sub` | `"hello".endswith("lo")` → `True` |
| `isalpha()` | True if all characters are letters | `"hello".isalpha()` → `True` |
| `isdigit()` | True if all characters are digits | `"123".isdigit()` → `True` |
| `isalnum()` | True if all characters are letters or digits | `"abc123".isalnum()` → `True` |
| `isspace()` | True if the string contains only whitespace | `"   ".isspace()` → `True` |

```python
text = "Python Programming"

print(text.find("Pro"))         # 7
print(text.count("m"))          # 2
print(text.startswith("Py"))    # True
print(text.endswith("ing"))     # True

print("Python3".isalnum())      # True
print("123".isdigit())          # True
print("Hello".isalpha())        # True
```

**Splitting and Joining:**

| Method | Description | Example |
|---|---|---|
| `split(sep)` | Splits a string into a list, using `sep` as separator (default is whitespace) | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `join(iterable)` | Joins items of a list into a single string, using the string as separator | `"-".join(["a", "b", "c"])` → `"a-b-c"` |
| `replace(old, new)` | Replaces all occurrences of `old` with `new` | `"hi hi".replace("hi", "bye")` → `"bye bye"` |

```python
sentence = "Python is a fun language"
words = sentence.split()
print(words)     # ['Python', 'is', 'a', 'fun', 'language']

csv_line = "apple,banana,cherry"
fruits = csv_line.split(",")
print(fruits)     # ['apple', 'banana', 'cherry']

joined = "-".join(fruits)
print(joined)      # apple-banana-cherry

text = "I like cats"
print(text.replace("cats", "dogs"))   # I like dogs
```

### Example: Counting Vowels in a String

```python
text = "Python Programming"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
```

### Example: Word Frequency Using split()

```python
sentence = "the quick brown fox jumps over the lazy dog the fox runs"
words = sentence.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)
```

---

## 6. String Formatting

String formatting is used to insert variable values into a string in a clean, readable way. Python provides several formatting methods.

### 1. f-strings (Formatted String Literals) — Recommended

Introduced in Python 3.6, f-strings are the most readable and commonly used method. Prefix the string with `f` and place variables inside curly braces `{}`.

```python
name = "Ravi"
age = 20

print(f"My name is {name} and I am {age} years old.")
# Output: My name is Ravi and I am 20 years old.
```

**Expressions Inside f-strings:**

```python
a = 10
b = 5
print(f"The sum of {a} and {b} is {a + b}.")
# Output: The sum of 10 and 5 is 15.
```

**Formatting Numbers with f-strings:**

```python
price = 1234.5678
print(f"Price: {price:.2f}")     # Price: 1234.57   (2 decimal places)

number = 7
print(f"Number: {number:03d}")   # Number: 007       (padded with zeros, width 3)
```

### 2. `str.format()` Method

An older but still widely used method.

```python
name = "Priya"
age = 22
print("My name is {} and I am {} years old.".format(name, age))
```

**Using Positional Indexes:**

```python
print("{0} scored {1} marks".format("Ravi", 85))
print("{1} scored {0} marks".format(85, "Ravi"))   # same output, indexes reordered
```

**Formatting Decimal Places with `.format()`:**

```python
price = 1234.5678
print("Price: {:.2f}".format(price))    # Price: 1234.57
```

### 3. % Operator (Old Style Formatting)

The oldest method, inherited from the C language style. Still seen in older codebases.

```python
name = "Aman"
age = 25
print("My name is %s and I am %d years old." % (name, age))
```

| Symbol | Meaning |
|---|---|
| `%s` | String |
| `%d` | Integer |
| `%f` | Float |

### Comparison of Formatting Methods

| Method | Example | Notes |
|---|---|---|
| f-string | `f"{name} is {age}"` | Most readable, fastest, recommended |
| `.format()` | `"{} is {}".format(name, age)` | Flexible, works in older Python versions |
| `%` operator | `"%s is %d" % (name, age)` | Legacy style, less commonly used now |

### Example: Formatted Table Output

```python
items = [("Apple", 30), ("Banana", 10), ("Mango", 50)]

for item, price in items:
    print(f"{item:<10}{price:>5}")

# Output:
# Apple        30
# Banana       10
# Mango        50
```

---

## 7. Dictionaries and Key-Value Operations

A dictionary is an unordered (insertion-ordered since Python 3.7+), mutable collection that stores data as **key-value pairs**. Dictionaries are defined using curly braces `{}`.

### Creating a Dictionary

```python
student = {
    "name": "Ravi",
    "age": 20,
    "course": "Python Programming"
}
print(student)
print(type(student))    # <class 'dict'>
```

**Key Properties of Dictionaries:**
- Keys must be **unique** — duplicate keys overwrite the previous value.
- Keys must be **immutable** types (string, number, or tuple) — lists cannot be used as keys.
- Values can be of **any data type**, including lists or other dictionaries.

### Accessing Values

```python
student = {"name": "Ravi", "age": 20}

print(student["name"])       # Ravi
print(student.get("age"))    # 20
```

**Difference between `[]` and `.get()`:**
- `student["key"]` raises a `KeyError` if the key does not exist.
- `student.get("key")` returns `None` (or a default value you specify) instead of raising an error.

```python
student = {"name": "Ravi", "age": 20}

print(student["grade"])              # KeyError: 'grade'
print(student.get("grade"))          # None
print(student.get("grade", "N/A"))   # N/A   (default value if key not found)
```

### Adding and Updating Key-Value Pairs

```python
student = {"name": "Ravi", "age": 20}

student["course"] = "Python"     # adding a new key
print(student)   # {'name': 'Ravi', 'age': 20, 'course': 'Python'}

student["age"] = 21              # updating an existing key
print(student)   # {'name': 'Ravi', 'age': 21, 'course': 'Python'}
```

### Removing Key-Value Pairs

| Method | Description | Example |
|---|---|---|
| `pop(key)` | Removes the key and returns its value | `student.pop("age")` |
| `popitem()` | Removes and returns the last inserted key-value pair | `student.popitem()` |
| `del dict[key]` | Deletes a key-value pair (no return value) | `del student["age"]` |
| `clear()` | Removes all key-value pairs | `student.clear()` |

```python
student = {"name": "Ravi", "age": 20, "course": "Python"}

age_value = student.pop("age")
print(age_value)    # 20
print(student)       # {'name': 'Ravi', 'course': 'Python'}

del student["course"]
print(student)       # {'name': 'Ravi'}
```

### Dictionary Methods for Keys, Values, and Items

| Method | Description | Example |
|---|---|---|
| `keys()` | Returns all keys | `student.keys()` |
| `values()` | Returns all values | `student.values()` |
| `items()` | Returns all key-value pairs as tuples | `student.items()` |

```python
student = {"name": "Ravi", "age": 20, "course": "Python"}

print(student.keys())      # dict_keys(['name', 'age', 'course'])
print(student.values())    # dict_values(['Ravi', 20, 'Python'])
print(student.items())     # dict_items([('name', 'Ravi'), ('age', 20), ('course', 'Python')])
```

### Iterating Over a Dictionary

```python
student = {"name": "Ravi", "age": 20, "course": "Python"}

# Iterating over keys (default)
for key in student:
    print(key)

# Iterating over key-value pairs
for key, value in student.items():
    print(key, ":", value)
```

### Checking Membership

Membership checks (`in`, `not in`) test against the **keys** of a dictionary by default.

```python
student = {"name": "Ravi", "age": 20}

print("name" in student)     # True
print("Ravi" in student)     # False (checks keys, not values)
```

### Nested Dictionaries

```python
students = {
    "s1": {"name": "Ravi", "age": 20},
    "s2": {"name": "Priya", "age": 22}
}

print(students["s1"]["name"])    # Ravi
print(students["s2"]["age"])     # 22
```

### Example: Counting Word Frequency Using a Dictionary

```python
sentence = "the cat sat on the mat the cat ran"
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'ran': 1}
```

### Example: Finding the Topper from a Dictionary of Marks

```python
marks = {"Ravi": 85, "Priya": 92, "Aman": 78}

topper = max(marks, key=marks.get)
print("Topper:", topper)          # Priya
print("Marks:", marks[topper])    # 92
```

---

## 8. Sets and Set Operations

A set is an unordered, mutable collection that automatically **removes duplicate values**. Sets are defined using curly braces `{}` or the `set()` function.

### Creating a Set

```python
numbers = {1, 2, 3, 4}
print(numbers)          # {1, 2, 3, 4}

# Duplicates are automatically removed
values = {1, 2, 2, 3, 3, 3}
print(values)             # {1, 2, 3}

# Creating an empty set (must use set(), NOT {})
empty_set = set()
print(type(empty_set))    # <class 'set'>

not_a_set = {}
print(type(not_a_set))    # <class 'dict'>  (empty {} creates a dictionary, not a set)
```

**Key Properties of Sets:**
- **Unordered** — items do not maintain insertion order and cannot be accessed by index.
- **No duplicates** — automatically removes repeated values.
- **Mutable** — items can be added or removed, but the items themselves must be immutable (no lists inside a set).

### Adding and Removing Elements

| Method | Description | Example |
|---|---|---|
| `add(x)` | Adds a single item to the set | `s.add(5)` |
| `update(iterable)` | Adds multiple items from another collection | `s.update([4, 5, 6])` |
| `remove(x)` | Removes item `x`; raises an error if not found | `s.remove(3)` |
| `discard(x)` | Removes item `x`; does nothing if not found (no error) | `s.discard(3)` |
| `pop()` | Removes and returns a random item | `s.pop()` |
| `clear()` | Removes all items | `s.clear()` |

```python
fruits = {"apple", "banana"}

fruits.add("cherry")
print(fruits)     # {'apple', 'banana', 'cherry'}  (order may vary)

fruits.update(["mango", "kiwi"])
print(fruits)      # includes all five fruits now

fruits.discard("banana")
print(fruits)      # banana removed, no error even if it did not exist

fruits.remove("apple")
print(fruits)      # apple removed; would raise KeyError if "apple" was absent
```

### Mathematical Set Operations

Sets support standard mathematical operations, useful for comparing collections.

| Operation | Operator | Method | Description |
|---|---|---|---|
| Union | `\|` | `union()` | All items from both sets (no duplicates) |
| Intersection | `&` | `intersection()` | Items common to both sets |
| Difference | `-` | `difference()` | Items in the first set but not the second |
| Symmetric Difference | `^` | `symmetric_difference()` | Items in either set, but not both |

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)      # {1, 2, 3, 4, 5, 6}    Union
print(A & B)      # {3, 4}                Intersection
print(A - B)      # {1, 2}                Difference (A - B)
print(B - A)      # {5, 6}                Difference (B - A)
print(A ^ B)      # {1, 2, 5, 6}          Symmetric Difference
```

**Using Method Names (Equivalent Results):**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))                   # {1, 2, 3, 4, 5, 6}
print(A.intersection(B))            # {3, 4}
print(A.difference(B))              # {1, 2}
print(A.symmetric_difference(B))    # {1, 2, 5, 6}
```

### Checking Subsets and Supersets

| Method | Description | Example |
|---|---|---|
| `issubset()` | True if all items of the calling set are in another set | `A.issubset(B)` |
| `issuperset()` | True if the calling set contains all items of another set | `A.issuperset(B)` |
| `isdisjoint()` | True if the two sets have no items in common | `A.isdisjoint(B)` |

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))      # True,  every item of A is in B
print(B.issuperset(A))    # True,  B contains all items of A
print(A.isdisjoint(B))    # False, they share common items
```

### Example: Removing Duplicates from Data Using a Set

```python
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)     # {1, 2, 3, 4, 5}

# Converting back to a list, if needed
unique_list = list(unique_numbers)
print(unique_list)
```

### Example: Common Elements Between Two Lists

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = set(list1) & set(list2)
print(common)      # {4, 5}
```

---

## Unit 2 Summary

- Lists are ordered, mutable collections defined with `[]`; tuples are ordered but immutable, defined with `()`. Use lists when data will change, and tuples when it should remain fixed.
- Indexing accesses a single item using its position (including negative indexes from the end); slicing (`start:stop:step`) extracts a sub-sequence and works on lists, tuples, and strings.
- List methods like `append()`, `insert()`, `remove()`, `pop()`, `sort()`, and `copy()` allow adding, removing, searching, and reorganizing list data; `sort()` modifies the list in place, while `sorted()` returns a new list.
- Nested lists (lists within lists) represent grid-like or tabular data and are accessed with double indexing (`matrix[row][col]`), typically processed using nested `for` loops.
- Strings are immutable sequences of characters; built-in string methods handle case conversion, searching, whitespace cleanup, and splitting/joining between strings and lists.
- String formatting can be done using f-strings (recommended), `.format()`, or the older `%` operator, all of which insert variable values cleanly into text.
- Dictionaries store data as key-value pairs using `{}`; keys must be unique and immutable, and methods like `.get()`, `.keys()`, `.values()`, and `.items()` support safe access and iteration.
- Sets are unordered, mutable collections that automatically eliminate duplicates, supporting mathematical operations like union, intersection, difference, and symmetric difference.