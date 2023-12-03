from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")
        service_to_add = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service_to_add)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        robot_to_add = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot_to_add)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_by_name(robot_name)
        service = self.find_service_by_name(service_name)

        if robot.STR_ROBOT_TYPE == "FemaleRobot":
            if service.STR_SERVICE_TYPE == "MainService":
                return "Unsuitable service."
        elif robot.STR_ROBOT_TYPE == "MaleRobot":
            if service.STR_SERVICE_TYPE == "SecondaryService":
                return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_service_by_name(service_name)
        robot_to_remove = next((r for r in service.robots if r.name == robot_name), None)
        if not robot_to_remove:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot_to_remove)
        self.robots.append(robot_to_remove)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service_by_name(service_name)
        for r in service.robots:
            r.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.find_service_by_name(service_name)
        total_sum = 0
        for r in service.robots:
            total_sum += r.price
        return f"The value of service {service_name} is {total_sum:.2f}."

    def __str__(self):
        return '\n'.join(s.details() for s in self.services)

    def find_robot_by_name(self, given_robot_name):
        return next((r for r in self.robots if r.name == given_robot_name), None)

    def find_service_by_name(self, given_service_name):
        return next((s for s in self.services if s.name == given_service_name), None)
