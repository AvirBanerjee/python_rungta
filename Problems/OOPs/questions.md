# Unit 4 Practice Questions: Object-Oriented Programming

## Classes and Objects

<details>
<summary>1. Creating a Simple Class</summary>
Problem: Create a class named `Book` with no attributes, create two objects of it, and print the type of each object.

</details>

<details>
<summary>2. Adding Attributes to an Object</summary>
Problem: Create a class `Car`, create an object, and assign `brand` and `color` attributes to it outside the class. Print both values.

</details>

<details>
<summary>3. Class with a Method</summary>
Problem: Create a class `Greeter` with a method `say_hello` that prints "Hello from Greeter". Create an object and call the method.

</details>

<details>
<summary>4. Understanding self</summary>
Problem: Create a class `Counter` with a method `set_value(self, n)` and a method `show(self)`. Create two objects, give them different values, and show that each object keeps its own data.

</details>

<details>
<summary>5. Equivalent Method Call</summary>
Problem: Given `s1 = Student()` and a method `greet(self)`, write the two equivalent ways of calling the method: through the object, and through the class name.

</details>

<details>
<summary>6. Using isinstance()</summary>
Problem: Create a class `Dog` and an object `d`. Use `isinstance()` to check whether `d` is a `Dog` and whether the integer `5` is a `Dog`.

</details>

<details>
<summary>7. hasattr(), getattr(), and setattr()</summary>
Problem: Create an object with a `name` attribute. Use `hasattr()` to check for `name` and `age`, use `setattr()` to add `age`, and use `getattr()` to print both values.

</details>

<details>
<summary>8. Rectangle Area and Perimeter</summary>
Problem: Create a class `Rectangle` with methods `set_dimensions(length, width)`, `area()`, and `perimeter()`. Create an object and print both results.

</details>

---

## Constructors

<details>
<summary>1. Basic Constructor</summary>
Problem: Create a class `Student` with a constructor that takes `name` and `age`, stores them as attributes, and print them for one object.

</details>

<details>
<summary>2. Constructor Runs Automatically</summary>
Problem: Create a class with an `__init__` method that prints "Object created". Create three objects and observe how many times the message prints.

</details>

<details>
<summary>3. Constructor with Default Values</summary>
Problem: Create a class `Employee` with a constructor taking `name` and `department`, where `department` defaults to "General". Create one object with and one without a department.

</details>

<details>
<summary>4. Constructor with a Method</summary>
Problem: Create a class `Circle` whose constructor takes `radius`, and add a method `area()` that returns the area using 3.14. Print the area for two circles of different radii.

</details>

<details>
<summary>5. Two Constructors Problem</summary>
Problem: Explain what happens if a class defines two `__init__` methods with different parameters, and show how to achieve the same effect using default arguments.

</details>

<details>
<summary>6. Constructor Validation</summary>
Problem: Create a class `Person` whose constructor sets `age` to 0 and prints "Invalid age" if a negative age is passed, otherwise stores the given age.

</details>

<details>
<summary>7. Constructor with Computed Attribute</summary>
Problem: Create a class `Student` whose constructor takes `name` and a list of three marks, and calculates and stores the `total` and `average` as attributes.

</details>

<details>
<summary>8. Destructor</summary>
Problem: Create a class with `__init__` and `__del__` methods that print messages, create an object, delete it using `del`, and describe the output order.

</details>

---

## Instance and Class Variables

<details>
<summary>1. Instance Variables are Separate</summary>
Problem: Create a class `Player` with an instance variable `score`. Create two objects, change the score of one, and show that the other is unaffected.

</details>

<details>
<summary>2. Shared Class Variable</summary>
Problem: Create a class `Student` with a class variable `college = "Rungta"`. Create two objects and print the college through both objects and through the class.

</details>

<details>
<summary>3. Counting Objects</summary>
Problem: Create a class `Product` that uses a class variable to count how many objects have been created, and print the count after creating four objects.

</details>

<details>
<summary>4. Changing a Class Variable</summary>
Problem: Create a class with a class variable, change it using the class name, and show that all objects now see the new value.

</details>

<details>
<summary>5. Shadowing a Class Variable</summary>
Problem: Predict the output of the following code and explain why the class variable is not changed for `s2`:

