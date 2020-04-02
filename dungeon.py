from utls import Mixin, Weapon, Spell

class Hero(Mixin):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return(f'{self.name} the {self.title }')

class Enemy(Mixin):
	
    def __init__(self,health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage


if __name__ == '__main__':
    main()