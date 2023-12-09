from project.trip import Trip
from unittest import TestCase, main


class TestsTrip(TestCase):
    def setUp(self) -> None:
        self.trip1 = Trip(10000.0, 1, False)
        self.trip2 = Trip(20000.0, 2, False)
        self.trip3 = Trip(30000.0, 3, True)

    def test_init(self):
        self.assertEqual(self.trip1.budget, 10000.0)
        self.assertEqual(self.trip1.travelers, 1)
        self.assertEqual(self.trip1.is_family, False)
        self.assertEqual(self.trip1.booked_destinations_paid_amounts, {})

    def test_travellers_setter_bad_data(self):
        with self.assertRaises(ValueError) as ve:
            self.trip1.travelers = 0
        self.assertEqual(str(ve.exception), 'At least one traveler is required!')

    def test_is_family_setter_bad_data(self):
        self.trip1.travelers = 1
        self.trip1.is_family = True
        self.assertEqual(self.trip1.is_family, False)

        self.trip1.travelers = 2
        self.trip1.is_family = False
        self.assertEqual(self.trip1.is_family, False)

    def test_is_family_setter_good_data(self):
        self.trip3.travelers = 4
        self.trip3.is_family = True
        self.assertEqual(self.trip3.is_family, True)

    def test_book_trip_not_existing_destination(self):
        self.trip4 = Trip(1000.0, 3, True)
        result = self.trip4.book_a_trip("Not existing destination")
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_book_trip_budget_not_enough(self):
        self.trip4 = Trip(200.0, 3, True)
        result = self.trip4.book_a_trip("Bulgaria")
        self.assertEqual(result, 'Your budget is not enough!')

    def test_book_trip_good_data(self):
        self.trip4 = Trip(1500.0, 3, True)
        result = self.trip4.book_a_trip("Bulgaria")
        self.assertEqual(self.trip4.booked_destinations_paid_amounts["Bulgaria"], 1350.0)
        self.assertEqual(self.trip4.budget, 150.0)
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 150.00')

        result1 = self.trip1.book_a_trip('New Zealand')
        self.assertEqual(self.trip1.booked_destinations_paid_amounts['New Zealand'], 7500.0)
        self.assertEqual(self.trip1.budget, 2500.0)
        self.assertEqual(result1, 'Successfully booked destination New Zealand! Your budget left is 2500.00')

    def test_booking_status_no_bookings(self):
        result = self.trip1.booking_status()
        self.assertEqual(result, 'No bookings yet. Budget: 10000.00')

    def test_booking_status_1_booking(self):
        self.trip1.book_a_trip("Bulgaria")
        result = self.trip1.booking_status()
        expected_result = (f"Booked Destination: Bulgaria\n"
                           f"Paid Amount: 500.00\n"
                           f"Number of Travelers: 1\n"
                           f"Budget Left: 9500.00")

        self.assertEqual(result, expected_result)

    def test_booking_status_2_bookings(self):
        self.trip1.book_a_trip("Bulgaria")
        self.trip1.book_a_trip("Australia")

        result = self.trip1.booking_status()
        expected_result = (f"Booked Destination: Australia\n"
                           f"Paid Amount: 5700.00\n"
                           f"Booked Destination: Bulgaria\n"
                           f"Paid Amount: 500.00\n"
                           f"Number of Travelers: 1\n"
                           f"Budget Left: 3800.00")

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
