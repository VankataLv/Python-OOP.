from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 120)

    def miss(self, time_to_catch: int):
        new_oxygen = self.oxygen_level - (0.6 * time_to_catch)
        new_oxygen = round(new_oxygen, 0)
        if new_oxygen < 0:
            self.oxygen_level = 0
            BaseDiver.update_health_status(self)
        else:
            self.oxygen_level = new_oxygen

    def renew_oxy(self):
        self.oxygen_level = 120
