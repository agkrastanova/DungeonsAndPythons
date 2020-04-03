import unittest

from dungeon import Hero, Enemy


class TestHeroClass(unittest.TestCase):

    def test_instantiating_hero_with_wrong_type_name_should_raise_error(self):

        exc = None

        try:
            Hero(name = 123, title='Dragonslayer', health = 100, mana=100, mana_regeneration_rate=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Name should be string')

    def test_instantiating_hero_with_wrong_type_health_should_raise_error(self):

        exc = None

        try:
            Hero(name = 'Bron', title='Dragonslayer', health = 'asd', mana=100, mana_regeneration_rate=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Health should be positive integer')


    def test_instantiating_hero_with_wrong_type_mana_should_raise_error(self):

        exc = None

        try:
            Hero(name = 'Bron', title='Dragonslayer', health = 100, mana='asd', mana_regeneration_rate=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana should be positive integer')

    def test_instantiating_hero_with_wrong_type_mana_regeneration_rate_should_raise_error(self):

        exc = None

        try:
            Hero(name = 'Bron', title='Dragonslayer', health = 100, mana=100, mana_regeneration_rate='asd')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana_regeneration_rate should be positive integer')

    def test_instantiating_hero_with_negative_mana_regeneration_rate_should_raise_error(self):

        exc = None

        try:
            Hero(name = 'Bron', title='Dragonslayer', health = 100, mana=100, mana_regeneration_rate=-2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana_regeneration_rate should be positive integer')


    def test_known_as_representation_works_correctly(self):
        h = Hero(name='Bron', title='Dragonslayer', health=100, mana=100, mana_regeneration_rate=2)

        result = h.known_as()

        self.assertEqual(result, 'Bron the Dragonslayer')


class TestEnemyClass(unittest.TestCase):

    def test_instantiating_enemy_with_wrong_type_health_should_raise_error(self):

        exc = None

        try:
            Enemy(health='asd', mana=100, damage=20)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Health should be positive integer')

    def test_instantiating_enemy_with_negative_health_should_raise_error(self):

        exc = None

        try:
            Enemy(health=-1, mana=100, damage=20)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Health should be positive integer')


    def test_instantiating_enemy_with_wrong_type_mana_should_raise_error(self):

        exc = None

        try:
            Enemy(health=100, mana='asd', damage=20)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana should be positive integer')

    def test_instantiating_enemy_with_negative_mana_should_raise_error(self):

        exc = None

        try:
            Enemy(health=100, mana=-1, damage=20)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana should be positive integer')

    def test_instantiating_enemy_with_wrong_type_damage_should_raise_error(self):

        exc = None

        try:
            Enemy(health=100, mana=100, damage='asd')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Damage should be positive integer')

    def test_instantiating_enemy_with_negative_damage_should_raise_error(self):

        exc = None

        try:
            Enemy(health=100, mana=100, damage=-20)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Damage should be positive integer')



if __name__ == '__main__':
    unittest.main()