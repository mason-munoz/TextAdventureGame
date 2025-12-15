import random
from entities.player import Player
from entities.enemy import Enemy, Boss
from entities.treasure import Treasure
from entities.merchant import Merchant
from .world import world_map
from entities import room

def main():
    print("\n---- Welcome to the dungeon of object oriented programming! ----\n")
    print("!    Note: Please ensure terminal window is large enough    !\n")
    player_name = input("What is your name: ").title().strip()
    print(f'\n   -- Welcome {player_name}! --')
    

    player = Player(player_name)
    merchant = Merchant()
    boss = Boss()


    while True:
        option_string = "\nWhat would you like to do?\n - Explore (e)\n - Check inventory (i)\n"
        
        if "Map" in player.inventory:
            option_string = option_string + " - View map (m)\n"
        if "Health Potion" in player.inventory and player.health < player.max_health:
            option_string = option_string + " - Drink health potion (h)\n"
        if player.current_room.name == "Merchant Room":
            option_string = option_string + " - Talk to merchant (t)\n"
        elif player.current_room.name == "Boss Room" and "Torch" in player.inventory and boss.alive == True:
            option_string = option_string + " - Raise torch (t)\n"
        elif player.current_room.name == "Exit Room":
            option_string = option_string + " - Open the door (o)\n" 
        
        decision = input(option_string).lower().strip()

        if (decision == "explore") or (decision == "e"):
            options = player.explore()
            direction = input(f'\nWhich way would you like to go:\n{options}').upper().strip()

            if "N" in options:
                if direction == "N":
                    player.current_room = player.current_room.directions["N"]
            if "E" in options:
                if direction == "E":
                    player.current_room = player.current_room.directions["E"]
            if "S" in options:
                if direction == "S":
                    player.current_room = player.current_room.directions["S"]
            if "W" in options:
                if direction == "W":
                    player.current_room = player.current_room.directions["W"]


            if player.current_room.enemy == True:
                enemy = Enemy()
                enemy.battle(player)
                player.current_room.enemy = False
                player.current_room.nothing = True
                if player.enemy_counter == 0:
                    room.enemy_reset(player)
                #"Enemy remains are splattered across the dungeon walls"

            elif player.current_room.treasure == True:
                treasure = Treasure()
                print("\n! A glowing chest sits in the middle of the room !")
                treasure_decision = input("\nWould you like to open it? (Y/N)").lower().strip()
                if treasure_decision == "yes" or treasure_decision == "y":
                    treasure.open_treasure(player)
                    player.current_room.treasure = False
                    player.current_room.nothing = True
                else:
                    print("\n* You decide to ignore the chest (you can always come back for it later) *")
                #"The empty chest sits in the middle of the room"

            elif player.current_room.name == "Merchant Room":
                print("\n! You have encountered a goblin merchant !\n")
                purchase_decision = input("Would you like to talk to him? (Y/N) ").lower().strip()
                if purchase_decision == "y":
                    merchant.display_items(player)
            
            elif player.current_room.name == "Boss Room":
                print("\n! The room is pitch black... !")
            
            elif player.current_room.name == "Exit Room":
                print("\n! A heavy metal door sits at the end of the room !\n")

            elif player.current_room.nothing == True:
                print("\nThe room is empty")

        
        elif (decision == "check inventory") or (decision == "inventory") or (decision == "i"):
            player.check_inventory()
        
        elif (decision == "view map" or decision == "map" or decision == "m") and ("Map" in player.inventory):
            world_map(player)
        
        elif (decision == "drink" or decision == "drink health potion" or decision == "h") and "Health Potion" in player.inventory:
            confirmation = input(f'Are you sure you want to heal yourself? You have {player.health}/{player.max_health} health. (Y/N) ').lower().strip()
            if confirmation == "y":
                player.heal()
                player.inventory.remove("Health Potion")
            else:
                print("\nYou put the potion away")
        
        elif ((decision == "raise torch") or (decision == "torch") or (decision == "t")) and (player.current_room.name == "Boss Room") and ("Torch" in player.inventory) and boss.alive == True:
            print("\n* You raise your torch and illuminate the room *")
            boss.battle(player)
        
        elif ((decision == "open door") or (decision == "open") or (decision == "o")) and (player.current_room.name == "Exit Room"):
            print("\n! The door is locked !")
            
            if "Key" in player.inventory:
                door_decision = input("\nUnlock the door with your key? (Y/N)").lower().strip()
                if door_decision == "y" or door_decision == "yes":
                    print("\n* You unlock the door and rays of sunlight shine down upon an ascending staircase... *")
                    player.victory()
                else:
                    continue
            else:
                print("\nIt seems the lock on the door is awaiting a key...")

        elif ((decision == "talk to merchant") or (decision == "talk") or (decision == "t")) and (player.current_room.name == "Merchant Room"):
            merchant.display_items(player)

        else:
            print("\n-- Please select a valid choice -- ")


if __name__ == "__main__":
    main()

