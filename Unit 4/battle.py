from character import Character, CharacterList

def main ():
    # Loads the character list from the file
    character_choices = CharacterList ("battle_characters.txt")

    # Get the user's choice
    print ("Prepare to battle!\n\nWhich character would you like?")


    character_choices.print_list()
    iMax = character_choices.get_number_of_characters()
    choice = int(input())
    while (choice < 0 or choice >=iMax):
        choice = int(input ("Please choose between 0 and " + str (iMax) + "."))

    # Get the character for the user and the computer.
    player = character_choices.get_and_remove_character(choice)
    computer = character_choices.get_random_character()

    # Preparation for the battle
    print ("You have picked a " + player.name)
    print ("The computer picked " + computer.name)
    print ("Let's battle!\n")

    # Battle Loop
    rnd = 1
    while (player.hit_points > 0 and computer.hit_points > 0):
        print ("Round: " + str (rnd))
        player.attack (computer);
        computer.attack (player)

        if (player.hit_points <= 0 or computer.hit_points <= 0):
            if (computer.hit_points <= 0):
                computer.die()

            if (player.hit_points <= 0):
                player.die()

        else:
            print (player.name + ": " + str(player.hit_points) + " hit points remaining.")
            print (computer.name + ": " + str(computer.hit_points) + " hit points remaining.")
            raw_input("\nPress enter to continue battle.\n")
            rnd += 1

    # Print exit message
    if (player.hit_points <= 0) and (computer.hit_points <= 0):
        print ("\nThe battle ended in a tie.")
    elif (player.hit_points <= 0):
        print ("\nYou have lost.")
    else:
        print ("\nYou have won!")

main()