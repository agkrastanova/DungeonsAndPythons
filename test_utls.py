import unittest
from utls import Mixin, Weapon, Spell, Fight, Hero, Enemy


class TestMixinClass(unittest.TestCase):
    def test_get_health_function_should_return_current_health(self):

        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        result = Mixin.get_health(h)

        self.assertEqual(result, 100)

    def test_is_alive_function_returns_true_if_get_health_is_not_zero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        result = Mixin.is_alive(h)

        self.assertTrue(result)

    def test_can_cast_function_should_return_true_if_object_can_cast(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        result = Mixin.can_cast(h)

        self.assertTrue(result)

    def test_take_damage_should_reduce_health_with_damage_points(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        reduced_health = Mixin.take_damage(h, 65)

        self.assertEqual(reduced_health, 35)

        reduced_health2 = Mixin.take_damage(h, 50)

        self.assertEqual(reduced_health2, 0)

        health = Mixin.get_health(h)

        self.assertEqual(health, 0)

    def test_get_mana_should_return_current_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        mana = Mixin.get_mana(h)

        self.assertEqual(mana, 100)

    def test_take_healing_when_hero_is_not_alive_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        h.health = 0
        result = h.take_healing(100)

        self.assertEqual(result, False)

    def test_take_healing_when_hero_is_alive_and_healing_is_less_than_max_health_should_return_True_and_hero_health_is_changed(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        h.health = 10
        result = h.take_healing(50)

        self.assertEqual(result, True)
        self.assertEqual(h.health, 60)

    def test_take_healing_when_hero_is_alive_and_healing_is_greater_than_max_should_return_True_and_health_must_be_max(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        h.health = 10
        result = h.take_healing(100)

        self.assertEqual(result, True)
        self.assertEqual(h.health, 100)

    def test_take_mana_when_hero_is_not_alive_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        h.health = 0
        result = h.take_mana(20)

        self.assertEqual(result, False)

    def test_take_mana_when_hero_is_alive_should_return_true_and_icrease_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        h.mana = 0
        result = h.take_mana(20)

        self.assertEqual(result, True)
        self.assertEqual(h.mana, 20)

    def test_take_mana_when_hero_is_alive_and_mana_is_more_than_max_should_return_true_and_make_mana_max(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        h.mana = 0
        result = h.take_mana(120)

        self.assertEqual(result, True)
        self.assertEqual(h.mana, 100)

    def test_equip_hero_weapon_must_be_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        weapon = Weapon(name='Axe', damage=20)
        h.equip(weapon)

        self.assertEqual(h.weapon, weapon)

    def test_learn_spell_hero_spell_must_be_the_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        spell = Spell(name='Fireball', damage=20, mana_cost=20, cast_range=2)
        h.learn(spell)

        self.assertEqual(h.spell, spell)

    def test_attack_method_when_by_weapon_when_no_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        result = h.attack(by='weapon')

        self.assertEqual(result, 0)

    def test_attack_method_when_by_weapon_when_has_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        weapon = Weapon(name='Axe', damage=20)
        h.equip(weapon)

        result = h.attack(by='weapon')

        self.assertEqual(result, 20)

    def test_attack_method_when_by_spell_when_no_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        result = h.attack(by='spell')

        self.assertEqual(result, 0)

    def test_attack_method_when_by_spell_when_has_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        spell = Spell(name='Fireball', damage=20, mana_cost=20, cast_range=2)
        h.learn(spell)

        result = h.attack(by='spell')

        self.assertEqual(result, 20)


class TestWeaponClass(unittest.TestCase):
    def test_instantiating_weapon_wrong_type_name_should_raise_error(self):
        exc = None

        try:
            Weapon(name=123, damage=20)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Name should be string')

    def test_instantiating_weapon_with_wrong_damage_value_should_raise_error(self):

        exc = None

        try:
            Weapon(name='Axe', damage=-20)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Damage should be positive integer')

    def test_weapon_str_repr(self):
        weapon = Weapon(name='Axe', damage=20)

        self.assertEqual(str(weapon), 'Axe, damage: 20')


class TestSpellClass(unittest.TestCase):
    def test_instantiating_spell_with_wrong_type_name_should_raise_error(self):
        exc = None

        try:
            Spell(name=123, damage=20, mana_cost=20, cast_range=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Name should be string')

    def test_instantiating_spell_with_wrong_damage_value_should_raise_error(self):
        exc = None

        try:
            Spell(name='Fireball', damage=-20, mana_cost=20, cast_range=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Damage should be positive integer')

    def test_instantiating_spell_with_wrong_mana_cost_value_should_raise_error(self):
        exc = None

        try:
            Spell(name='Fireball', damage=20, mana_cost=-20, cast_range=2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Mana_cost should be positive integer')

    def test_instantiating_spell_with_wrong_cast_range_value_should_raise_error(self):
        exc = None

        try:
            Spell(name='Fireball', damage=20, mana_cost=20, cast_range='a')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Cast_range should be positive integer')

    def test_spell_str_repr(self):
        spell = Spell(name='Fireball', damage=20, mana_cost=20, cast_range=2)

        self.assertEqual(str(spell), 'Fireball, damage: 20, mana cost: 20, cast range: 2')


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


class TestFightClass(unittest.TestCase):
    def test_init_should_raise_type_error_if_hero_or_enemy_not_of_their_type(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = "enemy"

        exc = None
        try:
            Fight(hero, enemy)
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid type.')

        hero = "hero"
        enemy = Enemy(health=100, mana=20, damage=20)

        exc = None
        try:
            Fight(hero, enemy)
        except Exception as e:
            exc = e

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid type.')

    def test_init_fight_should_save_hero_and_enemy(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=20, damage=20)

        fight = Fight(hero, enemy)

        self.assertEqual((hero, enemy), (fight.hero, fight.enemy))


if __name__ == '__main__':
    unittest.main()
