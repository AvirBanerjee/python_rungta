# UNIT 4: Object-Oriented Programming in Python

## Topics Covered
1. Classes and Objects
2. Constructors
3. Instance and Class Variables
4. Methods (Instance, Class, and Static)
5. Encapsulation
6. Inheritance
7. Method Overriding
8. Polymorphism
9. Operator Overloading

---

## 1. Classes and Objects

### What is Object-Oriented Programming (OOP)?

Object-Oriented Programming is a way of organizing a program around **objects** — bundles of data (attributes) and the functions that work on that data (methods) — instead of writing everything as a flat sequence of functions. It models real-world things: a student, a bank account, a car.

**Why OOP?**
- **Organization** — related data and behavior live together in one unit.
- **Reusability** — a class can be reused to create many objects, and extended through inheritance.
- **Maintainability** — changes to one class do not break unrelated parts of the program.
- **Real-world modeling** — programs map naturally to real entities.

### Class

A class is a **blueprint** (template) that defines what data and behavior its objects will have. A class by itself does not hold any actual data — it only describes the structure.

### Object

An object is an **instance** of a class — an actual thing created from the blueprint, with its own data.

**Analogy:** A class is like the architectural plan of a house; objects are the actual houses built from that plan. One plan can produce many houses, each with its own color, owner, and address.

### Defining a Class and Creating Objects

A class is defined using the `class` keyword. By convention, class names use **PascalCase** (each word capitalized, no underscores).

```python
class Student:
    pass       # empty class for now

s1 = Student()     # creating an object (instance)
s2 = Student()     # another object of the same class

print(type(s1))    # <class '__main__.Student'>
print(s1 == s2)    # False, two separate objects
```

### Adding Attributes to an Object

Attributes are variables attached to an object, accessed using the dot (`.`) operator.

```python
class Student:
    pass

s1 = Student()
s1.name = "Ravi"
s1.age = 20

print(s1.name)    # Ravi
print(s1.age)     # 20
```

Assigning attributes object by object works, but is error-prone — a better approach is to initialize attributes in a constructor (next section).

### Adding Behavior (Methods)

A function defined inside a class is called a **method**. Its first parameter is always `self`, which refers to the object the method is being called on.

```python
class Student:
    def greet(self):
        print("Hello, I am a student")

s1 = Student()
s1.greet()      # Hello, I am a student
```

### Understanding `self`

`self` is the reference to the **current object**. When you write `s1.greet()`, Python automatically passes `s1` as the first argument, so it is equivalent to `Student.greet(s1)`.

```python
class Student:
    def set_name(self, name):
        self.name = name        # stores the value in THIS object

    def show_name(self):
        print("Name:", self.name)

s1 = Student()
s2 = Student()

s1.set_name("Ravi")
s2.set_name("Priya")

s1.show_name()     # Name: Ravi
s2.show_name()     # Name: Priya   (each object has its own data)
```

**Note:** The name `self` is only a convention, not a keyword, but it is followed universally and should always be used.

### Checking Objects

```python
s1 = Student()

print(isinstance(s1, Student))     # True
print(hasattr(s1, "name"))         # False (attribute not set yet)

s1.name = "Ravi"
print(hasattr(s1, "name"))         # True
print(getattr(s1, "name"))         # Ravi
setattr(s1, "age", 20)
print(s1.age)                       # 20
```

| Function | Purpose |
|---|---|
| `isinstance(obj, Class)` | Checks whether `obj` is an instance of `Class` |
| `hasattr(obj, "attr")` | Checks whether the object has the attribute |
| `getattr(obj, "attr")` | Gets the value of the attribute |
| `setattr(obj, "attr", value)` | Sets the value of the attribute |
| `delattr(obj, "attr")` | Deletes the attribute |

---

## 2. Constructors

A constructor is a special method that runs **automatically** when an object is created, used to initialize the object's attributes. In Python, the constructor is the method named `__init__`.

### The `__init__` Method

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ravi", 20)
s2 = Student("Priya", 22)

