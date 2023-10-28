from project.task import Task
from typing import List


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            searched_task = next(filter(lambda x: x.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        searched_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        tasks_to_be_cleared = []
        for cur_task in self.tasks:
            if cur_task.completed:
                tasks_to_be_cleared.append(cur_task)
        for el in tasks_to_be_cleared:
            self.tasks.remove(el)
        return f"Cleared {len(tasks_to_be_cleared)} tasks."

    def view_section(self):
        tasks = '\n'.join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n{tasks}"

    # def __repr__(self):
    #     return f"{', '.join([t.details() for t in self.tasks])}"


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# # print(section.__repr__())
# print(section.clean_section())
# print(section.view_section())
