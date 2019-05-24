import random

class item:
    def __init__(self):
        self._attack = 0
        self._image = None
        self._health = 0
        self._defence = 0
        self._speed = 0
        self._dexterity = 0
        self._strength = 0
        self._constitution = 0
        self._intelligence = 0
        self._wisdom = 0
        self._charisma = 0

    def equip(self, target):
        target._health += self._health
        target._defence += self._defence
        target._speed += self._speed
        target._dexterity += self._dexterity
        target._strength += self._strength
        target._constitution += self._constitution
        target._intelligence += self._intelligence
        target._wisdom += self._wisdom
        target._charisma += self._charisma

    def unequip(self, target):
        target._health -= self._health
        target._defence -= self._defence
        target._speed -= self._speed
        target._dexterity -= self._dexterity
        target._strength -= self._strength
        target._constitution -= self._constitution
        target._intelligence -= self._intelligence
        target._wisdom -= self._wisdom
        target._charisma -= self._charisma


class Shortsword(item):
    def __init__(self, name):
        self._attack = 0
        self._image = '/uti/Shortsword.jpg'
        self._health = 0
        self._defence = 0
        self._dexterity = 0
        self._constitution = 0
        self._intelligence = 0
        self._wisdom = 0
        self._charisma = 0
        self._strength = 5
        self._name = name
        self._speed = 10
    
    def light_atack(self, hero, target):
        damage = hero._strength // 10 
        target._health -= random.randint(0, 4) + damage
        
    
class Normal_unit:

    _image = None
    _health = None
    _defence = None
    _name = None
    _exp = None
    _race = None
    _speed = None
    _dexterity = None
    _strength = None
    _constitution = None
    _intelligence = None
    _wisdom = None
    _charisma = None

    def attack(self, target):
        target._health -= self._attack
        print(target.name, target._health, '/', target._healthfull, 'HP')

    def is_alive(self):
        return self._health > 0

class Bandit(Normal_unit):
    def __init__(self):
        self._health = 11
        self._defence = 12
        self._name = 'Bandit'
        self._exp = 25
        self._race = 'Humanoid'
        self._speed = 30
        self._dexterity = 12
        self._strength = 11
        self._constitution = 12
        self._intelligence = 10
        self._wisdom = 10
        self._charisma = 10

    def scimilar(self, target): #Melee weapon attack
        target._slashing = True
        target._health -= 1 + random.randint(0, 6)

    def light_crossbow(self, target): #Ranged weapon attack
        target._piercing = True
        target._health -= 1 + random.randint(0, 8)


class Blood_hawk(Normal_unit):
    def __init__(self):
        self._health = 7
        self._defence = 12
        self._name = 'Blood Hawk'
        self._exp = 25
        self._race = 'Humanoid'
        self._speed = 10
        self._dexterity = 14
        self._strength = 6
        self._constitution = 10
        self._intelligence = 3
        self._wisdom = 14
        self._charisma = 5

    def beak(self, target):
        target._health -= 2 + random.randint(0, 4)


class Boggle(Normal_unit):
    def __init__(self):
        self._health = 18
        self._defence = 14
        self._name = 'Boggle'
        self._exp = 25
        self._race = 'Fey'
        self._speed = 30
        self._dexterity = 18
        self._strength = 8
        self._constitution = 13
        self._intelligence = 6
        self._wisdom = 12
        self._charisma = 7

    def pummel(self, target):
        target._health -= random.randint(0, 6) - 2


class Camel(Normal_unit):
    pass

class Cultist(Normal_unit):
    pass

class Flumph(Normal_unit):
    pass

class Giant_rat(Normal_unit):
    pass

class Giant_crab(Normal_unit):
    pass

class Kobold(Normal_unit):
    pass

class Manes(Normal_unit):
    pass

class Merfolk(Normal_unit):
    pass



class Elite_unit:
    def __init(self):
        self._health = None
        self._attack = None

    def attack(self, target):
        target._health -= self._attack
        print(target.name, target._health, '/', target._healthfull, 'HP')

    def is_alive(self):
        return self._health > 0


class Boss:
    def __init__(self):

        self._health = None
        self._attack = None

    def attack(self, target):
        target._health -= self._attack
        print(target.name, target._health, '/', target._healthfull, 'HP')

    def is_alive(self):
        return self._health > 0


class Hero:
    def __init__(self):

        self._image = None
        self._health = None
        self._defence = None
        self._name = None
        self._exp = None
        self._race = None
        self._speed = None
        self._dexterity = None
        self._strength = None
        self._constitution = None
        self._intelligence = None
        self._wisdom = None
        self._charisma = None
        self._class = None
        self._lvl = None

    def attack(self, target):
        target._health -= self._attack


    def is_alive(self):
        return self._health > 0

    def lvl_up(self):
        if self.exp > 300 + self.lvl * 300:
            self.lvl += 1

class Traveler(Hero):
    def __init__(self, health, defence, name, exp, speed, dex, stren, con, intel, wis, cha, lvl):
        self._health = health
        self._defence = defence
        self._name = name
        self._exp = exp
        self._race = 'Humanoid'
        self._speed = speed
        self._dexterity = dex
        self._strength = stren
        self._constitution = con
        self._intelligence = intel
        self._wisdom = wis
        self._charisma = cha
        self._lvl = lvl

enemy_types = [Bandit, Blood_hawk, Boggle]
