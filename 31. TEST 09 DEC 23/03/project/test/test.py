from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque


class TestsRailwayStation(TestCase):
    def setUp(self) -> None:
        self.rs = RailwayStation("Sofia")

    def test_constructor(self):
        self.assertEqual(self.rs.name, "Sofia")
        self.assertEqual(self.rs.arrival_trains, deque())
        self.assertEqual(self.rs.departure_trains, deque())

    def test_name_setter_bad_data(self):
        with self.assertRaises(ValueError) as ve:
            self.rs.name = "S"
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board_clear_board(self):
        self.rs.new_arrival_on_board("TestArrivingTrain")
        self.assertEqual(self.rs.arrival_trains, deque(["TestArrivingTrain"]))

    def test_new_arrival_on_board_busy_board(self):
        self.rs.new_arrival_on_board("TestArrivingTrain1")
        self.rs.new_arrival_on_board("TestArrivingTrain2")
        self.assertEqual(self.rs.arrival_trains, deque(["TestArrivingTrain1", "TestArrivingTrain2"]))

    def test_train_has_arrived_first_case(self):
        self.rs.new_arrival_on_board("TestArrivingTrain1")
        self.rs.new_arrival_on_board("TestArrivingTrain2")
        result = self.rs.train_has_arrived("TestArrivingTrain2")
        expected_result = "There are other trains to arrive before TestArrivingTrain2."
        self.assertEqual(result, expected_result)

    def test_train_has_arrived_second_case(self):
        self.rs.new_arrival_on_board("TestArrivingTrain1")
        self.rs.new_arrival_on_board("TestArrivingTrain2")
        result = self.rs.train_has_arrived("TestArrivingTrain1")
        expected_result = "TestArrivingTrain1 is on the platform and will leave in 5 minutes."
        self.assertEqual(self.rs.departure_trains, deque(["TestArrivingTrain1"]))
        self.assertEqual(result, expected_result)

    def test_train_has_left_expected_True(self):
        self.rs.new_arrival_on_board("TestArrivingTrain1")
        self.rs.new_arrival_on_board("TestArrivingTrain2")
        self.rs.train_has_arrived("TestArrivingTrain1")
        self.assertTrue(self.rs.train_has_left("TestArrivingTrain1"))
        self.assertEqual(self.rs.departure_trains, deque())

    def test_train_has_left_expected_False(self):
        self.rs.new_arrival_on_board("TestArrivingTrain1")
        self.rs.new_arrival_on_board("TestArrivingTrain2")
        self.rs.train_has_arrived("TestArrivingTrain1")
        self.assertFalse(self.rs.train_has_left("TestArrivingTrain2"))
        self.assertEqual(self.rs.departure_trains, deque(["TestArrivingTrain1"]))


if __name__ == "__main__":
    main()