class Mixin:
    def is_alive():
        pass

    def can_cast():
        pass

    def get_health():
        pass

    def get_mana():
        pass

    def take_damage(damage_points):
        pass

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        self.health += healing_points

        if self.health > self.max_health:
            self.health = self.max_health

        return True

    def take_mana(mana_points):
        pass

    def attack(by):
        pass

    def equip(self, weapon):
        self.weapon = weapon

    def learn(spell):
        pass

class Weapon:
    pass

class Spell:
    pass