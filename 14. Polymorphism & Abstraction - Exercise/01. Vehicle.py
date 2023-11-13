from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance:float) -> None:
        return None

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        return None


class Car(Vehicle):
    SUMMER_CONDITIONS = 0.9

    def drive(self, distance: float):
        consumption = self.fuel_consumption + Car.SUMMER_CONDITIONS
        fuel_needed = consumption * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_CONDITIONS = 1.6
    HOLE_IN_TANK = 0.95

    def drive(self, distance: float):
        consumption = self.fuel_consumption + Truck.SUMMER_CONDITIONS
        fuel_needed = consumption * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * Truck.HOLE_IN_TANK


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