print(s1.name, s1.age)     # Ravi 20
print(s2.name, s2.age)     # Priya 22
```

When `Student("Ravi", 20)` is executed, Python:
1. Creates a new empty object.
2. Calls `__init__` automatically with that object as `self`, followed by the given arguments.
3. Returns the fully initialized object.

### Types of Constructors

**1. Default Constructor (no parameters except `self`):**

```python
class Demo:
    def __init__(self):
        print("Object created")
        self.value = 0

d = Demo()      # Object created
```

**2. Parameterized Constructor (takes extra parameters):**

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(5, 3)
print(r.area())      # 15
```

### Constructor with Default Arguments

Default argument values (from Unit 3) work in constructors too.

```python
class Student:
    def __init__(self, name, course="Python"):
        self.name = name
        self.course = course

s1 = Student("Ravi")
s2 = Student("Priya", "Java")

print(s1.course)     # Python
print(s2.course)     # Java
```

### Python Does Not Support Multiple Constructors Directly

Unlike some languages, Python does not allow defining two `__init__` methods with different parameters — the second definition simply replaces the first. Use default arguments or `*args` instead.

```python
class Demo:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("No arguments")
        elif b is None:
            print("One argument:", a)
        else:
            print("Two arguments:", a, b)

Demo()           # No arguments
Demo(1)          # One argument: 1
Demo(1, 2)       # Two arguments: 1 2
```

### Destructor: `__del__` (Brief Introduction)

`__del__` is called when an object is about to be destroyed (when no references to it remain). It is rarely needed in everyday Python programs.

```python
class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

d = Demo()
del d          # Object created, then Object destroyed
```

---

## 3. Instance and Class Variables

### Instance Variables

Instance variables belong to **each individual object**. They are usually created inside `__init__` using `self`. Every object has its own separate copy.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name         # instance variable
        self.marks = marks       # instance variable

s1 = Student("Ravi", 85)
s2 = Student("Priya", 92)

s1.marks = 90                    # changing s1 does NOT affect s2
print(s1.marks)    # 90
print(s2.marks)    # 92
```

### Class Variables

Class variables belong to the **class itself** and are **shared by all objects** of that class. They are defined directly inside the class body, outside any method.

```python
class Student:
    college = "Rungta"           # class variable, shared by all objects

    def __init__(self, name):
        self.name = name         # instance variable

s1 = Student("Ravi")
s2 = Student("Priya")

print(s1.college)       # Rungta
print(s2.college)       # Rungta
print(Student.college)  # Rungta   (can also be accessed through the class name)
```

### Changing a Class Variable

To change the value for **all** objects, modify it through the **class name**.

```python
Student.college = "ABC University"

print(s1.college)    # ABC University
print(s2.college)    # ABC University
```

### The Common Trap: Assigning Through an Object Creates a New Instance Variable

If you assign to a class variable through an **object**, Python does not modify the class variable — it creates a new instance variable that hides (shadows) the class variable for that object only.

```python
class Student:
    college = "Rungta"

s1 = Student()
s2 = Student()

s1.college = "XYZ"          # creates a NEW instance variable on s1 only

print(s1.college)           # XYZ      (instance variable)
print(s2.college)           # Rungta   (still the class variable)
print(Student.college)      # Rungta   (class variable unchanged)
```

### Example: Counting Objects with a Class Variable

A classic use of a class variable is keeping a count shared across all objects.

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1       # increase the shared counter

s1 = Student("Ravi")
s2 = Student("Priya")
s3 = Student("Aman")

print("Total students:", Student.count)    # Total students: 3
```

### The Mutable Class Variable Pitfall

Just like the mutable default argument pitfall in Unit 3, a **mutable** class variable (like a list) is shared by every object, so changes made through one object appear in all of them.

```python
class Team:
    members = []                 # shared list — risky

    def add(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()

t1.add("Ravi")
t2.add("Priya")

print(t1.members)    # ['Ravi', 'Priya']  <- both objects share one list
print(t2.members)    # ['Ravi', 'Priya']
```

**Fix:** create the list inside `__init__` so each object gets its own.