```python
class Student:
    college = "Rungta"

s1 = Student()
s2 = Student()
s1.college = "XYZ"
print(s1.college, s2.college, Student.college)
```

</details>

<details>
<summary>6. Mutable Class Variable Trap</summary>
Problem: Predict the output of the following code, explain why both objects see the same list, and rewrite the class so each object has its own list:

```python
class Team:
    members = []
    def add(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()
t1.add("Ravi")
t2.add("Priya")
print(t1.members, t2.members)
```

</details>

<details>
<summary>7. Interest Rate Using a Class Variable</summary>
Problem: Create a class `Savings` with a class variable `rate = 5` and an instance variable `balance`. Add a method that returns the interest as `balance * rate / 100`, and show what happens to all objects when the class variable changes.

</details>

<details>
<summary>8. Viewing Instance Variables</summary>
Problem: Create an object with three attributes, print its `__dict__`, and explain why class variables do not appear in it.

</details>

---

## Methods (Instance, Class, and Static)

<details>
<summary>1. Bank Account Methods</summary>
Problem: Create a class `BankAccount` with a balance and methods `deposit(amount)` and `withdraw(amount)`. The withdraw method should print "Insufficient balance" if the amount is more than the balance.

</details>

<details>
<summary>2. Class Method for a Counter</summary>
Problem: Create a class that counts its objects using a class variable, and add a `@classmethod` named `get_count` that returns the count.

</details>

<details>
<summary>3. Static Method Utility</summary>
Problem: Create a class `MathUtils` with static methods `is_even(n)` and `factorial(n)`, and call both without creating any object.

</details>

<details>
<summary>4. Alternative Constructor</summary>
Problem: Create a class `Student` with `name` and `age`, and add a class method `from_string("Ravi-20")` that splits the string and returns a new `Student` object.

</details>

<details>
<summary>5. Choosing the Method Type</summary>
Problem: For each of the following tasks, state whether an instance method, class method, or static method is most suitable and why: (a) calculating the percentage of one student object, (b) returning the total number of students created, (c) checking whether a given number is prime.

</details>

<details>
<summary>6. Method Calling Another Method</summary>
Problem: Create a class `Calculator` with methods `add(a, b)` and `average(a, b)`, where `average` calls `self.add` internally.

</details>

<details>
<summary>7. Printing an Object Using __str__</summary>
Problem: Create a class `Student` with `name` and `marks`, and define `__str__` so that `print(student)` shows "Student: Ravi, Marks: 85".

</details>

<details>
<summary>8. Comparing the Three Method Types</summary>
Problem: Write a single class that contains one instance method, one class method, and one static method, call all three, and print what each one can and cannot access.

</details>

---

## Encapsulation

<details>
<summary>1. Public, Protected, and Private</summary>
Problem: Create a class with one public, one protected (`_`), and one private (`__`) attribute. Try to print all three from outside the class and describe the result.

</details>

<details>
<summary>2. Name Mangling</summary>
Problem: Create a class with a private attribute `__secret`, and show how to access it from outside using its mangled name. Explain why this is discouraged.

</details>

<details>
<summary>3. Getter and Setter Methods</summary>
Problem: Create a class `Account` with a private `__balance`, a getter `get_balance()`, and a setter `set_balance(amount)` that rejects negative values.

</details>

<details>
<summary>4. Using @property</summary>
Problem: Rewrite the previous question using the `@property` decorator and a `@balance.setter`, so that `acc.balance` and `acc.balance = 500` work like normal attributes.

</details>

<details>
<summary>5. Read-Only Property</summary>
Problem: Create a class `Circle` with a private radius and a read-only property `area`. Show what happens when you try to assign a value to `area`.

</details>

<details>
<summary>6. Private Method</summary>
Problem: Create a class `Login` with a private method `__check_pin(pin)` and a public method `login(pin)` that uses it. Show that the private method cannot be called directly from outside.

</details>

<details>
<summary>7. Validated Marks</summary>
Problem: Create a class `Student` with a private `__marks` attribute, where the setter accepts only values between 0 and 100 and prints "Invalid marks" otherwise.

</details>

