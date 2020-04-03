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

        self.weapon = None
        self.spell = None

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
    def __init__(self, health, mana, damage):
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
    HERO = 'H'
    ENEMY = 'E'
    START = 'S'
    EXIT = 'G'
    OBSTACLE = '#'
    TREASURE = 'T'
    WALKABLE_PATH = '.'
    POSSIBLE_DIRECTIONS = ['up', 'down', 'left', 'right']

    def __init__(self, level1):
        with open(level1) as f:
            line = f.read().split('\n')
            level_map = [list(l) for l in line if l.strip() != '']

        self.level_map = level_map

    def __str__(self):
        level = ''
        for line in self.level_map:
            for l in line:
                level += str(l)
            level += '\n'

        level = level[:-1]

        return level

    def print_map(self):
        # print(self.__str__())
        return self.__str__()

    def spawn(self, hero):
        pass

    def move_hero(self, direction):
        x, y = self.find_hero()

        if direction == 'up':
            if y == 0 or self.level_map[y - 1] == '#':
                return False
            else:
                self.level_map[x][y - 1] = 'H'
        elif direction == 'left':
            if x == 0 or self.level_map[x - 1] == '#':
                return False
            else:
                self.level_map[x - 1][y] = 'H'
        elif direction == 'right':
            if x == len(self.level_map[0]) - 1 or self.level_map[x][y + 1] == '#':
                return False
            else:
                self.level_map[x + 1][y] = 'H'
        else:
            if y == len(self.level_map) - 1 or self.level_map[x + 1][y] == '#':
                return False
            else:
                self.level_map[x][y + 1] = 'H'

        self.level_map[x][y] = '.'
        return True

    def find_hero(self):
        level_map = self.level_map

        rows = len(level_map)
        for row in range(rows):
            if 'H' in level_map[row]:
                for col in range(len(level_map[row])):
                    if level_map[row][col] == 'H':
                        return (row, col)
        return None

    def pick_treasure():
        pass

    def hero_attack(by):
        pass


if __name__ == '__main__':
    main()
