from classes.game import Person, bcolors
from classes.magic import spell
from classes.inventory import item
import random


#create black magic
fire = spell("Fire", 10, 100, "black")
thunder = spell("Thunder", 10, 100, "black")
blizzard = spell("Blizzard", 10, 100, "black")
meteor = spell("Meteor", 20, 200, "black")
Quake = spell("Quake", 14, 140, "black")

#create white magic
cure = spell("Cure", 12, 120, "white")
cura = spell("Cura", 10, 200, "white")

#create some items
potion = item("Potion", "potion", "Heals 50 HP", 50)
hipotion = item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = item("Elixer", "elixer", "Fully store HP/MP of one party member", 9999)
hielixer = item("MegaElixer", "elixer", "Fully store party's HP/MP", 9999)

grenade = item("Grenade", "attack", "Deals 500 damage", 500)

player_spell = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity":15}, {"item": hipotion, "quantity":5},
                {"item": superpotion, "quantity":5}, {"item": elixer, "quantity":5},
                {"item": hielixer, "quantity":2}, {"item": grenade, "quantity":2}]

player1 = Person("Valos:", 3260, 132, 514, 34, player_spell, player_items)
player2 = Person("Nick :", 4160, 188, 617, 34, player_spell, player_items)
player3 = Person("Robot:",3089, 174, 615, 34, player_spell, player_items)
enemy = Person("magus",11200, 221, 315, 25, [], [])

players = [player1, player2, player3]



running = True
i=0

print("AN ENEMY ATTACK")

while running:
    for player in players:
        print('==============================')
        print("\n\n")
        print("NAME              HP                                   MP")
        for play in players:
            play.get_stats()

        print("\n")

        enemy.get_enemy_stats()

        player.choose_action()
        choice = input("Choose Action")
        print("You choose", choice)
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("you attacked for", dmg, "points of damage. Enemy HP", enemy.get_hp())

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print( " not enough MP\n")
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(  "\n" + spell.name + "heals for", str(magic_dmg), "HP" )

            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print("\n" + spell.name + " deals", str(magic_dmg), "points of damage" )

        elif index == 2:
            player.choose_item()
            item_choice = int(input("choose item:")) - 1
            if player.items[item_choice]["quantity"] == 0:
                print("None Left")
                continue
            player.items[item_choice]["quantity"] -= 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]
            if item["item"].type == "potion":
                player.heal(item["item"].prop)
                print("\n" + item["item"].name + "heals for", str(item["item"].prop), "HP")

            elif item["item"].type == "elixer":
                if item["item"].name == "MegaElixer":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                print("\n" + item["item"].name + "fully restores HP/MP")

            elif item["item"].type == "attack":
                enemy.take_damage(item.prop)
                print("\n" + item.name + "deals", str(item.prop), "points of daamge")

        enemy_choice = 1
        target = random.randrange(0,3)
        enemy_dmg = enemy.generate_damage()
        players[target].take_damage(enemy_dmg)

        print("Enemy attacked for", enemy_dmg, "Player HP", player.get_hp())

        if enemy.get_hp() == 0:
            print( "you win!")
            running = False
        elif player.get_hp() == 0:
            print( "Your enemy has defeated you!")
            running = False
