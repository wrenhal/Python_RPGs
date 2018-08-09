# Now we have a premise. We are in a room and we have two door to choose from.
# We are still in the blue room. Now we have to deal with the guard
# after taking or leaving the treasure chest.

##### ACTIONS #####
def you_died(why):
    # You expect a reason why the player died. It's a string.
    print("{}. Good job!".format(why))

    # This exits the program entirely.
    exit(0)

### END ACTIONS ###

### CHARACTERS ###
def guard():
    # The guard
    print("You approach the guard, he's still sleeping.")
    print("Suddenly you knocked a wooden cask with a mug on it... CRASSH!")
    print("\nOi, what you doing 'ere?")

    # Initialise boolean, guard_moved, to False (because he's asleep)
    guard_moved = False

    # There are ways to escape a while loop, in this example:
    # - When a player dies, it calls you_died() and it exits() the program.
    # - When a player escapes through the door, you return to the previous function which
    #   called this function.
    while True:
        next_action = raw_input("[run | door] > ").lower()
        if next_action == "run" and guard_moved:
            you_died("Guard was faster than he looks and your world goes dark...")
        elif next_action == "run" and not guard_moved:
            print("Guard jumps up and looks the other way, missing you entirely.")
            guard_moved = True
        elif next_action == "door" and guard_moved:
            print("You just slipped through the door before the guard realised it.")
            print("You are now outside, home free! Huzzah!")
            return
        elif next_action == "door" and not guard_moved:
            you_died("Guard was faster than he looks and your world goes dark...")
        else:
            print("Not sure what you meant there... try again.")
# END CHARACTERS #

##### ROOMS #####
def blue_door_room():
    # So our treasure_chest list contains 4 items.
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the door")

    # Ask player what to do.
    action = raw_input("What do you do? > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!")

        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = raw_input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)

            # So much treasure, what to do? Take it or leave it.
            print("What do you want to do?")
            print("Take all {} treasure, press '1'".format(len(treasure_chest)))
            print("Leave it, press '2'")

            treasure_choice = raw_input("> ")
            if treasure_choice == "1":
                print("\tWoohoo! Bounty and a shiney new sword. /drops your crappy sword in the empty treasure chest.")
                print("\tYou just received [{}]".format(", ".join(treasure_chest)))
            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")

        # Picked up treasure or left it, you will now encounter the guard.
        guard()
    elif action.lower() in ["guard", "right"]:
        print("The guard is more interesting, let's go that way!")
        guard()
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")
        guard()


def red_door_room():
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = raw_input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        you_died("It eats you. Well, that was tasty!")
### END ROOMS ###

def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = raw_input("Do you pick the red door or blue door? > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

def main():
    player_name =  raw_input("What's your name? >")
    print("Your name is {}".format(player_name.upper()))

    start_adventure()

    print("\nThe end\n")
    print("Thanks for playing, {}".format(player_name.upper()))


if __name__ == '__main__':
    main()