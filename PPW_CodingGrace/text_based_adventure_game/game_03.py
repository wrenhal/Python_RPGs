def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = raw_input("Do you pick the red door or blue door? > ")

    # IF STATEMENTS
    # door_picked variable contains whatever the player types in.
    if door_picked == "red":
        print("You picked the red door")
    elif door_picked == "blue":
        print("You picked the blue door")
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

    # Run the program a few times testing out the different answers.

def main():
    player_name =  raw_input("What's your name? >")
    print("Your name is {}".format(player_name.upper()))

    # Calls another function, declare it above.
    start_adventure()

if __name__ == '__main__':
    main()