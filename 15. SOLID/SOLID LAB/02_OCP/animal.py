from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Turtle(Animal):
    def make_sound(self):
        return "Tur"


def animal_sound(all_animals: list[Animal]):
    for animal in all_animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Turtle(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
