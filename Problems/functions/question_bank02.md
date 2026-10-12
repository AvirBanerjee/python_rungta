# Question Bank: Functions in Python

## Defining and Calling Functions

<details>
<summary>1. Basic Greeting Function</summary>
Problem: Write a function with no parameters that prints "Welcome to Python Programming" when called.

</details>

<details>
<summary>2. Calling a Function Multiple Times</summary>
Problem: Define a function that prints your name and course, then call it three times.

</details>

<details>
<summary>3. Function to Print a Separator Line</summary>
Problem: Write a function that prints a line of 20 dashes, and use it before and after some output to separate sections.

</details>

<details>
<summary>4. Identifying Valid Function Names</summary>
Problem: Out of `def 2sum():`, `def calc_total():`, and `def class():`, identify which are valid function names and explain why the others are not.

</details>

<details>
<summary>5. Using pass in an Unfinished Function</summary>
Problem: Write a function named `process_order` that currently does nothing (to be completed later), without causing a syntax error.

</details>

---

## Parameters and Return Values

<details>
<summary>6. Greeting with a Name Parameter</summary>
Problem: Write a function that takes a name as a parameter and prints a personalized greeting.

</details>

<details>
<summary>7. Adding Two Numbers</summary>
Problem: Write a function that takes two numbers as parameters and returns their sum.

</details>

<details>
<summary>8. Difference Between print() and return</summary>
Problem: Write two versions of a function that adds two numbers — one using print() and one using return. Show what happens when you try to use the result of each in further calculations.

</details>

<details>
<summary>9. Function Returning Multiple Values</summary>
Problem: Write a function that takes three numbers and returns both their sum and their average.

</details>

<details>
<summary>10. Function with No Return Statement</summary>
Problem: Write a function that only prints a message (no return statement), store its result in a variable, and print that variable to show what value it holds.

</details>

<details>
<summary>11. Checking Positive, Negative, or Zero</summary>
Problem: Write a function that takes a number and returns "Positive", "Negative", or "Zero" accordingly.

</details>

<details>
<summary>12. Area of a Rectangle</summary>
Problem: Write a function that takes length and width as parameters and returns the area of the rectangle.

</details>

<details>
<summary>13. Early Return Based on a Condition</summary>
Problem: Write a function that takes a number and immediately returns "Invalid" if it is negative, otherwise continues to classify it as "Small" (0-9) or "Large" (10+).

</details>

---

## Default Arguments and Keyword Arguments

<details>
<summary>14. Greeting with a Default Message</summary>
Problem: Write a function that takes a name and a greeting message, where the greeting defaults to "Hello" if not provided.

</details>

<details>
<summary>15. Default Arguments for Pricing</summary>
Problem: Write a function to calculate a bill that takes item price as a required parameter and tax rate as an optional parameter defaulting to 5 percent.

</details>

<details>
<summary>16. Calling a Function Using Keyword Arguments</summary>
Problem: Write a function with three parameters (name, age, city) and call it twice: once using positional arguments, and once using keyword arguments in a different order.

</details>

<details>
<summary>17. Identifying an Invalid Default Argument Order</summary>
Problem: Explain why `def info(age, name="Unknown", city):` is invalid, and rewrite it correctly.

</details>

<details>
<summary>18. Student Report Card with Defaults</summary>
Problem: Write a function that prints a student's name and marks, where the subject name defaults to "General" if not specified by the caller.

</details>

---

## Variable-Length Arguments (*args and **kwargs)

<details>
<summary>19. Sum of Any Number of Values</summary>
Problem: Write a function using *args that can accept any number of numbers and returns their total.

</details>

<details>
<summary>20. Finding the Largest Among Many Values</summary>
Problem: Write a function using *args that accepts any number of numbers and returns the largest one, without using the built-in max() function.

</details>

<details>
<summary>21. Printing Any Number of Named Details</summary>
Problem: Write a function using **kwargs that accepts any number of named details (like name, age, course) and prints each one.

</details>

<details>
<summary>22. Combining Normal Parameters with *args</summary>
Problem: Write a function that takes a student's name as a normal parameter, followed by any number of subject marks using *args, and prints the name along with the average of the marks.

</details>

<details>
<summary>23. Combining *args and **kwargs</summary>
Problem: Write a function that accepts a title as a normal parameter, any number of extra positional values using *args, and any number of extra named settings using **kwargs, then prints all three separately.

</details>

---

## Variable Scope

<details>
<summary>24. Local vs Global Variable</summary>
Problem: Create a global variable and a local variable with different values but the same name, and show what gets printed inside and outside the function.

</details>

<details>
<summary>25. Modifying a Global Variable Using global</summary>
Problem: Write a function that increments a global counter variable each time it is called, using the global keyword.

</details>

<details>
<summary>26. Predicting a Scope Error</summary>
Problem: Given a function that tries to use and modify a global variable without declaring it global, predict and explain the error that occurs.

</details>