```python
class Team:
    def __init__(self):
        self.members = []        # separate list per object

    def add(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()
t1.add("Ravi")
t2.add("Priya")

print(t1.members)    # ['Ravi']
print(t2.members)    # ['Priya']
```

### Instance Variable vs Class Variable

| Feature | Instance Variable | Class Variable |
|---|---|---|
| Belongs to | Each individual object | The class (shared by all objects) |
| Defined | Inside methods using `self.` (usually `__init__`) | Directly inside the class body |
| Copies | One separate copy per object | One single copy |
| Accessed via | `object.variable` | `ClassName.variable` (or `object.variable`) |
| Typical use | Data unique to each object (name, marks) | Data common to all objects (college name, counters, constants) |

### Viewing an Object's Attributes: `__dict__`

```python
s1 = Student("Ravi")
print(s1.__dict__)      # {'name': 'Ravi'}   (only instance variables)
```

---

## 4. Methods (Instance, Class, and Static)

Python has three kinds of methods inside a class, differing in what they can access.

### 1. Instance Methods

The most common kind. They take `self` as the first parameter and can access and modify both the object's data and (indirectly) class data.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")

acc = BankAccount("Ravi", 1000)
acc.deposit(500)       # Deposited 500. Balance: 1500
acc.withdraw(200)      # Withdrew 200. Balance: 1300
acc.withdraw(5000)     # Insufficient balance
```

### 2. Class Methods

A class method works with the **class** rather than an individual object. It is marked with the `@classmethod` decorator and takes `cls` (the class itself) as its first parameter.

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

s1 = Student("Ravi")
s2 = Student("Priya")

print(Student.get_count())     # 2
```

**Common use: alternative constructors.** A class method can create objects in a different way.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

s = Student.from_string("Ravi-20")
print(s.name, s.age)        # Ravi 20
```

### 3. Static Methods

A static method does not receive `self` or `cls` — it behaves like a normal function that simply lives inside the class because it is logically related to it. It is marked with the `@staticmethod` decorator.

```python
class MathHelper:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def square(n):
        return n * n

print(MathHelper.is_even(10))     # True
print(MathHelper.square(5))       # 25
```

No object is needed to call it — it can be called directly on the class.

### Comparison of the Three Method Types

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None | `@classmethod` | `@staticmethod` |
| First parameter | `self` (the object) | `cls` (the class) | None |
| Can access instance data | Yes | No | No |
| Can access class data | Yes | Yes | No |
| Called using | Object | Class or object | Class or object |
| Typical use | Work with an object's own data | Work with class-level data, alternative constructors | Utility functions related to the class |

### Methods Calling Other Methods

One method can call another using `self`.

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add_and_double(self, a, b):
        return self.add(a, b) * 2      # calling another method of the same object

c = Calculator()
print(c.add_and_double(3, 4))     # 14
```

### Methods Returning Objects and Printing Objects: `__str__`

By default, printing an object shows an unhelpful memory address. Defining `__str__` controls what `print()` displays.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Ravi", 20)
print(s)       # <__main__.Student object at 0x000001F5...>  (not useful)
```

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

s = Student("Ravi", 20)
print(s)       # Student(name=Ravi, age=20)
```

`__str__` returns a readable string for users; `__repr__` (similar, but aimed at developers) is used when the object is shown inside a list or in the interactive shell.

---

## 5. Encapsulation

Encapsulation means **bundling data and the methods that work on it into one unit (the class), and controlling access to that data** so it cannot be changed carelessly from outside. It is one of the four pillars of OOP (the others being inheritance, polymorphism, and abstraction).

### Why Encapsulation?
- **Protects data** from accidental or invalid changes.
- **Hides internal details** — outside code only needs to know *what* an object does, not *how*.
- **Allows validation** — rules (for example, balance cannot go negative) can be enforced in one place.

### Access Levels in Python

Unlike languages such as Java or C++, Python has no strict `private` or `public` keywords. Instead, it uses **naming conventions**:

| Type | Syntax | Meaning |
|---|---|---|
| Public | `name` | Accessible from anywhere |
| Protected | `_name` (one underscore) | Convention: meant for use inside the class and its subclasses only |
| Private | `__name` (two underscores) | Name-mangled: Python makes it hard to access from outside the class |

