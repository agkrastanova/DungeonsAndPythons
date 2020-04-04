import unittest

from dungeon import Hero, Enemy, Dungeon


class TestHeroClass(unittest.TestCase):

    def test_instantiating_hero_with_wrong_type_name_should_raise_error(self):

        exc = None

        try:
            Hero(name=123, title='Dragonslayer', health=100, mana=100, mana_regeneration_rate=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Name should be string')

    def test_instantiating_hero_with_wrong_type_health_should_raise_error(self):

        exc = None

        try:
            Hero(name='Bron', title='Dragonslayer', health='asd', mana=100, mana_regeneration_rate=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Health should be positive integer')

    def test_instantiating_hero_with_wrong_type_mana_should_raise_error(self):

        exc = None

        try:
            Hero(name='Bron', title='Dragonslayer', health=100, mana='asd', mana_regeneration_rate=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana should be positive integer')

    def test_instantiating_hero_with_wrong_type_mana_regeneration_rate_should_raise_error(self):

        exc = None

        try:
            Hero(name='Bron', title='Dragonslayer', health=100, mana=100, mana_regeneration_rate='asd')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana_regeneration_rate should be positive integer')

    def test_instantiating_hero_with_negative_mana_regeneration_rate_should_raise_error(self):

        exc = None

        try:
            Hero(name='Bron', title='Dragonslayer', health=100, mana=100, mana_regeneration_rate=-2)
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


class TestDungeonClass(unittest.TestCase):

    def test_load_map_function_should_take_map_from_txt_file(self):

        result = Dungeon('level1.txt')

        self.assertEqual(str(result), 'S.##.....T\n#T##..###.\n#.###E###E\n#.E...###.\n###T#####G')

    def test_print_map_function_should_print_map(self):

        load_map = Dungeon('level1.txt')

        printed_map = load_map.__str__()

        self.assertEqual(str(load_map), printed_map)

    def test_move_hero_up_should_return_true_if_can_move_or_false_if_not(self):
        map_ = Dungeon('level1.txt')
        map_.level_map[0][0] = 'H'

        result = map_.move_hero('up')

        self.assertEqual(result, False)

    def test_move_hero_left_should_return_true_if_can_move_or_false_if_not(self):
        map_ = Dungeon('level1.txt')
        map_.level_map[0][0] = 'H'

        result = map_.move_hero('left')

        self.assertEqual(result, False)

    def test_move_hero_right_should_return_true_if_can_move_or_false_if_not(self):
        map_ = Dungeon('level1.txt')
        map_.level_map[0][0] = 'H'

        result = map_.move_hero('right')

        self.assertEqual(result, True)

    def test_move_hero_down_should_return_true_if_can_move_or_false_if_not(self):
        map_ = Dungeon('level1.txt')
        map_.level_map[0][0] = 'H'

        result = map_.move_hero('down')

        self.assertEqual(result, False)

    def test_find_hero_returns_hero_coordinates_or_none_if_hero_not_found(self):
        map_ = Dungeon('level1.txt')

        result = map_.find_hero()
        expected = None
        self.assertEqual(result, expected)

        map_.level_map[0][0] = 'H'

        result = map_.find_hero()
        expected = (0, 0)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()