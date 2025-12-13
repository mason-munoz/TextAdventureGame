import random

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
            player.inventory.append("Health Potion")
        
        player.gold += self.gold
        print(f"* You picked up the {self.gold} gold *")
        