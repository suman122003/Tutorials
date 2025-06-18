# Object Oriented Programming in Python

**YouTube Video:** https://youtu.be/Ej_02ICOIgs

**Original Codes:** https://github.com/jimdevops19/PythonOOP

**Date: 13.06.2025 - 17.06.2025**

## Constructor, __init__ (File: [`sec1.py`](sec1.py))

Constructor: `__init__`.

Magic methods: `__init__`, `__dict__` etc.

Instance (`self.something`) attribute: `self.name`, `self.price` etc.

Class (`Item.something`) attribute: Used just after class line outside `def __init__` loop.

More about `__repr__`: https://www.youtube.com/watch?v=FIaPZXaePhw

## Class vs Static Methods (File: [`sec2.py`](sec2.py))

Decorator: `@classmethod`, `@staticmethod` etc.

Static method: This should do something that has a relationship with the class, but not somethng that must be uique per instance!

Class method: This should alos do something that has a relationship with the class, but usually, those are used to manipulate different structures of data to instantiate objects, like we have done with csv.

We can call class and static methods from both class and instance level.

## Inheritance (File: [`sec3.py`](sec3.py))

class Child_class(Parent_class): `class Phone(Item)`

`super().__init__(...)` function to access all attributes / methods of parent class `__init__(self, ...)` function.

## Getters and Setters (File: [`sec4_item.py`](sec4_item.py), [`sec4_phone.py`](sec4_phone.py), [`sec4.py`](sec4.py))

Setting an attribute and not change that later (encapculation).

Read only attribute: `@property` decorator.

`@name.setter` decorator for setting a fixed attribute `__name` (it's like private attribute in Java or C++).

## OOP Principles (File: [`sec5_item.py`](sec5_item.py), [`sec5_phone.py`](sec5_phone.py), [`sec5_keyboards`](sec5_keyboard.py), [`sec5.py`](sec5.py))

1. Encapculation: e.g. `increment_price`.
2. Abstraction: Abstracting an email process, `__function`.
3. Inheritance: Child classes can be used for all works.
4. Polymorphism: Word meaning - 'many forms'. Working with class attributes.

