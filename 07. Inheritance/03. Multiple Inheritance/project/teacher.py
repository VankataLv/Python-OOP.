from project.employee import Employee
from project.person import Person


class Teacher(Employee, Person):
    def __init__(self):
        Employee.__init__(self)
        Person.__init__(self)

    def teach(self) -> str:
        return "teaching..."
