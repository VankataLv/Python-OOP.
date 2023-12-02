from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list[BaseLoan] = []
        self.clients: list[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")
        loan_to_create = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan_to_create)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        client_to_add = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client_to_add)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self.find_loan_by_type(loan_type)
        client = self.find_client_by_id(client_id)
        if not client.ALLOWED_LOAN == loan_type:                # check if it works
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for bank_loan in self.loans:
            if bank_loan.__class__.__name__ == loan_type:
                bank_loan.increase_interest_rate()
                counter += 1
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_clients_income = sum(c.income for c in self.clients)

        granted_sum = 0
        loans_count_granted_to_clients = 0
        for c in self.clients:
            if c.loans:
                for l in c.loans:
                    granted_sum += l.amount
                    loans_count_granted_to_clients += 1

        not_granted_sum = 0
        if self.loans:
            for l in self.loans:
                not_granted_sum += l.amount

        avg_client_interest_rate = 0

        for c in self.clients:
            avg_client_interest_rate += c.interest

        if self.clients:
            avg_client_interest_rate /= len(self.clients)

        result = f"""Active Clients: {len(self.clients)}
Total Income: {total_clients_income:.2f}
Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_interest_rate:.2f}"""

        return result

    def find_loan_by_type(self, given_loan_type):
        return next((l for l in self.loans if l.__class__.__name__ == given_loan_type), None)

    def find_client_by_id(self, given_client_id):
        return next((c for c in self.clients if c.client_id == given_client_id), None)