<details>
<summary>8. ATM Simulation</summary>
Problem: Create a class `ATM` with a private PIN and a private balance. Provide public methods to verify the PIN, check the balance, and withdraw money only after the correct PIN is entered.

</details>

---

## Inheritance

<details>
<summary>1. Single Inheritance</summary>
Problem: Create a class `Animal` with a method `eat()` and a class `Dog` that inherits from it and adds `bark()`. Call both methods on a `Dog` object.

</details>

<details>
<summary>2. Using super() in a Constructor</summary>
Problem: Create a class `Person` with `name` and `age`, and a class `Student` that inherits from it and adds `course`, using `super().__init__()` to set the inherited attributes.

</details>

<details>
<summary>3. Forgetting super()</summary>
Problem: Predict what happens if a child class defines its own `__init__` without calling `super().__init__()`, and then tries to access a parent attribute. Explain the error.

</details>

<details>
<summary>4. Multilevel Inheritance</summary>
Problem: Create classes `Grandparent`, `Parent`, and `Child` in a chain, each with one method of its own, and call all three methods using a single `Child` object.

</details>

<details>
<summary>5. Hierarchical Inheritance</summary>
Problem: Create a class `Vehicle` with a method `start()`, and two child classes `Car` and `Bike`. Show that both children can use `start()`.

</details>

<details>
<summary>6. Multiple Inheritance</summary>
Problem: Create classes `Father` and `Mother`, each with one method, and a class `Child` inheriting from both. Call both methods from a `Child` object.

</details>

<details>
<summary>7. Method Resolution Order</summary>
Problem: Given classes `A`, `B(A)`, `C(A)`, and `D(B, C)`, where `A`, `B`, and `C` each define a method `show()`, predict which `show()` runs for a `D` object, and print the MRO to confirm.

</details>

<details>
<summary>8. issubclass() and isinstance()</summary>
Problem: For `Dog(Animal)`, use `issubclass()` and `isinstance()` to check the relationship between the classes and between an object and both classes.

</details>

---

## Method Overriding

<details>
<summary>1. Overriding a Simple Method</summary>
Problem: Create a class `Animal` with a method `sound()` and two child classes `Dog` and `Cat` that override it. Call the method on one object of each class.

</details>

<details>
<summary>2. Overriding with super()</summary>
Problem: Create an `Employee` class with a `show()` method, and a `Manager` class that overrides `show()` by calling the parent's `show()` first and then printing the team size.

</details>

<details>
<summary>3. Shape Area Hierarchy</summary>
Problem: Create a base class `Shape` with `area()` returning 0, and child classes `Rectangle` and `Circle` that override `area()`. Print the area for a list of mixed shapes using a loop.

</details>

<details>
<summary>4. Overriding __str__</summary>
Problem: Create a parent class and a child class that each define `__str__`, and show that printing a child object uses the child's version.

</details>

<details>
<summary>5. Which Method Runs?</summary>
Problem: Predict the output of the following code and explain which version of `show()` runs:

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    pass

