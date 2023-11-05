from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List = []  # contains Lion/Tiger/Cheetah classes
        self.workers: List = []  # contains Vet/Caretaker/Keeper classes

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

    def hire_worker(self, worker_name):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker_name)
            return f"{worker_name.name} the {worker_name.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        cur_total_salaries = 0
        for worker in self.workers:
            cur_total_salaries += worker.salary

        if cur_total_salaries <= self.__budget:
            self.__budget -= cur_total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        cur_total_cost_tending_animals = 0
        for animal in self.animals:
            cur_total_cost_tending_animals += animal.money_for_care

        if self.__budget >= cur_total_cost_tending_animals:
            self.__budget -= cur_total_cost_tending_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        sorted_animals_by_type = {"Lion": [], "Tiger": [], "Cheetah": []}
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                sorted_animals_by_type["Lion"].append(animal)
            elif animal.__class__.__name__ == "Tiger":
                sorted_animals_by_type["Tiger"].append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                sorted_animals_by_type["Cheetah"].append(animal)
        output = ""
        output += f"You have {len(self.animals)} animals \n"
        output += f"----- {len(sorted_animals_by_type['Lion'])} Lions:\n"
        for lion in sorted_animals_by_type['Lion']:
            output += f"{lion}\n"
        output += f"----- {len(sorted_animals_by_type['Tiger'])} Tigers:\n"
        for tiger in sorted_animals_by_type['Tiger']:
            output += f"{tiger}\n"
        output += f"----- {len(sorted_animals_by_type['Cheetah'])} Cheetahs:\n"
        for cheetah in sorted_animals_by_type['Cheetah']:
            output += f"{cheetah}\n"
        return output

    def workers_status(self):
        sorted_worker_by_type = {"Keeper": [], "Caretaker": [], "Vet": []}
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                sorted_worker_by_type["Keeper"].append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                sorted_worker_by_type["Caretaker"].append(worker)
            elif worker.__class__.__name__ == "Vet":
                sorted_worker_by_type["Vet"].append(worker)
        output = ""
        output += f"You have {len(self.workers)} workers \n"
        output += f"----- {len(sorted_worker_by_type['Keeper'])} Keepers:\n"
        for keeper in sorted_worker_by_type['Keeper']:
            output += f"{keeper}\n"
        output += f"----- {len(sorted_worker_by_type['Caretaker'])} Caretakers:\n"
        for caretaker in sorted_worker_by_type['Caretaker']:
            output += f"{caretaker}\n"
        output += f"----- {len(sorted_worker_by_type['Vet'])} Vets:\n"
        for vet in sorted_worker_by_type['Vet']:
            output += f"{vet}\n"
        return output
