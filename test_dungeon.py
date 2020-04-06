import unittest

from dungeon import Hero, Enemy, Dungeon, Weapon, Spell, Fight


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
        h = Hero('hero', 'the hero', 100, 100, 2)
        map_.spawn(h)
        h.take_mana(-10)

        result = map_.move_hero('right')

        self.assertEqual(result, True)
        self.assertEqual(h.get_mana(), 92)

    def test_move_hero_down_should_return_true_if_can_move_or_false_if_not(self):
        map_ = Dungeon('level1.txt')
        map_.level_map[0][0] = 'H'

        result = map_.move_hero('down')

        self.assertEqual(result, False)

    def test_move_hero_should_increase_hero_mana(self):
        map_ = Dungeon('level1.txt')
        map_.level_map[0][0] = 'H'

        result = map_.move_hero('right')

        self.assertEqual(result, True)

    def test_find_hero_returns_hero_coordinates_or_none_if_hero_not_found(self):
        map_ = Dungeon('level1.txt')

        result = map_.find_hero(map_.level_map)
        expected = None
        self.assertEqual(result, expected)

        map_.level_map[0][0] = 'H'

        result = map_.find_hero(map_.level_map)
        expected = (0, 0)

        self.assertEqual(result, expected)

    def test_pick_treasure_should_return_random_weapon_or_spell(self):
        map = Dungeon('level1.txt')
        hero = Hero(name='Bron', title='Dragonslayer', health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)
        treasure = map.pick_treasure()

        self.assertIn(type(treasure), [Weapon, Spell, str])


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

    def test_hero_attack_by_spell_returns_false_if_no_fight(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map = Dungeon('level1.txt')
        map.spawn(hero)
        spell = Spell('fireball', 20, 20, 2)
        hero.spell = spell

        result = map.hero_attack(by='spell')

        self.assertEqual(result, False)

    def test_hero_attack_by_spell_returns_true_if_fight_starts(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map_ = Dungeon('level1.txt')
        map_.spawn(hero)
        weapon = Weapon('Axe', damage=20)
        hero.equip(weapon)
        spell = Spell('fireball', 20, 20, 2)
        hero.spell = spell
        map_.move_hero('right')
        map_.move_hero('down')
        map_.move_hero('down')
        map_.move_hero('down')

        result = map_.hero_attack(by='spell')

        self.assertEqual(result, True)


class TestFightClass(unittest.TestCase):
    def test_init_should_raise_type_error_if_hero_or_enemy_not_of_their_type(self):
        map_ = Dungeon('level1.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = "enemy"

        exc = None
        try:
            Fight(hero, enemy, level_map=map_.level_map)
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid type.')

        hero = "hero"
        enemy = Enemy(health=100, mana=20, damage=20)

        exc = None
        try:
            Fight(hero, enemy, level_map=map_.level_map)
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid type.')

    def test_init_fight_should_save_hero_and_enemy(self):
        map_ = Dungeon('level1.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        weapon = Weapon('Axe', 20)
        spell = Spell('Fireball', 20, 50, 2)
        hero.equip(weapon)
        hero.learn(spell)
        enemy = Enemy(health=100, mana=20, damage=20)

        fight = Fight(hero, enemy, level_map=map_.level_map)

        self.assertEqual((hero, enemy), (fight.hero, fight.enemy))

    def test_if_spawn_function_populates_first_spawning_point_correctly(self):
        level_map = Dungeon('level1.txt')

        h = Hero(name='Bron', title='Dragonslayer', health=100, mana=100, mana_regeneration_rate=2)

        result = level_map.spawn(h)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
