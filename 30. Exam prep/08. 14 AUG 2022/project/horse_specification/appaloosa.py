from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    STRING_HORSE_TYPE = "Appaloosa"

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed += 2
