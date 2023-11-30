from project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):

    def setUp(self):
        self.hero = Hero("Barb", 5, 100, 10)

    def test_constructor(self):
        self.assertEqual(self.hero.username, "Barb")
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 10)

    def test_battle_fight_same_username(self):
        self.enemy = Hero("Barb", 5, 100, 10)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_is_zero(self):
        self.hero.health = 0
        self.enemy = Hero("Necromongar", 15, 100, 5)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_is_zero(self):
        self.enemy = Hero("Necromongar", 15, 0, 5)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Necromongar. He needs to rest", str(ve.exception))

    def test_battle_correct_health_subtraction(self):
        self.enemy = Hero("Necromongar", 5, 100, 5)
        expected_result = "You lose"
        result = self.hero.battle(self.enemy)

        self.assertEqual(self.hero.health, 75)
        self.assertEqual(self.enemy.health, 55)
        self.assertEqual(expected_result, result)


    def test_battle_both_heroes_health_is_zero_after_battle(self):
        self.enemy = Hero("Necromongar", 10, 50, 10)
        expected_result = "Draw"
        result = self.hero.battle(self.enemy)
        self.assertEqual(expected_result, result)

    def test_battle_hero_wins_correct_attribute_values(self):
        self.enemy = Hero("Necromongar", 1, 10, 1)
        expected_result = "You win"
        result = result = self.hero.battle(self.enemy)

        self.assertEqual(expected_result, result)
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.health, 104)
        self.assertEqual(self.hero.damage, 15)

    def test_str(self):
        expected_result = f"Hero Barb: 5 lvl\n" \
                          f"Health: 100\n" \
                          f"Damage: 10\n"
        self.assertEqual(expected_result, self.hero.__str__())


if __name__ == "__main__":
    main()