<details>
<summary>27. Using nonlocal in a Nested Function</summary>
Problem: Write an outer function containing a nested inner function that increments a variable from the outer function's scope using nonlocal, and call the inner function three times.

</details>

<details>
<summary>28. Tracing the LEGB Rule</summary>
Problem: Given a variable with the same name defined at the global level, in an outer function, and in an inner function, trace and explain what gets printed at each level.

</details>

---

## The Mutable Default Argument Pitfall

<details>
<summary>29. Predicting Output of a Mutable Default</summary>
Problem: Given a function `def add_item(item, basket=[]):` that appends to basket and returns it, predict the output of calling it three times in a row with different items.

</details>

<details>
<summary>30. Fixing a Mutable Default Argument</summary>
Problem: Rewrite the add_item function from the previous question so that each call starts with a fresh, independent list.

</details>

---

## Docstrings

<details>
<summary>31. Writing a Simple Docstring</summary>
Problem: Write a function that calculates the perimeter of a rectangle, including a one-line docstring describing what it does.

</details>

<details>
<summary>32. Accessing a Function's Docstring</summary>
Problem: Write a function with a docstring, then print its docstring using the __doc__ attribute.

</details>

<details>
<summary>33. Writing a Multi-Line Docstring</summary>
Problem: Write a function that converts Celsius to Fahrenheit, with a multi-line docstring describing its parameter and return value.

</details>

---

## Pass by Reference vs Pass by Value

<details>
<summary>34. Modifying an Integer Inside a Function</summary>
Problem: Write a function that takes a number, reassigns it to a new value inside the function, and show that the original variable outside the function remains unchanged.

</details>

<details>
<summary>35. Modifying a List In Place Inside a Function</summary>
Problem: Write a function that appends a value to a list passed as a parameter, and show that the change is visible outside the function too.

</details>

<details>
<summary>36. Reassigning a List Inside a Function</summary>
Problem: Write a function that reassigns its list parameter to a brand new list inside the function, and show that the original list outside the function remains unaffected.

</details>

<details>
<summary>37. Predicting Mutable vs Immutable Behavior</summary>
Problem: Given one function that modifies a dictionary in place and another that reassigns an integer parameter, predict which change is visible outside the function and explain why.

</details>

---

## Lambda Functions

<details>
<summary>38. Basic Lambda for Squaring</summary>
Problem: Write a lambda function that returns the square of a number, and use it to print the square of 7.

</details>

<details>
<summary>39. Lambda with Two Arguments</summary>
Problem: Write a lambda function that takes two numbers and returns their product.

</details>

<details>
<summary>40. Converting a Regular Function to a Lambda</summary>
Problem: Convert the following regular function into an equivalent lambda function: `def is_even(n): return n % 2 == 0`.

</details>

<details>
<summary>41. Sorting a List of Tuples Using Lambda</summary>
Problem: Given a list of (name, marks) tuples, use sorted() with a lambda function to sort the list by marks in descending order.

</details>

---

## map(), filter(), and reduce()

<details>
<summary>42. Doubling Every Element with map()</summary>
Problem: Given a list of numbers, use map() with a lambda to create a new list where every number is doubled.

</details>

<details>
<summary>43. Filtering Numbers Greater Than a Value</summary>
Problem: Given a list of numbers, use filter() with a lambda to keep only the numbers greater than 50.

</details>

<details>
<summary>44. Converting a List of Strings to Uppercase with map()</summary>
Problem: Given a list of names, use map() to convert all the names to uppercase.

</details>

<details>
<summary>45. Finding the Product of a List Using reduce()</summary>
Problem: Given a list of numbers, use reduce() from the functools module to find the product of all the numbers.

</details>

<details>
<summary>46. Combining filter() and map() Together</summary>
Problem: Given a list of numbers, first filter out the odd numbers using filter(), then use map() to square each of the remaining even numbers.

</details>

---

## Recursion

<details>
<summary>47. Factorial Using Recursion</summary>
Problem: Write a recursive function to calculate the factorial of a given number.

</details>

<details>
<summary>48. Sum of First N Natural Numbers Using Recursion</summary>
Problem: Write a recursive function that returns the sum of the first n natural numbers.

</details>

<details>
<summary>49. Power of a Number Using Recursion</summary>
Problem: Write a recursive function that calculates base raised to the power exponent, without using the ** operator.

</details>

<details>
<summary>50. Identifying the Base Case and Recursive Case</summary>
Problem: Given a recursive function that reverses a string, identify its base case and its recursive case, and explain what would happen if the base case were removed.

</details>

<details>
<summary>51. Fibonacci Sequence Using Recursion</summary>
Problem: Write a recursive function that returns the nth Fibonacci number, and print the first 10 Fibonacci numbers using it.

</details>

<details>
<summary>52. Counting Digits of a Number Using Recursion</summary>
Problem: Write a recursive function that counts and returns the number of digits in a given positive integer.

</details>