from project.services.base_service import BaseService


class SecondaryService(BaseService):
    STR_SERVICE_TYPE = "SecondaryService"

    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def details(self):
        if self.robots:
            return f"""{self.name} Secondary Service:
Robots: {' '.join(r.name for r in self.robots)}"""
        else:
            return f"""{self.name} Secondary Service:
Robots: none"""
