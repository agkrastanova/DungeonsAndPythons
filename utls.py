class Mixin:
    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        alive = Mixin.get_health(self)
        return alive > 0

    def can_cast(self):
        return Mixin.get_mana(self) > 0 

    def take_damage(self,damage_points):
        self.health -= damage_points

        if self.health <= 0:
            self.health = 0
        return self.health

    def take_healing(healing_points):
        pass

    def take_mana(mana_points):
        pass

    def attack(by):
        pass

    def equip(weapon):
        pass

    def learn(spell):
        pass

class Weapon:
    pass

class Spell:
    pass