from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_TYPES_LOANS = {"StudentLoan": StudentLoan,
                         "MortgageLoan": MortgageLoan}
    VALID_TYPES_CLIENTS = {"Student": Student,
                           "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list = []
        self.clients: list = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_TYPES_LOANS:
            raise Exception("Invalid loan type!")
        self.loans.append(self.VALID_TYPES_LOANS[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_TYPES_CLIENTS:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        self.clients.append(self.VALID_TYPES_CLIENTS[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_client_id(client_id)
        if not client.LOANS_THAT_CAN_TAKE == loan_type:
            raise Exception("Inappropriate loan type!")
        loan = self.find_loan_by_type(loan_type)
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.find_client_by_client_id(client_id)
        if client not in self.clients:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if loan.LOAN_TYPE == loan_type:
                loan.increase_interest_rate()
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
        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        not_granted_sum = 0
        total_interest_rate = 0

        for client in self.clients:
            total_clients_income += client.income
            if self.clients:
                total_interest_rate += client.interest
            if client.loans:
                for loan in client.loans:
                    loans_count_granted_to_clients += 1
                    granted_sum += loan.amount

        for bank_loan in self.loans:
            not_granted_sum += bank_loan.amount

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_clients_income:.2f}
Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {total_interest_rate / len(self.clients):.2f}"""

    # ______________ SUPPORT METHODS ____________________
    def find_loan_by_type(self, given_loan_type):
        for cur_loan in self.loans:
            if cur_loan.LOAN_TYPE == given_loan_type:
                return cur_loan

    def find_client_by_client_id(self, given_id):
        for cur_el in self.clients:
            if cur_el.client_id == given_id:
                return cur_el

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
