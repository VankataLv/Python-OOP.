from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("A3", "Audi", 100_000, 10_000.00)
        self.car2 = SecondHandCar("320", "BMW", 200_000, 20_000.00)
        self.car3 = SecondHandCar("A4", "Audi", 300_000, 5_000.00)

    def test_constructor(self):
        self.assertEqual(self.car.model, "A3")
        self.assertEqual(self.car.car_type, "Audi")
        self.assertEqual(self.car.mileage, 100_000)
        self.assertEqual(self.car.price, 10_000.00)

    def test_price_setter_bad_data(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_bad_data(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 52
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_promotional_price_higher_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(20000.0)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_promotional_price_lower_price(self):
        result = self.car.set_promotional_price(5000.0)
        self.assertEqual(self.car.price, 5000.0)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_bad_data(self):
        result = self.car.need_repair(50_000, "Total Fail")
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_possible_repair(self):
        result = self.car.need_repair(1_000, "Coils")
        self.assertEqual(f'Price has been increased due to repair charges.', result)
        self.assertEqual(self.car.price, 11_000)
        self.assertEqual(self.car.repairs, ["Coils"])

    def test_gt_mismatch(self):
        result = self.car.__gt__(self.car2)
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_gt_good(self):
        result = self.car.__gt__(self.car3)
        self.assertTrue(result)

    def test_str_method(self):
        result = self.car.__str__()
        expected_result = """Model A3 | Type Audi | Milage 100000km
Current price: 10000.00 | Number of Repairs: 0"""
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()