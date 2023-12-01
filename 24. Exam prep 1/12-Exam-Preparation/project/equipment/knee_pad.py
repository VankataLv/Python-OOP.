from equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self, protection: int, price: float):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        self.price *= 1.2
