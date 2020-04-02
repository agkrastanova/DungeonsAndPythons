from utls import Mixin, Weapon, Spell

class Hero(Mixin):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        if type(name) is not str:
            raise TypeError('Name should be string')

        if type(health) is not int:
            raise TypeError('Health should be number')

        if type(mana) is not int:
            raise TypeError('Mana should be number')

        if type(mana_regeneration_rate) is not int:
            raise TypeError('Mana_regeneration_rate should be integer')
        elif mana_regeneration_rate < 0:
            raise ValueError('Mana_regeneration_rate cannot be negative')

        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_health = health
        self.max_mana = mana

    def known_as(self):
        return(f'{self.name} the {self.title }')

class Enemy(Mixin):
	
    def __init__(self,health, mana, damage): 

        if type(health) is not int:
            raise TypeError('Health should be number')
        elif health <= 0:
            raise ValueError('Health cannot be zero or negative')

        if type(mana) is not int:
            raise TypeError('Mana should be number')
        elif mana < 0 :
            raise ValueError('Mana cannot be negative')

        if type(damage) is not int:
            raise TypeError('Damage should be number')
        elif damage < 0:
            raise ValueError('Damage cannot be negative')

        self.health = health
        self.mana = mana
        self.damage = damage
        self.max_health = health
        self.max_damage = damage

class Dungeon:

    def load_map():
        pass

    def print_map():
        pass

    def spawn(hero):
        pass

    def move_hero(direction):
        pass

    def pick_treasure():
        pass



if __name__ == '__main__':
    main()