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

    def take_damage(self, damage_points):
        self.health -= damage_points

        if self.health <= 0:
            self.health = 0
        return self.health

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

        return True

    def attack(self, by):
        if by == "weapon":
            if self.weapon is not None:
                return self.weapon.damage
            else:
                return 0
        elif by == "spell":
            if self.spell is not None:
                return self.spell.damage
            else:
                return 0

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell


class Weapon:
    def __init__(self, name, damage):
        if type(name) is not str:
            raise ValueError('Name should be string')
        if type(damage) is not int or damage < 0:
            raise ValueError('Damage should be positive integer')

        self.name = name
        self.damage = damage

    def __str__(self):
        return f'{self.name}, damage: {self.damage}'


class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.validate_spell_arguments(name, damage, mana_cost, cast_range)

        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return f'{self.name}, damage: {self.damage}, mana cost: {self.mana_cost}, cast range: {self.cast_range}'

    @staticmethod
    def validate_spell_arguments(name, damage, mana_cost, cast_range):
        if type(name) is not str:
            raise ValueError('Name should be string')

        if type(damage) is not int or damage < 0:
            raise ValueError('Damage should be positive integer')

        if type(mana_cost) is not int or mana_cost < 0:
            raise ValueError('Mana_cost should be positive integer')

        if type(cast_range) is not int or cast_range < 0:
            raise ValueError('Cast_range should be positive integer')
