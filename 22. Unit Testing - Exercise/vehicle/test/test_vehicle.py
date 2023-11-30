from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTests(TestCase):

    def setUp(self) -> None:
        self.audi = Vehicle(55.0, 150.0)

    def test_constructor(self):
        self.assertEqual(self.audi.fuel, 55.0)
        self.assertEqual(self.audi.capacity, 55.0)
        self.assertEqual(self.audi.horse_power, 150.0)
        self.assertEqual(self.audi.fuel_consumption, self.audi.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.audi.drive(10_000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_correct_amount_fuel(self):
        fuel_needed = 42.5
        self.audi.drive(10)
        self.assertEqual(fuel_needed, self.audi.fuel)

    def test_refuel_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.audi.refuel(10000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_correct_amount_fuel(self):
        self.audi.fuel = 10.0
        self.audi.refuel(10.0)
        expected_result = 20.0
        self.assertEqual(expected_result, self.audi.fuel)

    def test_str_output(self):
        expected_result = f"The vehicle has 150.0 " \
                          f"horse power with 55.0 fuel left and 1.25 fuel consumption"
        result = self.audi.__str__()

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
