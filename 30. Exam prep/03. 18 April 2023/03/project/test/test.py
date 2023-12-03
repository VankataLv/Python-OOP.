from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot1 = Robot("1", "Military", 10, 100.00)
        self.robot2 = Robot("2", "Military", 10, 50.00)
        self.robot3 = Robot("3", "Military", 10, 100.00)
        self.robot4 = Robot("4", "Military", 10, 200.00)

    def test_constructor(self):
        self.assertEqual(self.robot1.robot_id, "1")
        self.assertEqual(self.robot1.category, "Military")
        self.assertEqual(self.robot1.available_capacity, 10)
        self.assertEqual(self.robot1.price, 100.00)
        self.assertEqual(self.robot1.hardware_upgrades, [])
        self.assertEqual(self.robot1.software_updates, [])

    def test_category_setter_bad_data(self):
        with self.assertRaises(ValueError) as ve:
            self.robot1.category = "Unknown Category"
        self.assertEqual(f"Category should be one of '{self.robot1.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_setter_bad_data(self):
        with self.assertRaises(ValueError) as ve:
            self.robot1.price = -999
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_method_already_existing_component(self):
        self.robot1.hardware_upgrades.append("missile")
        result = self.robot1.upgrade("missile", 50.0)
        expected_result = f"Robot 1 was not upgraded."
        self.assertEqual(result, expected_result)

    def test_upgrade_method_new_component(self):
        result = self.robot1.upgrade("canon", 50.0)
        expected_result = 'Robot 1 was upgraded with canon.'
        self.assertEqual(result, expected_result)
        self.assertEqual(self.robot1.hardware_upgrades, ["canon"])
        self.assertEqual(self.robot1.price, 175.00)

    def test_cannot_update_already_higher_version(self):
        self.robot1.software_updates.append(2.0)
        result1 = self.robot1.update(1.0, 1)
        expected_result1 = "Robot 1 was not updated."
        self.assertEqual(result1, expected_result1)

    def test_cannot_update_no_capacity(self):
        self.robot1.available_capacity = 2
        result1 = self.robot1.update(5.0, 10)
        expected_result1 = "Robot 1 was not updated."
        self.assertEqual(result1, expected_result1)

    def test_good_update(self):
        result = self.robot1.update(1.1, 1)
        self.assertEqual(self.robot1.software_updates, [1.1])
        self.assertEqual(self.robot1.available_capacity, 9)
        expected_result = 'Robot 1 was updated to version 1.1.'
        self.assertEqual(result, expected_result)

    def test_greater_than(self):
        expected_result = 'Robot with ID 1 is more expensive than Robot with ID 2.'
        result = self.robot1.__gt__(self.robot2)
        self.assertEqual(result, expected_result)

    def test_equals(self):
        expected_result = 'Robot with ID 1 costs equal to Robot with ID 3.'
        result = self.robot1.__gt__(self.robot3)
        self.assertEqual(result, expected_result)

    def test_less(self):
        expected_result = 'Robot with ID 1 is cheaper than Robot with ID 4.'
        result = self.robot1.__gt__(self.robot4)
        self.assertEqual(result, expected_result)

        
if __name__ == "__main__":
    main()
