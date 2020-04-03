from utls import Mixin, Weapon, Spell


class Hero(Mixin):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.validate_arguments_hero(name, health, mana, mana_regeneration_rate)

        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
       
        self.max_health = health
        self.max_mana = mana


    def known_as(self):
        return(f'{self.name} the {self.title }')


    @staticmethod
    def validate_arguments_hero(name, health, mana, mana_regeneration_rate):

        if type(name) is not str:
            raise TypeError('Name should be string')

        if type(health) is not int or health <= 0:
            raise TypeError('Health should be positive integer')

        if type(mana) is not int or mana <= 0:
            raise TypeError('Mana should be positive integer')

        if type(mana_regeneration_rate) is not int or mana_regeneration_rate <= 0:
            raise TypeError('Mana_regeneration_rate should be positive integer')
        


class Enemy(Mixin):
	
    def __init__(self,health, mana, damage): 
        self.validate_arguments_enemy(health, mana, damage)

        self.health = health
        self.mana = mana
        self.damage = damage
        self.max_health = health
        self.max_mana = mana

    @staticmethod
    def validate_arguments_enemy(health, mana, damage):

        if type(health) is not int or health <= 0:
            raise TypeError('Health should be positive integer')
        
        if type(mana) is not int or mana <= 0:
            raise TypeError('Mana should be positive integer')
        
        if type(damage) is not int or damage <= 0:
            raise TypeError('Damage should be positive integer')


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