from car_manager import Car
from unittest import TestCase, main


class CarTests(TestCase):

    def setUp(self) -> None:
        self.car = Car("Audi", "A3", 6, 55)

    def test_initialization(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("A3", self.car.model)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(55, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "A3", 6, 55)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Audi", "", 6, 55)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_invalid_consumption_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Audi", "A3", 0, 55)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_invalid_consumption_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Audi", "A3", -10, 55)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_invalid_capacity_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Audi", "A3", 6, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_invalid_capacity_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Audi", "A3", 6, -55)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_invalid_fuel_amount_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_fuel_attribute_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_fuel_more_than_capacity(self):
        self.car.refuel(100)
        self.assertEqual(55, self.car.fuel_amount)

    def test_drive_not_enough_fuel(self):
        self.car.fuel_amount = 10
        with self.assertRaises(Exception) as ex:
            self.car.drive(100000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_correct_amount_fuel_left(self):
        self.car.fuel_amount = 10
        self.car.drive(10)

        self.assertEqual(9.4, self.car.fuel_amount)


if __name__ == "__main__":
    main()
