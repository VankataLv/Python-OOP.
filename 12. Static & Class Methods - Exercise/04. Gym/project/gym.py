from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans:list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next((s for s in self.subscriptions if subscription_id == s.id), None)
        customer = next((c for c in self.customers if subscription.customer_id == c.id), None)
        trainer = next((t for t in self.trainers if subscription.trainer_id == t.id), None)
        plan = next((p for p in self.plans if subscription.exercise_id == p.id), None)
        equipment = next((e for e in self.equipment if plan.equipment_id == e.id), None)

        return '\n'.join([subscription.__repr__(),
                          customer.__repr__(),
                          trainer.__repr__(),
                          equipment.__repr__(),
                          plan.__repr__()])