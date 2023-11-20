from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SERVICE_TYPE = "Secondary"
    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def details(self):
        result = f"{self.name} Secondary Service:\n"
        if self.robots:
            result += f"Robots: {' '.join(r.name for r in self.robots if self.robots)}"
        else:
            result += "Robots: none"
        return result
