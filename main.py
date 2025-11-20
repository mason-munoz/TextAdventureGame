from classes import Player, Enemy

print("\n---- Welcome to the dungeon of object oriented programming! ----\n")
player_name = input("What is your name: ").title().strip()
print(f'\n   -- Welcome {player_name}! --')

player = Player(player_name)


while True:
    decision = input("\nWhat would you like to do? \n - Fight (f)\n - Check inventory (i)\n ").lower().strip()
    if (decision == "fight") or (decision == "f"):
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
    
    elif (decision == "check inventory") or (decision == "inventory") or (decision == "i"):
        player.check_inventory()

    else:
        print("\n-- Please select a valid choice -- ")

