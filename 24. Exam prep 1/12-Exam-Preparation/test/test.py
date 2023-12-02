from unittest import TestCase, main
from project.trip import Trip


class TripTests(TestCase):
    def setUp(self) -> None:
        self.t1f = Trip(10000, 1, False)
        self.t2t = Trip(10000, 3, True)
        self.t3f = Trip(20000, 2, False)

    def test_constructor_initialization(self):
        self.assertEqual(self.t1f.budget, 10000)
        self.assertEqual(self.t1f.travelers, 1)
        self.assertEqual(self.t1f.is_family, False)
        self.assertEqual(self.t1f.booked_destinations_paid_amounts, {})

        self.assertEqual(self.t2t.is_family, True)
        self.assertEqual(self.t3f.is_family, False)

    def test_travellers_props(self):
        with self.assertRaises(ValueError) as ve:
            self.t1f.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_book_a_trip_error_wrong_destinations(self):
        result = self.t1f.book_a_trip("Wrong Destination")
        expected_result = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(result, expected_result)

    def test_correct_price_and_budget_and_booking(self):
        result = self.t1f.book_a_trip("Bulgaria")
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 9500.00')

        self.t2t.book_a_trip("Bulgaria")
        self.assertEqual(self.t2t.budget, 8650)
        self.assertEqual(self.t2t.booked_destinations_paid_amounts, {'Bulgaria': 1350.0})

    def test_not_enough_budget(self):
        result = self.t2t.book_a_trip('New Zealand')
        self.assertEqual(result, 'Your budget is not enough!')

    def test_no_bookings_yet(self):
        result = self.t1f.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: {self.t1f.budget:.2f}')

    def test_successful_booking(self):
        self.t1f.book_a_trip("Bulgaria")
        result = self.t1f.booking_status()
        expected_result = (f"""Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 9500.00""")
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()

