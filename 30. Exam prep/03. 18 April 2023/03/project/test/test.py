from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestsTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Ivan", 21, 10.0)
        self.player2 = TennisPlayer("Petar", 21, 55.0)
        self.player3 = TennisPlayer("Vlado", 21, 5.0)

    def test_constructor(self):
        self.player = TennisPlayer("Ivan", 21, 10.0)
        self.assertEqual(self.player.name, "Ivan")
        self.assertEqual(self.player.age, 21)
        self.assertEqual(self.player.points, 10.0)
        self.assertEqual(self.player.wins, [])

    def test_name_setter_bad(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "a"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_bad(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_with_new_win(self):
        self.player.add_new_win("Sofia")
        self.assertEqual(self.player.wins, ["Sofia"])

    def test_add_new_win_with_existing_win(self):
        self.player.wins = ["Plovdiv", "Sofia"]
        result = self.player.add_new_win("Plovdiv")
        expected_result = f"Plovdiv has been already added to the list of wins!"
        self.assertEqual(result, expected_result)

    def test_lt_method_other_better(self):
        result = self.player.__lt__(self.player2)
        expected_result = 'Petar is a top seeded player and he/she is better than Ivan'
        self.assertEqual(result, expected_result)

    def test_lt_method_other_worse(self):
        result = self.player.__lt__(self.player3)
        expected_result = 'Ivan is a better player than Vlado'
        self.assertEqual(result, expected_result)

    def test_str_wins_one(self):
        self.player.add_new_win("Sofia")
        expected_result = f"Tennis Player: Ivan\n" \
                          f"Age: 21\n" \
                          f"Points: 10.0\n" \
                          f"Tournaments won: Sofia"
        result = self.player.__str__()
        self.assertEqual(result, expected_result)

    def test_str_no_wins(self):
        expected_result3 = f"Tennis Player: Vlado\n" \
                           f"Age: 21\n" \
                           f"Points: 5.0\n" \
                           f"Tournaments won: "
        result3 = self.player3.__str__()
        self.assertEqual(result3, expected_result3)

    def test_str_with_wins_two(self):
        self.player3.add_new_win("Sofia")
        self.player3.add_new_win("Varna")

        expected_result3 = f"Tennis Player: Vlado\n" \
                           f"Age: 21\n" \
                           f"Points: 5.0\n" \
                           f"Tournaments won: Sofia, Varna"
        result3 = self.player3.__str__()
        self.assertEqual(result3, expected_result3)


if __name__ == "__main__":
    main()
