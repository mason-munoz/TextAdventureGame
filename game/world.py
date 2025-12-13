def world_map(player):
    if player.current_room.name == "Start Room":
        current_map = ("""    
                    |-----|
                    |  E  |
              |-----|-----|-----|
              |  1  |  2  |  3  |
        |-----|-----|-----|-----|-----|
        |  B  |  4  |  5  |  6  |  M  |
        |-----|-----|-----|-----|-----|
              |  7  |  8  |  9  |
              |-----|-----|-----|
                    | S # |
                    |-----|

        """)
        print("""             -- Key --
            - #: You
            - !: Enemy
            - *: Treasure 
            - S: Start 
            - E: Exit
            - M: Merchant
            - B: Boss
             """)

