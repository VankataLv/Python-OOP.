from project.services.base_service import BaseService


class MainService(BaseService):
    STR_SERVICE_TYPE = "MainService"

    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):
        if self.robots:
            return f"""{self.name} Main Service:
Robots: {' '.join(r.name for r in self.robots)}"""
        else:
            return f"""{self.name} Main Service:
Robots: none"""
