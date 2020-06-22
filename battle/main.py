from classes.game import Person, bcolors
from classes.magic import spell
from classes.inventory import item

print("\n\n")
print("NAME                HP                                    MP")
print("                    _________________________             __________")
print("Valos:    460/460  |                         |    65/65  |          |")

print("                    _________________________             __________")
print("Valos:    460/460  |                         |    65/65  |          |")

print("                    _________________________             __________")
print("Valos:    460/460  |                         |    65/65  |          |")

print("\n\n")

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

player = Person(460, 65, 60, 34, player_spell, player_items)
enemy = Person(1200, 65, 54, 25, player_spell, player_items)

running = True
i=0

print("AN ENEMY ATTACK")

while running:
    print('==============================')
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
            player.hp = player.max_hp
            player.mp = player.max_mp
            print("\n" + item.name + "fully restores HP/MP")

        elif item["item"].type == "attack":
            enemy.take_damage(item.prop)
            print("\n" + item.name + "deals", str(item.prop), "points of daamge")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg, "Player HP", player.get_hp())

    print("--------------------------------------------")
    print("Enemy HP:",  str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + "\n")

    print("Your HP:",  str(player.get_hp()) + "/" + str(player.get_max_hp()) +"\n")
    print("Your MP:", str(player.get_mp()) + "/" + str(player.get_max_mp()) )
    if enemy.get_hp() == 0:
        print( "you win!")
        running = False
    elif player.get_hp() == 0:
        print( "Your enemy has defeated you!")
        running = False








'''print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print(player.generate_damage())
'''
