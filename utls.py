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

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

if __name__ == '__main__':
    main()