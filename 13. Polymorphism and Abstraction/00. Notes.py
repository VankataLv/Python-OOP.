# It is the ability to present the same interface for
# differing underlying forms through the interface
# of their base class
# prevents type-checking!
# нашите инстанции (от различни класове) имат един и същи base-class и имат подобна функционалност,
# без да се налага да правим проверки с -> if-elif-else <-code smell. ако направим проверка значи нарушаваме Polymorphism principles
# for ex. base class Shape has method calculate area()#
# child classes circle and triangle both have calculate_area which override the base class but have the same name
#____________________________________________________________
# class Shape:
#     def calculate_area(self):
#         return None
#
# class Square(Shape):
#     side_length = 2
#
#     def calculate_area(self):       # overriding
#         return self.side_length * 2
#
# class Triangle(Shape):
#     base_length = 4
#     height = 3
#
#     def calculate_area(self):      # overriding
#         return 0.5 * self.base_length * self.height
#____________________________________________________________
# Overloading Built-in Methods:
# __add__(self, other) +
# __sub__(self, other) -
# __mul__(self, other) *
# __floordiv__(self, other) //
# __truediv__(self, other) /
# __pow__(self, other[, modulo]) **
# __lt__(self, other) <
# __le__(self, other) <=
# __eq__(self, other) ==
# __ne__(self, other) !=
# __gt__(self, other) >
# __ge__(self, other) >=

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self. age = age
#
#     def __len__(self):                  # overloading len method instead of length returns age cause Persons does not have lengths
#         return self.age
#
#     def __add__(self, other):     # overloading add method
#         return self.name + " " + other.name
#
# p1 = Person("Test1", 12)
# p2 = Person("Test2", 10)
# print(len(p1))
# print(p1 + p2)

# ---------------------------------------------------------------
# Duck typing -> Различни типове но с еднакви методи, задача 3.
# Влак и котка нямат нищо общо но имат мотод sound и за двата класа
# class Cat:
#     def sound(self):
#         print("Meow!")
#
#
# class Train:
#     def sound(self):
#         print("Sound from wheels slipping!")
#
#
# for any_type in Cat(), Train():
#     any_type.sound()
# ----------------------------------------------------------------
# Through abstraction, we hide all but the relevant
# data about an object to reduce complexity and increase efficiency
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod                # Shape class e abstract class and cannot initialize!!!
#     def calculate_area(self):
#         return None
#
# class Circle(Shape):                # ако не дефинитаме методите на Shape няма да работи, това ни гарантира че няма да имаме грешки после
#     def calculate_area(self):       # задължени сме да дефинираме методите на Parent clasa и кода няма да гърми
#         return "Something"
#
# # s = Shape()
# s_t = Circle()
# print(s_t)
# ------------------------------------------------------------------
# ▪ Abstract classes are classes that contain one or more abstract methods
# ▪ An abstract method is a method that is declared but contains no implementation
# ▪ Abstract classes may not be instantiated and require subclasses to provide implementations for the abstract methods