### Public Members

```python
class Student:
    def __init__(self, name):
        self.name = name        # public

s = Student("Ravi")
print(s.name)       # Ravi
s.name = "Aman"     # can be freely changed
```

### Protected Members (Single Underscore)

A single underscore is only a **signal to other programmers**: "this is for internal use, please do not touch it." Python does not actually block access.

```python
class Student:
    def __init__(self, name):
        self._name = name       # protected by convention

s = Student("Ravi")
print(s._name)      # Ravi   (works, but discouraged)
```

### Private Members (Double Underscore)

Names starting with two underscores are **name-mangled**: Python internally renames `__balance` to `_ClassName__balance`, so direct access from outside fails.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance       # private

acc = BankAccount("Ravi", 1000)
print(acc.owner)         # Ravi
print(acc.__balance)     # AttributeError: 'BankAccount' object has no attribute '__balance'
```

**Name mangling revealed:** private data is not truly locked — Python just renames it.

```python
print(acc._BankAccount__balance)    # 1000  (still reachable, but clearly bypassing the rules)
```

Python's philosophy is "we are all consenting adults": the double underscore discourages misuse, but does not make it impossible.

### Getters and Setters

The proper way to access private data is through public methods that control how it is read and changed.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):                  # getter
        return self.__balance

    def set_balance(self, amount):          # setter with validation
        if amount < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = BankAccount("Ravi", 1000)
print(acc.get_balance())     # 1000

acc.set_balance(-500)        # Balance cannot be negative
acc.set_balance(2000)
print(acc.get_balance())     # 2000
```

### The `@property` Decorator (Pythonic Getters and Setters)

Python provides `@property`, which lets getter and setter methods be used like ordinary attributes — cleaner than calling `get_balance()` and `set_balance()`. (It builds on the decorators introduced in Unit 3.)

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):                  # getter
        return self.__balance

    @balance.setter
    def balance(self, amount):          # setter
        if amount < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = amount

acc = BankAccount("Ravi", 1000)
print(acc.balance)       # 1000     (looks like an attribute, runs the getter)

acc.balance = 5000       # runs the setter
print(acc.balance)       # 5000

acc.balance = -100       # Balance cannot be negative
print(acc.balance)       # 5000
```

A property with **no setter** becomes **read-only**:

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14 * self.__radius ** 2

c = Circle(5)
print(c.area)        # 78.5
c.area = 100         # AttributeError: can't set attribute (read-only)
```

### Private Methods

Methods can also be made private with a double underscore, so they are only meant to be used inside the class.

```python
class Account:
    def __init__(self, pin):
        self.__pin = pin

    def __verify(self, entered):         # private helper method
        return entered == self.__pin

    def login(self, entered):
        if self.__verify(entered):
            print("Access granted")
        else:
            print("Access denied")

a = Account(1234)
a.login(1234)         # Access granted
a.login(1111)         # Access denied
a.__verify(1234)      # AttributeError
```

---

## 6. Inheritance

Inheritance allows a new class (the **child**, **derived**, or **subclass**) to **reuse the attributes and methods of an existing class** (the **parent**, **base**, or **superclass**). It models an "is-a" relationship: a Dog *is an* Animal.

### Why Inheritance?
- **Code reuse** — common code is written once in the parent.
- **Extensibility** — a child can add new features or change inherited ones.
- **Logical hierarchy** — mirrors real-world relationships.

### Syntax

```python
class Parent:
    ...

class Child(Parent):      # Child inherits from Parent
    ...
```

### Basic Example

```python
class Animal:
    def eat(self):
        print("This animal eats food")

    def sleep(self):
        print("This animal sleeps")

class Dog(Animal):             # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()       # This animal eats food    (inherited)
d.sleep()     # This animal sleeps       (inherited)
d.bark()      # Dog barks                (Dog's own method)
```

### The `super()` Function

`super()` gives access to the parent class from inside the child. It is most commonly used to call the parent's constructor, so the parent's attributes are set up properly.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)       # initialize name and age via the parent
        self.course = course

