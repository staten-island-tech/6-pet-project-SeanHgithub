Skip to main content
Google ClassroomClassroom
Comp Sci/Engineering T1SKS21T_30 (Period 3) 2025 1
Home
Calendar
Enrolled
To-do
N
NHS Cohort Class of 2029
Current Freshmen
M
Math Club
2
2025-26 Chess
S
SITHS Career Development Center 2025-26
8
8 Freshmen PE
PPS71_83 (Period 8) 2025 1
C
Class of 2029 - College Advisement
GAS11QC_9 (Period 13) 2025 1
S
SITHS Library Google Classroom
P
Period 1 T1- Freshman Russian T1
31R605_2025_1_FRS61H_1
C
Comp Sci/Engineering T1
SKS21T_30 (Period 3) 2025 1
M
Math Team B
MQS11QTB_42 (Period 4) 2025 1
I
Intro Tech Careers T1
RZS21TF_62 (Period 6) 2025 1
A
AP World History T1
HGS41X_70 (Period 7) 2025 1
C
Chem Lab T1 - Wednesday, P6
MWeitzman@schools.nyc.gov
C
Chemistry T1
SCS21H_29 (Period 2) 2025 1
G
Geometry T1-PD 5
MGS21H_50 (Period 5) 2025 1
P
Pd 9 English T1 - Fall Honors 2025
EES81H_99 (Period 9) 2025 1
Archived classes
Settings
Assignment details
Personal Pet Project
Michael Whalen
•
Oct 21
Learning Progress
•
15 points
Repo: https://classroom.github.com/a/_NmmYTVg

Personal Pet Project
You will be designing an application to allow users to play with a new “pet”. Think Tamgaotchi. You may use whatever lore or character style you want.
Users will be able to create a new pet based on Python classes. After instantiating a new pet they will be able to play and care for the pet. Values for the pet should be displayed and updated. See in class example.
L1.md
Text
lesson2.md
Text
Class comments
Your work
Assigned
Private comments

# 🧠 Lesson: Python Classes & Encapsulation


## 🚀 1. What Is a Class?

Imagine you’re designing a video game.
You might have many **heroes**, each with a name, money, and items in their backpack.

Instead of writing new code for each hero, Python lets us use a **class** — a *blueprint* for making similar objects.

### Analogy:

> A **class** is like a *cookie cutter*.
> An **object** is like the *cookie* made from it.

So if `Hero` is our cookie cutter, then `Jillian` or `Mario` are individual cookies 🍪.

---

## 🧩 2. Simple Example: Calculator Class

Let’s look at this code:

```python
class Calculator():
    def add(x, y):
        print(x + y)
        return x + y

    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers

Calculator.add(5, 6)
```

### 💡 What’s Happening

* `class Calculator()` — defines a new *type* of object called **Calculator**.
* Inside are **methods** (functions that belong to a class):
  `add`, `add_many`, and `subtract`.
* `Calculator.add(5, 6)` calls the `add` method.

---

## 🧱 3. Building Your Own Class: Hero

Now we make a **Hero** class that describes a game character.

```python
class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
```

### 🔍 Breaking it down

#### 🏗️ `__init__` Method

This is a *special* function called every time a new Hero is created.
It sets up the hero’s starting information (name, money, items).

* `self.name` — hero’s name
* `self.money` — how much money the hero has
* `self.inventory` — what items they carry

#### 🧍‍♀️ Creating a Hero

```python
Jillian = Hero("Jillian", 150, ["Potion"])
```

* We just made a new **Hero object** named Jillian!
* Jillian starts with **$150** and one **Potion**.

#### 💰 Buying an Item

```python
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)
```

When Jillian buys something:

* The item is added to her inventory list.
* The inventory is printed.
* `__dict__` shows all her data stored in a dictionary format.

---

## 🔒 4. Encapsulation: Protecting Data

Encapsulation means **keeping related data and methods inside a single unit (the class)** — and **controlling how outside code interacts** with that data.

### Analogy:

> Imagine the Hero’s backpack is zipped shut 🎒.
> Only the Hero knows how to open it properly (using their methods).
> You don’t just reach in and mess with it directly!

In Python, we can use **naming conventions** to mark variables as “private” (for internal use only).

Example:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
```

This way, no one outside the class should directly do `my_account.__balance = 0`.
They should use the **methods** (`deposit`, `show_balance`) instead.

---

## 🧠 5. Practice Time

### ✏️ Activity 1 – Create Your Own Hero

Make your own hero object with a name, starting money, and one item.

Then, use `.buy()` to add another item to your inventory.

### ✏️ Activity 2 – Add Encapsulation

Create a class `Pet` that has:

* A **name**
* A **private variable** for happiness level (e.g., `__happiness`)
* A method to **play()** that increases happiness
* A method to **show_status()** that prints how happy the pet is

Example output:

```
Fluffy is playing fetch!
Fluffy’s happiness is now 10
```

---

## 💬 6. Key Takeaways

| Concept           | Meaning                                       | Example                              |
| ----------------- | --------------------------------------------- | ------------------------------------ |
| **Class**         | Blueprint for creating objects                | `class Hero:`                        |
| **Object**        | A specific example from a class               | `Jillian = Hero(...)`                |
| **Method**        | Function inside a class                       | `def buy(self, item)`                |
| **Encapsulation** | Keeping data + methods together and protected | private variables like `__balance`   |
| **self**          | Refers to the *current object*                | `self.name` means “this hero’s name” |

---

## 🌟 7. Challenge (Optional)

Modify the Hero class so that:

* It has a **private money variable** (`__money`)
* You must use a method like `.spend(amount)` to reduce money when buying something

Then print out how much money Jillian has left after buying her sword.

---

L1.md