C().show()
```

</details>

<details>
<summary>6. Overriding vs Overloading</summary>
Problem: Explain the difference between method overriding and method overloading, and state how Python handles each.

</details>

<details>
<summary>7. Bank Account Types</summary>
Problem: Create a base class `Account` with a method `calculate_interest()` returning 0, and child classes `Savings` and `Current` that override it with different rules. Print the interest for one object of each type.

</details>

<details>
<summary>8. Salary Calculation</summary>
Problem: Create a base class `Employee` with a method `salary()`. Create child classes `Developer` and `Tester` that override it using different formulas, and print salaries for a list of employees.

</details>

---

## Polymorphism

<details>
<summary>1. Built-in Polymorphism</summary>
Problem: Show that `len()` and the `+` operator work on different data types, giving one example each for strings, lists, and numbers.

</details>

<details>
<summary>2. Same Method, Different Classes</summary>
Problem: Create classes `Dog`, `Cat`, and `Cow`, each with a `speak()` method returning a different sound, and loop over a list of one object from each class.

</details>

<details>
<summary>3. Function Accepting Any Object</summary>
Problem: Write a function `make_sound(animal)` that calls `animal.speak()`, and use it with objects of three different classes.

</details>

<details>
<summary>4. Polymorphism with Inheritance</summary>
Problem: Create a parent class `Bird` with `fly()`, and child classes `Sparrow` and `Penguin` that override it. Call `fly()` on a list containing all three kinds of objects.

</details>

<details>
<summary>5. Duck Typing</summary>
Problem: Create two unrelated classes `Duck` and `Robot`, each with a `quack()` method, and a function that calls `quack()` on any object passed to it. Explain why no shared parent class is needed.

</details>

<details>
<summary>6. Payment System</summary>
Problem: Create classes `CreditCard`, `UPI`, and `NetBanking`, each with a `pay(amount)` method, and a `checkout(method, amount)` function that works with all three.

</details>

<details>
<summary>7. Area Calculator</summary>
Problem: Create classes `Square`, `Triangle`, and `Circle`, each with an `area()` method, and write one function that prints the area of any shape passed to it.

</details>

<details>
<summary>8. Adding a New Type Without Changing Old Code</summary>
Problem: Extend the payment system from question 6 with a new `Wallet` class, and show that `checkout()` works with it without any modification.

</details>

---

## Operator Overloading

<details>
<summary>1. Overloading the + Operator</summary>
Problem: Create a class `Point` with `x` and `y`, and overload `+` using `__add__` so that adding two points returns a new point with the summed coordinates.

</details>

<details>
<summary>2. Overloading - and *</summary>
Problem: Create a class `Vector` and overload `-` (subtraction of two vectors) and `*` (multiplication by a number).

</details>

<details>
<summary>3. Overloading ==</summary>
Problem: Create a class `Student` with `name` and `marks`, and overload `==` using `__eq__` so that two students are equal when their marks are equal.

</details>

<details>
<summary>4. Overloading Comparison for Sorting</summary>
Problem: Overload `__lt__` for a `Student` class based on marks, and use `sort()` on a list of student objects.

</details>

<details>
<summary>5. Overloading __len__</summary>
Problem: Create a class `Playlist` that stores a list of songs and overload `__len__` so that `len(playlist)` returns the number of songs.

</details>

<details>
<summary>6. Overloading __getitem__ and __contains__</summary>
Problem: Add `__getitem__` and `__contains__` to the `Playlist` class so that `playlist[0]` and `"Song A" in playlist` both work.

</details>

<details>
<summary>7. Money Class</summary>
Problem: Create a class `Money` that overloads `+`, `==`, and `__str__`, so that `Money(500) + Money(250)` prints "Rs. 750".

</details>

<details>
<summary>8. Fixing a TypeError</summary>
Problem: The following code raises a `TypeError`. Explain why, and add the missing magic method to fix it:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point(1, 2) + Point(3, 4))
```

</details>

---

## Mixed Problems (Combining Concepts)

<details>
<summary>1. Library Management</summary>
Problem: Create a class `Book` with title and author, and a class `Library` that stores a list of `Book` objects with methods to add a book, remove a book, and display all books. Use a class variable to count total books ever added.

</details>

<details>
<summary>2. Student Result System</summary>
Problem: Create a class `Student` with private marks for three subjects, a property `total`, a property `percentage`, and a method that returns the grade.

</details>

<details>
<summary>3. Employee Hierarchy</summary>
Problem: Create a base class `Employee` and child classes `Manager` and `Developer`, each overriding a `salary()` method. Use `super()` in constructors, and print details for a list of mixed employees using polymorphism.

</details>

<details>
<summary>4. Fraction Class</summary>
Problem: Create a class `Fraction` with numerator and denominator, and overload `+`, `==`, and `__str__` so that `Fraction(1, 2) + Fraction(1, 3)` prints "5/6".

</details>

<details>
<summary>5. Shopping Cart</summary>
Problem: Create classes `Product` and `Cart`, where `Cart` stores a list of products, overloads `__len__`, and has a method that returns the total price.

</details>

<details>
<summary>6. Vehicle Rental System</summary>
Problem: Create a base class `Vehicle` with a rate per day, and child classes `Car` and `Bike` that override a `rent(days)` method with different pricing rules. Use a class variable to track the total number of rentals.

</details>
