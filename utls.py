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

    def take_mana(self, mana_points):
        if not self.is_alive():
            return False

        self.mana += mana_points

        if self.mana > self.max_mana:
            self.mana = self.max_mana
        elif self.mana < 0:
            self.mana = 0

    def attack(self, by):
        if by == "weapon":
            if self.weapon != None:
                return self.weapon.damage
            else:
                return 0
        elif by == "spell":
            if self.spell != None:
                return self.spell.damage
            else:
                return 0
        else:
            raise ValueError("Invalid arguement.")

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

class Weapon:
    pass

class Spell:
    pass