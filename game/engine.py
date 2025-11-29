from entities.player import Player
from entities.enemy import Enemy
from entities.room import Treasure

def main():
    print("\n---- Welcome to the dungeon of object oriented programming! ----\n")
    player_name = input("What is your name: ").title().strip()
    print(f'\n   -- Welcome {player_name}! --')
    print("! Note: Please ensure terminal window is large enough !")

    player = Player(player_name)


    while True:
        print(player.current_room.name)
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
                #"Enemy remains are splattered across the dungeon walls"

            elif player.current_room.treasure == True:
                treasure = Treasure()
                treasure.open_treasure(player)
                player.current_room.treasure = False
                player.current_room.nothing = True
                #"The empty chest sits in the middle of the room"

            elif player.current_room.nothing == True:
                print("The room is empty")
            
            print(player.current_room.name)
        
        elif (decision == "check inventory") or (decision == "inventory") or (decision == "i"):
            player.check_inventory()

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

            if enemy.health <= 0:
                print(f'You have killed the enemy!\n *You gained 1 gold!*\n')
                player.gold += 1
                print(f'You now have {player.gold} gold!\n')
                break
            
        elif (battle == "block") or (battle == "b"):
            print("\n")
            player.block(enemy)

            if enemy.health <= 0:
                print(f'You have killed the enemy!\n *You gained 1 gold!*\n')
                player.gold += 1
                print(f'You now have {player.gold} gold!\n')
                break
        
        elif (battle == "charge") or (battle == "c"):
            print("\n")
            player.charge(enemy)

            if enemy.health <= 0:
                print(f'You have killed the enemy!\n *You gained 1 gold!*\n')
                player.gold += 1
                print(f'You now have {player.gold} gold!\n')
                break

if __name__ == "__main__":
    main()

