from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        battery_consumed = mileage / self.MAX_MILEAGE
        battery_consumed *= 100
        battery_consumed = round(battery_consumed)
        self.battery_level -= battery_consumed
