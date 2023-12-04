from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_constructor(self):
        expected_toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(self.store.toy_shelf, expected_toy_shelf)

    def test_add_toy_1(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "car")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_2(self):
        self.store.add_toy("A", "car")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "car")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_3(self):
        self.store.add_toy("A", "doll")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "car")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_4(self):
        result = self.store.add_toy("A", "doll")
        self.assertEqual(result, "Toy:doll placed successfully!")

    def test_remove_toy_1(self):
        self.store.add_toy("A", "doll")
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "car")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_2(self):
        self.store.add_toy("A", "doll")
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "car")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_3(self):
        self.store.add_toy("A", "doll")
        result = self.store.remove_toy("A", "doll")
        self.assertEqual(result, "Remove toy:doll successfully!")
        self.assertEqual(self.store.toy_shelf["A"], None)


if __name__ == "__main__":
    main()
