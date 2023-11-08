# @ првави метода статичен, метода не знае нищо за метода или за инстанцията
# ако се налага да създаваме атрибут в класа използваме @classmethod
# class Math:
#     def __init__(self, num):
#         self.num = num
#
#     def sum_number(self, number):
#         pass
#         # заради self този метод знае всичко за метода
#
#     def sum_nums(self, a, b):
#         return a + b
#         # подчертава името защото метода не използва нищо от класа
#
#     @staticmethod  # декорираме метода с @staticmethod и трием self
#     def sum_nums_static_method(a, b):
#         return a + b
        # отказваме се от self и би трябвало да го изтрием

# Защо държим статик методи в класа като не използваме нищо от класа?
# Защото държим всичко на едно място и пакетираме всичко заедно.
# може да бъде бъде викан статик метод както от инстанцията "m" така и от самия клас "Math"
# m = Math(5)
# print(m.sum_nums_static_method(5, 6))
# print(Math.sum_nums_static_method(5, 6))
#  в бъдеще ако някой ползва нашия код, сме сигурни че той няма да модифицира нищо в класа през self и този метод
# при наследяване статичните методи се наследяват също освен ако не са private methods -> __name_static_method!
# ____________________________________________
# Клас методи
# клас параметрите започват с първи параметър "cls" и се записват с @classmethod. cls == class
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def pepperoni(cls):
#         return cls(["tomato sauce", "parmesan", "pepperoni"])
#
#     @classmethod
#     def quattro_formaggi(cls):
#         return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])
#
#
# first_pizza = Pizza.pepperoni()
# second_pizza = Pizza.quattro_formaggi()
# print(first_pizza.ingredients)
# print(second_pizza.ingredients)
# # използва се контролирано създаване на атрибути и др. в класовете

