import unittest

from dungeon import Hero, Enemy, Dungeon, Weapon, Spell


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

    def test_pick_treasure_should_return_random_weapon_or_spell(self):
        map = Dungeon('level1.txt')
        hero = Hero(name='Bron', title='Dragonslayer', health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)
        treasure = map.pick_treasure()

        self.assertIn(type(treasure), [Weapon, Spell, str])


if __name__ == '__main__':
    unittest.main()
