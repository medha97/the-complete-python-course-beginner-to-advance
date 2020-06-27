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
curaga = spell("Curaga", 50, 6000, "white")

#create some items
potion = item("Potion", "potion", "Heals 50 HP", 50)
hipotion = item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = item("Elixer", "elixer", "Fully store HP/MP of one party member", 9999)
hielixer = item("MegaElixer", "elixer", "Fully store party's HP/MP", 9999)

grenade = item("Grenade", "attack", "Deals 500 damage", 500)

player_spell = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spell = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity":15}, {"item": hipotion, "quantity":5},
                {"item": superpotion, "quantity":5}, {"item": elixer, "quantity":5},
                {"item": hielixer, "quantity":2}, {"item": grenade, "quantity":2}]

player1 = Person("Valos:", 3260, 132, 300, 34, player_spell, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_spell, player_items)
player3 = Person("Robot:",3089, 174, 288, 34, player_spell, player_items)

enemy1 = Person("Imp  ",1250, 130, 560, 325, enemy_spell, [])
enemy2 = Person("magus",11200, 221, 525, 25, enemy_spell, [])
enemy3 = Person("Imp  ",1250, 130, 560, 325, enemy_spell, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

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
        for enemy in enemies:
            enemy.get_enemy_stats()

        player.choose_action()
        choice = input("Choose Action")
        print("You choose", choice)
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("you attacked"+enemies[enemy].name+"for", dmg, "points of damage. Enemy HP", str(enemies[enemy].get_hp()))

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + "has died.")
                del enemies[enemy]

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
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print("\n" + spell.name + " deals", str(magic_dmg), "points of damage to"+enemies[enemy].name )

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + "has died.")
                    del enemies[enemy]

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
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print("\n" + item.name + "deals", str(item.prop), "points of damage")

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + "has died.")
                    del enemies[enemy]

        #check if battle is over
        defeated_enemies = 0
        defeated_players = 0

        for player in players:
            if player.get_hp() == 0:
                defeated_players += 1

        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeated_enemies += 1

        #check if player has won
        if defeated_enemies == 2:
            print("You Win!")
            running = False

        #check if enemy is won
        if defeated_players == 2:
            print( "Your enemy has defeated you!")
            running = False

        # enemy attack phase
        for enemy in enemies:
            enemy_choice = random.randrange(0,3)

            if enemy_choice == 0:
                #choose attack
                target = random.randrange(0,3)
                enemy_dmg = enemies[0].generate_damage()

                players[target].take_damage(enemy_dmg)
                print(enemy.name.replace(" ","")+"attacked "+players[target].name.replace(" ","")+"for", enemy_dmg, "Player HP", player.get_hp())

            elif enemy_choice == 1:
                spell, magic_dmg = enemy.choose_enemy_spell()
                print("Enemy choose", spell, "damage is", magic_dmg)

                if spell.type == "white":
                    enemy.heal(magic_dmg)
                    print(  "\n" + spell.name + "heals"+ spell.name +"for", str(magic_dmg), "HP" )

                elif spell.type == "black":
                    target = random.randrange(0,3)
                    players[target].take_damage(magic_dmg)

                    print("\n" + enemy.name.replace(" ", "")+"'s"+ spell.name + " deals"+ str(magic_dmg)+"points of damage to"+players[target].name)

                    if players[target].get_hp() == 0:
                        print(players[target].name + "has died.")
                        del players[target]