s = Student("Ravi", 20, "Python")
print(s.name, s.age, s.course)     # Ravi 20 Python
```

If the child defines its own `__init__` and does **not** call `super().__init__()`, the parent's constructor is skipped and the parent's attributes will not exist.

```python
class Student(Person):
    def __init__(self, course):
        self.course = course          # parent's __init__ never runs

s = Student("Python")
print(s.name)      # AttributeError: 'Student' object has no attribute 'name'
```

### Types of Inheritance

**1. Single Inheritance** — one child, one parent.

```python
class A:
    pass

class B(A):
    pass
```

**2. Multilevel Inheritance** — a chain: grandparent, parent, child.

```python
class Grandparent:
    def home(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.home()      # Grandparent's house
c.car()       # Parent's car
c.bike()      # Child's bike
```

**3. Hierarchical Inheritance** — multiple children share one parent.

```python
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

Car().start()      # Vehicle starts
Bike().start()     # Vehicle starts
```

**4. Multiple Inheritance** — one child inherits from more than one parent.

```python
class Father:
    def skills(self):
        print("Father: gardening")

class Mother:
    def hobbies(self):
        print("Mother: painting")

class Child(Father, Mother):
    pass

c = Child()
c.skills()      # Father: gardening
c.hobbies()     # Mother: painting
```

**5. Hybrid Inheritance** — a combination of two or more of the above types.

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):         # combines hierarchical and multiple inheritance
    pass

D().show()      # A
```

### Summary of Inheritance Types

| Type | Structure | Example |
|---|---|---|
| Single | A → B | Animal → Dog |
| Multilevel | A → B → C | Grandparent → Parent → Child |
| Hierarchical | A → B, A → C | Vehicle → Car, Vehicle → Bike |
| Multiple | A, B → C | Father, Mother → Child |
| Hybrid | Mix of the above | Diamond shape (A → B, C → D) |

### Method Resolution Order (MRO)

When a method is called, Python searches for it in a specific order — the **Method Resolution Order**. With multiple inheritance, this decides which parent's version wins. It searches the object's own class first, then parents from left to right, following a consistent linearized order.

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

D().show()                  # B   (B comes before C in D(B, C))
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
print(D.mro())              # same order, as a list
```

### Checking Relationships

```python
print(issubclass(Dog, Animal))     # True
print(isinstance(d, Dog))          # True
print(isinstance(d, Animal))       # True  (a Dog is also an Animal)
```

### Everything Inherits from `object`

In Python 3, every class implicitly inherits from the built-in `object` class, which is why methods like `__str__` and `__init__` exist even if you never wrote them.

### Inheritance and Private Members

Private (`__name`) attributes of a parent are name-mangled and cannot be accessed directly by the child. Protected (`_name`) members can be accessed in the child by convention.

```python
class Parent:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

class Child(Parent):
    def show(self):
        print(self.public)           # works
        print(self._protected)       # works
        print(self.__private)        # AttributeError (name-mangled)

Child().show()
```

---

## 7. Method Overriding

Method overriding happens when a **child class defines a method with the same name as a method in its parent**, replacing the parent's version for objects of the child class. It allows a subclass to provide its own specific behavior.

### Basic Example

```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):                 # overrides Animal.sound
        print("Dog barks")

class Cat(Animal):
    def sound(self):                 # overrides Animal.sound
        print("Cat meows")

Animal().sound()    # Some generic animal sound
Dog().sound()       # Dog barks
Cat().sound()       # Cat meows
```

### Rules for Overriding
- The method name must be **exactly the same** as in the parent.
- The parameters should normally match, so the method can be used interchangeably.
- Python decides which version to run based on the **actual class of the object**, at runtime.

### Extending the Parent's Behavior Using `super()`

Instead of fully replacing the parent's method, the child can call the parent's version and then add to it.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show(self):
        super().show()                          # run the parent's version first
        print(f"Team size: {self.team_size}")   # then add extra behavior

m = Manager("Ravi", 80000, 5)
m.show()
# Name: Ravi, Salary: 80000
# Team size: 5
```

### Overriding Special Methods

Special (dunder) methods like `__str__` can be overridden too.

