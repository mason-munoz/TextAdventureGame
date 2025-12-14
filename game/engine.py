from entities.player import Player
from entities.enemy import Enemy
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


    while True:
        print(player.current_room.name)
        if player.map == True:
            if player.current_room.name == "Merchant Room":
                decision = input("\nWhat would you like to do?\n - Explore (e)\n - Check inventory (i)\n - View map(m)\n - Talk to merchant(t)\n").lower().strip()
            else:
                decision = input("\nWhat would you like to do?\n - Explore (e)\n - Check inventory (i)\n - View map(m)\n").lower().strip()
        elif player.current_room.name == "Merchant Room":
            decision = input("\nWhat would you like to do?\n - Explore (e)\n - Check inventory (i)\n - Talk to merchant(t)\n").lower().strip()
        else:
            decision = input("\nWhat would you like to do?\n - Explore (e)\n - Check inventory (i)\n ").lower().strip()
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
                battle(player)
                player.current_room.enemy = False
                player.current_room.nothing = True
                if player.enemy_counter == 0:
                    room.enemy_reset(player)
                #"Enemy remains are splattered across the dungeon walls"

            elif player.current_room.treasure == True:
                treasure = Treasure()
                print("\n* A glowing chest sits in the middle of the room *")
                treasure_decision = input("\nWould you like to open it? (Y/N)").lower().strip()
                if treasure_decision == "yes" or treasure_decision == "y":
                    treasure.open_treasure(player)
                    player.current_room.treasure = False
                    player.current_room.nothing = True
                else:
                    print("\n* You decide to ignore the chest (you can always come back for it later) *")
                #"The empty chest sits in the middle of the room"

            elif player.current_room.name == "Merchant Room":
                print("\nYou have encountered a goblin merchant")
                purchase_decision = input("Would you like to talk to him? (Y/N) ").lower().strip()
                if purchase_decision == "y":
                    merchant.display_items(player)

            elif player.current_room.nothing == True:
                print("The room is empty")
            
            print(player.current_room.name)
        
        elif (decision == "check inventory") or (decision == "inventory") or (decision == "i"):
            player.check_inventory()
        
        elif (decision == "view map" or decision == "m") and (player.map == True):
            world_map(player)

        elif ((decision == "talk to merchant") or (decision == "talk") or (decision == "t")) and (player.current_room.name == "Merchant Room"):
            merchant.display_items(player)

        else:
            print("\n-- Please select a valid choice -- ")

def battle(player):
    enemy = Enemy()
    print("\nYou have encountered a wild enemy!")
    while True:
        battle = input(f'You have {player.health} health! What would you like to do?\n - Strike (s)\n - Block (b)\n - Charge (c)\n').lower().strip()

        if (battle == "strike") or (battle == "s"):
            print("\n")
            player.strike(enemy)

            
        elif (battle == "block") or (battle == "b"):
            print("\n")
            player.block(enemy)

        
        elif (battle == "charge") or (battle == "c"):
            print("\n")
            player.charge(enemy)
        
        if enemy.health <= 0:
                print(f'You have killed the enemy!\n *You gained 1 gold!*\n')
                player.enemy_counter -= 1
                player.gold += 1
                print(f'You now have {player.gold} gold!\n')
                break

if __name__ == "__main__":
    main()

