from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST = 2.0
    LOANS_THAT_CAN_TAKE = "StudentLoan"

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 1.0
