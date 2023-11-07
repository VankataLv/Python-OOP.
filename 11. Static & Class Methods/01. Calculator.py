from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)  # за x и y, приложи +, от iterable (може да 0, 1 или много аргументи)
    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)
    @staticmethod
    def divide(*args):
        try:
            return reduce(lambda x, y: x / y, args)
        except ZeroDivisionError:
            return "Cannot divide by zero"
    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

# В теста статик метода е извикан през класа!!!

# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))