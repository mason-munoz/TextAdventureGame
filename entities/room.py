import random
from . import enemy

class Room():
    def __init__(self, name):
        self.name = name
        self.treasure = False
        self.enemy = False
        self.nothing = False
        self.directions = None

        rng = random.random()
        if rng < 0.3:
            self.treasure = Treasure()
        elif rng < 0.5:
            self.enemy = True
        else:
            self.nothing = True

class BossRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = False
        self.nothing = False

        self.name = "Boss Room"
        self.boss = enemy.Boss
        self.directions = {"E": room4}

class StartRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = False
        self.nothing = True

        self.name = "Start Room"
        self.directions = {"N": room8}
        

class MerchantRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = True
        self.nothing = False

        self.name = "Merchant Room"
        self.directions = {"W": room6}

class ExitRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = False
        self.nothing = False

        self.name = "Exit Room"
        self.directions = {"S": room2}
        self.description = "A heavy wooden door stands before you with light piercing through the cracks."

class Treasure():
    def __init__(self):
        random_num = random.random()
        weaponlist = [("Shiny Dagger", 2), ("Mace", 3), ("Broadsword", 4)]
        defenselist = [("Wooden Shield", 1), ("Iron Breastplate", 2), ("Chainmail Armor", 3)]
        self.gold = random.randint(4,11)
        self.weapon = random.choice(weaponlist)
        if random_num < 0.5:
            self.defensive_item = ("Health Potion", 1)
        else:
            self.defensive_item = random.choice(defenselist)

    def open_treasure(self, player):
        print("\n* A glowing chest sits in the middle of the room *")
        decision = input("\nWould you like to open it?\n - Yes\n - No\n").lower().strip()
        if decision == "yes" or decision == "y":
            print("\n* You open the chest in a burst of light *")
            print(f'\nBefore you lies a {self.weapon[0]}, {self.defensive_item[0]}, and {self.gold} gold!\n')

            if player.damage < self.weapon[1]:
                print(f"* You dropped your {player.weapon[0]} and picked up the {self.weapon[0]} *")
                player.update_weapon(self.weapon)
            elif player.damage >= self.weapon[1]:
                print(f'The {self.weapon[0]} is weaker than your current weapon.')
            
            if (self.defensive_item[1] != "Health Potion") and (player.armor[1] < self.defensive_item[1]):
                if player.armor[0] == "":
                    print(f'* You picked up the {self.defensive_item[0]} *')
                    player.update_armor(self.defensive_item)
                elif player.armor:
                    print(f'* You dropped your {player.armor[0]} and picked up the {self.defensive_item[0]} *')
                    player.update_armor(self.defensive_item)
            
            elif (self.defensive_item[1] != "Health Potion") and (player.armor[1] >= self.defensive_item[1]):
                print(f'The {self.defensive_item[0]} is weaker than your current armor.')
            elif self.defensive_item == "Health Potion":
                print(f'* You picked up the health potion *')
            
            player.gold += self.gold
            print(f"* You picked up the {self.gold} gold *")
        else:
            print("\n* You decide to ignore the chest (you can always come back for it later) *")




room1 = Room("room1")
room2 = Room("room2")
room3 = Room("room3")
room4 = Room("room4")
room5 = Room("room5")
room6 = Room("room6")
room7 = Room("room7")
room8 = Room("room8")
room9 = Room("room9")
start_room = StartRoom()
boss_room = BossRoom()
merchant_room = MerchantRoom()
exit_room = ExitRoom()

room1.directions = {"E":room2, "S":room4}
room2.directions = {"N":exit_room, "E":room3, "S":room5, "W":room1}
room3.directions = {"S":room6, "W":room2}
room4.directions = {"N":room1, "E":room5, "S":room7, "W":boss_room}
room5.directions = {"N":room2, "E":room6, "S":room8, "W":room4}
room6.directions = {"N":room3, "E":merchant_room, "S":room9, "W":room5}
room7.directions = {"N":room4, "E":room8}
room8.directions = {"N":room5, "E":room9, "S":start_room, "W":room7}
room9.directions = {"N":room6, "W":room8}
