from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS_TYPES = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        searched_client = self.find_client_by_phone_num(client_phone_number)
        if searched_client:
            raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for cur_meal_to_add in meals:
            if cur_meal_to_add.__class__.__name__ in self.VALID_MEALS_TYPES.keys():
                self.menu.append(cur_meal_to_add)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = "\n".join(m.details() for m in self.menu)
        return result

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client_to_order = self.find_client_by_phone_num(client_phone_number)
        if not client_to_order:
            self.register_client(client_phone_number)

        for meal_name, qty in meal_names_and_quantities.items():
            if not self.check_validity_of_meal_by_name(meal_name):
                raise Exception(f"{meal_name} is not on the menu!")

            searched_meal = self.find_meal_by_name(meal_name)
            if searched_meal.quantity < qty:
                raise Exception(f"Not enough quantity of {searched_meal.__class__.__name}: {meal_name}!")

            client_to_order.shopping_cart.append(searched_meal)
            client_to_order.bill += qty * searched_meal.price
            searched_meal.quantity -= qty

        ordered_meal_names = []
        for ordered_meal in client_to_order.shopping_cart:
            ordered_meal_names.append(ordered_meal.name)
        return f"Client {client_phone_number} successfully ordered {', '.join(ordered_meal_names)} for {client_to_order.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client_to_cancel_order = self.find_client_by_phone_num(client_phone_number)
        if len(client_to_cancel_order.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        for meal_obj in client_to_cancel_order.shopping_cart:
            for meal_in_menu in self.menu:
                if meal_obj.__class__.__name__ == meal_in_menu.__class__.name__:
                    meal_in_menu.quantity += 1

        client_to_cancel_order.shopping_cart = []
        client_to_cancel_order.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client_to_pay = self.find_client_by_phone_num(client_phone_number)
        if len(client_to_pay.shopping_cart) < 1:
            raise Exception("There are no ordered meals!")

        client_to_pay.shopping_cart = []
        total_paid_money = client_to_pay.bill
        client_to_pay.bill = 0.0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def find_client_by_phone_num(self, phone_num_given: str):
        client = None
        for stored_client in self.clients_list:
            if stored_client.phone_number == phone_num_given:
                client = stored_client
        return client

    def check_validity_of_meal_by_name(self, given_meal_name: str) -> bool:
        for meal in self.menu:
            if meal.name == given_meal_name:
                return True
        return False

    def find_meal_by_name(self, given_name):
        meal = None
        for m in self.menu:
            if m.name == given_name:
                meal = m
        return meal


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)