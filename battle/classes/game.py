import random
from .magic import spell
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i].dmg - 5
        mgh = self.magic[i].dmg + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp


    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\nAction")
        for item in self.action:
            print("    " + str(i)+".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\nMagic")
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name + "(cost" + ":", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i=1
        print("\nItems")
        print("ITEMS:" )
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, ":", item["item"].description, "(x"+str(item["quantity"])+")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.max_mp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar)<25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar)<10:
            mp_bar += " "

        print("                    _________________________              __________")
        print(self.name+"   "+str(self.hp)+"/"+str(self.max_hp)+" |"+hp_bar+"|"
        +"    "+str(self.mp)+"/"+str(self.max_mp)+" |"+mp_bar+"|")
