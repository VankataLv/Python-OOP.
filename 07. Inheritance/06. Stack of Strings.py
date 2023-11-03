class Stack:
    def __init__(self):
        self.data = list()

    def push(self, element: str):
        if not isinstance(element, str):
            raise ValueError("Element is not string!")
        self.data.append(element)

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        element = self.data[-1]
        return element

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f'[{", ".join(reversed_data)}]'


