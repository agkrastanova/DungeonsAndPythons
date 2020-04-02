import unittest

from dungeon import Hero, Enemy


class TestHeroClass(unittest.TestCase):

    def test_known_as_representation_works_correctly(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        result = h.known_as()

        self.assertEqual(result, 'Bron the Dragonslayer')


class TestEnemyClass(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
