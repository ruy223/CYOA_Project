# Author: The Game Master
# Github: ruy223
# Date: 10/02/2026
# Description: Choose your own adventure game

# Classes and Function
from classes_and_functions import print_wrapped



#Menu
answer = input("Would you like to start the game? (yes/no)")
if answer.lower().strip() == "yes":
    print("Welcome to Malikor's Dungeon!")

    #Game background lore
    answer = input("Would you like to hear the backstory? (yes/no)")
    if answer.lower().strip() == "yes":
        print_wrapped("In the shadowed realms of Eldoria, the ancient sorcerer Malikor has risen from centuries of slumber, transforming an abandoned underground fortress into his personal dungeon. A labyrinth of twisted magic, deadly traps, and monstrous guardians. Malikor, once a revered mage who delved too deep into forbidden necromancy, now seeks to harness the ""Heart of Eternity,"" a crystalline artifact buried deep within the dungeon. If he succeeds, he'll unleash an army of undead to conquer the surface world, plunging Eldoria into eternal darkness. Your quest begins after Malikor's minions raid your village and abduct your sister.")
    elif answer.lower().strip() == "no":
        print("Okay, let's begin!")

        answer = input("You stand at the crumbling stone entrance of Malikor's Dungeon.")
                    
    else:
        print("Invalid input. Start again!")

else: print("Maybe next time!")