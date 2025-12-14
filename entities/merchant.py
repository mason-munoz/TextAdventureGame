import random

class Merchant:
    def __init__(self):
        self.items = {"Torch": 3, "Health Potion": 3, "Map": 1}
        weaponlist = [{"Shiny Dagger": 2}, {"Mace": 3}, {"Broadsword": 4}]
        defenselist = [{"Wooden Shield": 1}, {"Iron Breastplate": 2}, {"Chainmail Armor": 3}]
        self.weapon = random.choice(weaponlist)
        self.defense = random.choice(defenselist)
        self.items.update(self.weapon)
        self.items.update(self.defense)

    def display_items(self, player):
        while True:
            print("\nThe Merchant proudly displays his wares: ")
            item_list = self.items.keys()
            weapon = list(self.weapon.keys())[0]
            defense = list(self.defense.keys())[0]
            for item in item_list:
                print(f'- {item}: {self.items[item]} gold')
                
            
            print(f'\nYou have {player.gold} gold')
            select_item = input('What would you like to purchase? (type "leave" or "l" to leave): ').lower().strip()

            if ("Torch" in self.items) and (select_item == "torch"):
                if (player.gold >= self.items["Torch"]): 
                    confirmation = input(f'Are you sure you would like to purchase the torch? (Y/N): ').lower().strip()
                    if confirmation == "y":
                        print("\n* You successfully purchased the Torch *")
                        player.inventory.append("Torch")
                        player.torch = True
                        player.gold -= self.items["Torch"]
                        player.display_gold()
                        self.items.pop("Torch")
                    else:
                        continue
                else:
                    print("! Error: You dont have enough gold to purchase this item !")

            elif ("Health Potion" in self.items) and ((select_item == "health potion") or (select_item == "potion")):
                if player.gold >= self.items["Health Potion"]:
                    confirmation = input(f'Are you sure you would like to purchase the health potion? (Y/N): ').lower().strip()
                    if confirmation == "y":
                        print("\n* You successfully purchased the Health Potion *")
                        player.inventory.append("Health Potion")
                        player.gold -= self.items["Health Potion"]
                        player.display_gold()
                        self.items.pop("Health Potion")
                    else:
                        continue
                else:
                    print("! Error: You dont have enough gold to purchase this item !")

            elif ("Map" in self.items) and (select_item == "map"):
                if player.gold >= self.items["Map"]:
                    confirmation = input(f'Are you sure you would like to purchase the map? (Y/N): ').lower().strip()
                    if confirmation == "y":
                        print("\n* You successfully purchased the Map *")
                        player.inventory.append("Map")
                        player.map = True
                        player.gold -= self.items["Map"]
                        player.display_gold()
                        self.items.pop("Map")
                    else:
                        continue
                else:
                    print("! Error: You dont have enough gold to purchase this item !")

            elif (weapon in self.items) and (select_item == weapon.lower().strip()):
                if player.gold >= self.items[weapon]:
                    if self.items[weapon] > player.weapon[1]:
                        confirmation = input(f'Are you sure you would like to purchase the {weapon}? (Y/N): ').lower().strip()
                        if confirmation == "y":
                            print(f"\n* You successfully purchased the {weapon} *")
                            new_weapon = tuple(self.weapon.items())[0]
                            player.update_weapon(new_weapon)
                            player.gold -= self.items[weapon]
                            player.display_gold()
                            self.items.pop(weapon)
                        else:
                            continue
                    else:
                        print(f'! Error: This {weapon} is weaker than your current {player.weapon[0]} !')
                else:
                    print("! Error: You dont have enough gold to purchase this item !")
            
            elif (defense in self.items) and (select_item == defense.lower().strip()):
                if player.gold >= self.items[defense]:
                    if self.items[defense] > player.armor[1]:
                        confirmation = input(f'Are you sure you would like to purchase the {defense}? (Y/N): ').lower().strip()
                        if confirmation == "y":
                            print(f"\n* You successfully purchased the {defense} *")
                            new_armor = tuple(self.defense.items())[0]
                            player.update_armor(new_armor)
                            player.gold -= self.items[defense]
                            player.display_gold()
                            self.items.pop(defense)
                        else:
                            continue
                    else:
                        print(f'\n! Error: This {defense} is weaker than your current {player.armor[0]} !')
                else:
                    print("\n! Error: You dont have enough gold to purchase this item !")

            elif (select_item == "leave") or (select_item == "l"):
                print("\n* You wave goodbye to the merchant *")
                break

            else:
                print("\n! Error: Please type out the full name of the item you would like to purchase !")
                
            






