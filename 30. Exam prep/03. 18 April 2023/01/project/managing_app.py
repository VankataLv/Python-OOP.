from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.find_user_by_driving_license(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        vehicle = self.find_vehicle_by_license_plate(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."
        vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        filtered_route = self.find_route_by_sp_ep_length(start_point, end_point, length)
        if filtered_route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        filtered_route = self.find_shorter_route_by_sp_ep(start_point, end_point, length)
        if filtered_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        filtered_route = self.find_longer_route_by_sp_ep(start_point, end_point, length)
        if filtered_route:
            filtered_route.is_locked = True

        future_route_id = len(self.routes) + 1
        route_to_add = Route(start_point, end_point, length, future_route_id)
        self.routes.append(route_to_add)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self.find_user_by_driving_license(driving_license_number)
        vehicle = self.find_vehicle_by_license_plate(license_plate_number)
        route = self.find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()

        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        if count != 0:
            damaged_vehicles = []
            for v in self.vehicles:
                if v.is_damaged:
                    damaged_vehicles.append(v)

            if damaged_vehicles:
                damaged_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))

                vehicles_to_be_repaired = []
                if count >= len(damaged_vehicles):
                    vehicles_to_be_repaired = damaged_vehicles.copy()
                else:
                    for i in range(0, count):
                        vehicles_to_be_repaired.append(damaged_vehicles[i])

                for v in vehicles_to_be_repaired:
                    v.change_status()
                    v.recharge()
                return f"{len(vehicles_to_be_repaired)} vehicles were successfully repaired!"
            else:
                return "0 vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        result = "*** E-Drive-Rent ***\n"
        result += '\n'.join(user.__str__() for user in sorted_users)
        return result

    # ----------------------------------------------------------------------------------
    def find_route_by_id(self, given_id: int):
        return next((r for r in self.routes if r.route_id == given_id), None)

    def find_route_by_sp_ep_length(self, sp: str, ep: str, length: float):
        return next((r for r in self.routes if
                     r.start_point == sp and
                     r.end_point == ep and
                     r.length == length), None)

    def find_shorter_route_by_sp_ep(self, sp: str, ep: str, length: float):
        return next((r for r in self.routes if
                     r.start_point == sp and
                     r.end_point == ep and
                     r.length < length), None)

    def find_longer_route_by_sp_ep(self, sp: str, ep: str, length: float):
        return next((r for r in self.routes if
                     r.start_point == sp and
                     r.end_point == ep and
                     r.length > length), None)

    def find_user_by_driving_license(self, given_license: str):
        return next((u for u in self.users if u.driving_license_number == given_license), None)

    def find_vehicle_by_license_plate(self, given_license_plate: str):
        return next((v for v in self.vehicles if v.license_plate_number == given_license_plate), None)
