# Question Bank: Functions in Python (Advanced)

<details>
<summary>1. Trace the Output: Mutable Default Argument</summary>
Problem: Predict the exact output of the following code, line by line, and explain why:

```python
def add_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(add_to_list(1))
print(add_to_list(2))
print(add_to_list(3, []))
print(add_to_list(4))
```

</details>

<details>
<summary>2. Trace the Output: Scope and global</summary>
Problem: Predict the output of the following code and explain what would go wrong if the `global` keyword were removed from `update_total`:

```python
total = 100

def update_total():
    global total
    total += 50
    return total

def show_total():
    total = 0
    return total

print(update_total())
print(show_total())
print(total)
```

</details>

<details>
<summary>3. Trace the Output: Nested Functions and nonlocal</summary>
Problem: Predict the output of the following code, and explain why removing `nonlocal` from `increment` would cause an error:

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = make_counter()
counter2 = make_counter()

print(counter1())
print(counter1())
print(counter2())
print(counter1())
```

</details>

<details>
<summary>4. Trace the Output: Mutable vs Immutable Arguments</summary>
Problem: Predict what gets printed for `num` and `data` after both functions run, and explain the difference in behavior:

```python
def modify_number(n):
    n += 10

def modify_list(lst):
    lst.append(10)

num = 5
data = [5]

modify_number(num)
modify_list(data)

print(num)
print(data)
```

</details>

<details>
<summary>5. Debug: Function Returns None Unexpectedly</summary>
Problem: The following function is meant to classify a number's sign, but calling `classify(5)` returns `None` instead of "Positive". Find and fix the bug.

```python
def classify(n):
    if n > 0:
        result = "Positive"
    elif n < 0:
        result = "Negative"
    else:
        result = "Zero"

print(classify(5))
```

</details>

<details>
<summary>6. Debug: Incorrect Use of *args and **kwargs Order</summary>
Problem: The following function definition raises a SyntaxError. Identify the exact issue and rewrite the function header correctly, keeping all three parameter types.

```python
def register_user(**details, name, *roles):
    print(name, roles, details)
```

</details>

<details>
<summary>7. Predict and Explain: Recursion Without Updating State</summary>
Problem: The following recursive function is meant to sum numbers from 1 to n, but it causes a RecursionError. Identify why, and rewrite it correctly.

```python
def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n)
```

</details>

<details>
<summary>8. Recursive Trace: Fibonacci Call Count</summary>
Problem: For the standard recursive Fibonacci function below, draw (or describe) the recursive call tree for `fibonacci(5)`, and count exactly how many times `fibonacci(1)` gets called in total.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

</details>

<details>
<summary>9. Memoized Recursion: Fill in the Missing Logic</summary>
Problem: Complete the memoized version of the Fibonacci function below so that `fibonacci_memo(50)` runs almost instantly, explaining what each added line does.

```python
memo = {}

def fibonacci_memo(n):
    # Add the missing logic here so that repeated calls are not recalculated
    if n <= 1:
        return n
    result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return result
```

</details>

<details>
<summary>10. Higher-Order Functions: Function Returning a Function</summary>
Problem: Write a function `make_power(exponent)` that returns a new function, which, when called with a number, raises that number to the given exponent. Then create `square` and `cube` using `make_power`, and demonstrate both.

</details>

<details>
<summary>11. Trace the Output: Closures in a Loop</summary>
Problem: Predict the output of the following code. It is a classic pitfall — explain why the output is not `0 1 2 3 4` and how you would fix it using a default argument.

```python
functions = []
for i in range(5):
    functions.append(lambda: i)

for f in functions:
    print(f())
```

</details>

<details>
<summary>12. Combine map, filter, and reduce in One Pipeline</summary>
Problem: Given a list of numbers from 1 to 20, write a single pipeline using `filter()` to keep only multiples of 3, `map()` to square each of them, and `reduce()` (from functools) to sum the squared results into one final value.

</details>

<details>
<summary>13. Lambda Inside a Sorting Key with Multiple Criteria</summary>
Problem: Given a list of tuples `(name, department, salary)`, write a single `sorted()` call using a lambda that sorts primarily by department (alphabetically) and, within the same department, by salary in descending order.

</details>

<details>
<summary>14. Shallow Copy Inside a Function Parameter</summary>
Problem: Given the function below, predict the output and explain whether `original` is affected, given that a list parameter undergoes both an in-place operation and a shallow copy inside the function:

```python
import copy

def process(data):
    local_copy = copy.copy(data)
    local_copy[0][0] = 999
    data.append("new")
    return local_copy

original = [[1, 2], [3, 4]]
result = process(original)

print(original)
print(result)
```

</details>

<details>
<summary>15. Deep Copy vs Shallow Copy Inside a Function</summary>
Problem: Rewrite the `process` function from the previous question so that modifying `local_copy[0][0]` never affects `original`, while still allowing `data.append("new")` to affect `original` as before. Explain your reasoning.

</details>

<details>
<summary>16. Decorator That Counts Function Calls</summary>
Problem: Write a decorator named `count_calls` that keeps track of how many times the decorated function has been called, printing the count each time. Apply it to a simple `greet()` function and call it three times.

</details>

<details>
<summary>17. Decorator with Arguments Passed Through</summary>
Problem: Write a decorator `log_arguments` that prints the arguments a function was called with, then calls the original function and returns its result. Apply it to a function `add(a, b)` that returns `a + b`, and show the output when called as `add(3, 4)`.

</details>

<details>
<summary>18. Generator vs List: Memory Behavior Trace</summary>
Problem: Given the two functions below, explain the key difference in how and when their values are computed, and predict what `next(gen)` prints when called three times in a row.

```python
def squares_list(n):
    return [i * i for i in range(n)]

def squares_gen(n):
    for i in range(n):
        yield i * i

gen = squares_gen(5)
```

</details>

<details>
<summary>19. Function Design: Safe Division with Default and Type Hints</summary>
Problem: Write a function `safe_divide(a: float, b: float, default: float = 0.0) -> float` that returns `a / b`, but returns `default` instead if `b` is zero (without letting the program crash). Demonstrate it with both a normal division and a division by zero.

</details>

<details>
<summary>20. Combining Recursion with *args: Variadic Sum</summary>
Problem: Write a recursive function `recursive_sum(*args)` that returns the sum of any number of arguments passed to it, without using Python's built-in `sum()` function, and without using a loop anywhere in your solution.

</details>