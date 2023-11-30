from project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Betsi", "cow", "Muu")

    def test_constructor(self):
        self.assertEqual(self.mammal.name, "Betsi")
        self.assertEqual(self.mammal.type, "cow")
        self.assertEqual(self.mammal.sound, "Muu")
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_make_sound(self):
        expected_result = "Betsi makes Muu"
        result = self.mammal.make_sound()
        self.assertEqual(result, expected_result)

    def test_if_get_kingdom_returns_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        expected_result = "Betsi is of type cow"
        result = self.mammal.info()
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
