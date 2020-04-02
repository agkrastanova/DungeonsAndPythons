import unittest

from utls import Mixin, Weapon, Spell
from dungeon import Hero, Enemy

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

        reduced_health = Mixin.take_damage(h,65)

        self.assertEqual(reduced_health, 35)

        reduced_health2 = Mixin.take_damage(h,50)

        self.assertEqual(reduced_health2, 0)

        health = Mixin.get_health(h)

        self.assertEqual(health, 0)

    def test_get_mana_should_return_current_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        mana = Mixin.get_mana(h)

        self.assertEqual(mana, 100)


class TestWeaponClass(unittest.TestCase):
    pass

class TestSpellClass(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()