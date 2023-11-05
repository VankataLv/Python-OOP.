from project.dough import Dough
from project.topping import Topping
from typing import Dict


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[Topping.topping_type: Topping.weight] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = value

    @property
    def dough(self):
        return self.__name

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        else:
            self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        else:
            self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) < self.max_number_of_toppings:
            if topping.topping_type not in self.toppings.keys():
                self.toppings[topping.topping_type] = topping.weight
            else:
                self.toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        weight_cur_pizza = 0
        weight_cur_pizza += self.__dough.weight
        for key in self.toppings.keys():
            weight_cur_pizza += self.toppings[key]
        return weight_cur_pizza