```python
class Shape:
    def __str__(self):
        return "I am a shape"

class Circle(Shape):
    def __str__(self):
        return "I am a circle"

print(Shape())      # I am a shape
print(Circle())     # I am a circle
```

### Example: Overriding in a Hierarchy

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(3)]
for s in shapes:
    print(s.area())
# 20
# 28.26
```

### Overriding vs Overloading

| Feature | Method Overriding | Method Overloading |
|---|---|---|
| Meaning | Child redefines a parent's method | Same method name with different parameters in the same class |
| Needs inheritance | Yes | No |
| Supported in Python | Yes | Not directly (the last definition wins); simulated with default arguments or `*args` |

---

## 8. Polymorphism

Polymorphism means "**many forms**": the same operation or method name behaves differently depending on the object it is used on. It lets code work with objects of different types through a common interface.

### 1. Polymorphism with Built-in Functions and Operators

Python's built-ins already behave polymorphically.

```python
print(len("Python"))         # 6   (length of a string)
print(len([1, 2, 3]))        # 3   (length of a list)
print(len({"a": 1}))         # 1   (length of a dictionary)

print(5 + 3)                  # 8        (addition)
print("Hello " + "World")     # Hello World   (concatenation)
print([1, 2] + [3, 4])        # [1, 2, 3, 4]  (list joining)
```

The same `+` operator and `len()` function work differently for different data types.

### 2. Polymorphism through Method Overriding

Different classes provide different versions of the same method, and calling code does not need to know which class it is dealing with.

```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())      # same call, different result for each object
# Woof
# Meow
# Moo
```

### 3. Polymorphism with a Function

One function can work on any object that supports the required method.

```python
def make_sound(animal):
    print(animal.speak())

make_sound(Dog())      # Woof
make_sound(Cat())      # Meow
```

### 4. Polymorphism with Inheritance

```python
class Bird:
    def fly(self):
        print("Most birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies low")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

for b in [Bird(), Sparrow(), Penguin()]:
    b.fly()
# Most birds can fly
# Sparrow flies low
# Penguins cannot fly
```

### Duck Typing

Python does not require objects to share a parent class for polymorphism to work. If an object has the required method, it can be used — "**If it walks like a duck and quacks like a duck, it is a duck.**"

```python
class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("I am imitating a duck")

def make_it_quack(thing):
    thing.quack()

make_it_quack(Duck())       # Quack
make_it_quack(Person())     # I am imitating a duck   (no shared parent needed)
```

### Example: Payment System

```python
class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class NetBanking:
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking")

def checkout(method, amount):
    method.pay(amount)          # works with any payment type

checkout(CreditCard(), 1000)
checkout(UPI(), 500)
checkout(NetBanking(), 2500)
```

New payment types can be added later without changing `checkout()` — the main benefit of polymorphism.

---

## 9. Operator Overloading

Operator overloading lets a class **define what operators like `+`, `-`, `==`, and `<` mean for its own objects**, by implementing special methods called **magic (dunder) methods** — methods whose names begin and end with double underscores.

### Why It Is Needed

Python does not know how to add two custom objects:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)       # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

Defining `__add__` teaches Python how:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2         # Python calls p1.__add__(p2)
print(p3)             # (4, 6)
```

### Arithmetic Operator Magic Methods

| Operator | Magic Method | Meaning |
|---|---|---|
| `+` | `__add__(self, other)` | Addition |
| `-` | `__sub__(self, other)` | Subtraction |
| `*` | `__mul__(self, other)` | Multiplication |
| `/` | `__truediv__(self, other)` | True division |
| `//` | `__floordiv__(self, other)` | Floor division |
| `%` | `__mod__(self, other)` | Modulus |
| `**` | `__pow__(self, other)` | Exponentiation |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)      # Vector(3, 7)
print(v1 - v2)      # Vector(1, -1)
print(v1 * 3)       # Vector(6, 9)
```

### Comparison Operator Magic Methods

| Operator | Magic Method |
|---|---|
| `==` | `__eq__(self, other)` |
| `!=` | `__ne__(self, other)` |
| `<` | `__lt__(self, other)` |
| `<=` | `__le__(self, other)` |
| `>` | `__gt__(self, other)` |
| `>=` | `__ge__(self, other)` |

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks

s1 = Student("Ravi", 85)
s2 = Student("Priya", 92)

print(s1 == s2)     # False
print(s1 < s2)      # True
print(s1 > s2)      # False
```

