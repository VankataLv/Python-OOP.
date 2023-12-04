from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestsTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Ivan", 10.0)

    def test_constructor(self):
        self.assertEqual(self.driver.name, "Ivan")
        self.assertEqual(self.driver.money_per_mile, 10.0)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0.0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -100
        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_already_added_offer(self):
        self.driver.available_cargos = {"Sofia": 10}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 10)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))


    def test_add_cargo_offer_good_data(self):
        self.driver.available_cargos = {"Sofia": 10}
        result = self.driver.add_cargo_offer("Plovdiv", 100)
        self.assertEqual(self.driver.available_cargos, {"Sofia": 10, "Plovdiv": 100})
        expected_result = f"Cargo for 100 to Plovdiv was added as an offer."
        self.assertEqual(result, expected_result)

    def test_drive_best_cargo_offer_no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_with_good_data(self):
        self.driver.available_cargos = {"Sofia": 10, "Plovdiv": 100}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 1000)
        self.assertEqual(self.driver.miles, 100)
        expected_result = "Ivan is driving 100 to Plovdiv."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.driver.earned_money, 1000)

    def test_check_for_activities_250(self):
        self.driver.earned_money = 1000
        self.driver.check_for_activities(250)
        self.assertEqual(self.driver.earned_money, 980)

    def test_check_for_activities_1000(self):
        self.driver.earned_money = 1000
        self.driver.check_for_activities(1000)
        self.assertEqual(self.driver.earned_money, 875)

    def test_check_for_activities_1500(self):
        self.driver.earned_money = 1000
        self.driver.check_for_activities(1500)
        self.assertEqual(self.driver.earned_money, 335)

    def test_check_for_activities_10000(self):
        self.driver.earned_money = 100000
        self.driver.check_for_activities(10000)
        self.assertEqual(self.driver.earned_money, 88250)

    def test___repr__(self):
        result = self.driver.__repr__()
        expected_result = "Ivan has 0 miles behind his back."
        self.assertEqual(result, expected_result)

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")


if __name__ == "__main__":
    main()