Because `__lt__` is defined, objects can also be sorted:

```python
students = [Student("Ravi", 85), Student("Priya", 92), Student("Aman", 78)]
students.sort()
for s in students:
    print(s.name, s.marks)
# Aman 78
# Ravi 85
# Priya 92
```

### Other Useful Magic Methods

| Magic Method | Triggered By | Purpose |
|---|---|---|
| `__str__(self)` | `print(obj)`, `str(obj)` | Readable string version of the object |
| `__repr__(self)` | `repr(obj)`, objects inside lists | Developer-friendly representation |
| `__len__(self)` | `len(obj)` | Length of the object |
| `__getitem__(self, i)` | `obj[i]` | Indexing |
| `__contains__(self, item)` | `item in obj` | Membership check |
| `__bool__(self)` | `bool(obj)`, `if obj:` | Truth value |
| `__call__(self, ...)` | `obj()` | Makes the object callable like a function |

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs

    def __str__(self):
        return f"Playlist with {len(self.songs)} songs"

p = Playlist(["Song A", "Song B", "Song C"])

print(len(p))              # 3
print(p[1])                # Song B
print("Song C" in p)       # True
print(p)                   # Playlist with 3 songs

for song in p:             # iteration works because __getitem__ is defined
    print(song)
```

### Example: Overloading `+` for a Fraction-Like Class

```python
class Money:
    def __init__(self, rupees):
        self.rupees = rupees

    def __add__(self, other):
        return Money(self.rupees + other.rupees)

    def __eq__(self, other):
        return self.rupees == other.rupees

    def __str__(self):
        return f"Rs. {self.rupees}"

wallet = Money(500)
bonus = Money(250)

total = wallet + bonus
print(total)                        # Rs. 750
print(total == Money(750))          # True
```

### Overloading vs Overriding vs Polymorphism (Quick Distinction)

| Concept | Meaning |
|---|---|
| Operator overloading | Giving operators like `+` a custom meaning for your own class |
| Method overriding | A child class replaces a parent's method |
| Polymorphism | The broader idea of one interface behaving differently for different objects (both of the above are ways of achieving it) |

---

## Unit 4 Summary

- A class is a blueprint and an object is an instance of it; `self` refers to the current object, and `isinstance()`, `hasattr()`, `getattr()`, and `setattr()` help inspect objects.
- The constructor `__init__` runs automatically when an object is created and initializes its attributes; Python allows only one `__init__` per class, so default arguments are used to support different ways of creating objects.
- Instance variables (defined with `self`) are separate for each object, while class variables (defined in the class body) are shared by all objects; assigning to a class variable through an object creates a new instance variable instead, and mutable class variables are shared and should be avoided.
- Instance methods work with `self`, class methods (`@classmethod`) work with `cls` and class-level data, and static methods (`@staticmethod`) take neither and act as utility functions; `__str__` controls how an object is printed.
- Encapsulation bundles data with the methods that act on it and controls access: public (`name`), protected (`_name`, by convention), and private (`__name`, name-mangled); getters/setters and `@property` allow safe, validated access.
- Inheritance lets a child class reuse a parent's attributes and methods (single, multilevel, hierarchical, multiple, and hybrid), `super()` calls the parent's methods and constructor, and the Method Resolution Order (MRO) decides which version runs in multiple inheritance.
- Method overriding lets a child class redefine an inherited method, optionally extending the parent's version through `super()`.
- Polymorphism means one interface with many behaviors, achieved through built-ins, overridden methods, and duck typing, where any object with the required method can be used regardless of its class.
- Operator overloading uses magic methods like `__add__`, `__eq__`, `__lt__`, `__len__`, and `__getitem__` to give operators and built-in functions a custom meaning for a class's own objects.
