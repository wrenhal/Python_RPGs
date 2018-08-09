# Now we have a premise. We are in a room and we have two door to choose from.
# We are still in the blue room. What do we do with the treasure chest?
# New code starts at line 52
#
# Length of a list, excaping characters and more string manipulations
#
# Run this code a few times and see what happens with different choices.
# It's good to test all options and see if that's what you expected.

##### ACTIONS #####
def you_died(why):
    # You expect a reason why the player died. It's a string.
    print("{}. Good job!".format(why))

    # This exits the program entirely.
    exit(0)

### END ACTIONS ###

##### ROOMS #####
def blue_door_room():
    # The variable treasure_chest is an object type called a list
    # A list maybe empty as well.
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

        # Try just leaving 1 and 2 as a number
        # Change to string and see what happens
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

            # INTRODUCING len()
            # Go to the Python interpreter.
            #   >>> treasure_chest = ["diamonds", "gold", "silver", "sword"]
            #   >>> len(treasure_chest)
            # This should give you how many items is in a list.
            #
            #   >>> len("diamonds")
            # This should give you how long the string is.
            print("Take all {} treasure, press '1'".format(len(treasure_chest)))
            print("Leave it, press '2'")

            treasure_choice = raw_input("> ")

            if treasure_choice == "1":
                # ESCAPE CHARACTERS
                # We encountered this when escaping those single or double quotes in the beginning.
                # Go to the Python interpreter.
                #   >>> print("hello")
                #   >>> print("\thello")
                #   >>> print("\nhello")
                #   >>> print("I\nam here,\n\tbut why!\n\nEscaping charaters.")
                #
                # See https://docs.python.org/2.7/reference/lexical_analysis.html#string-literals
                print("\tWoohoo! Bounty and a shiney new sword. /drops your crappy sword in the empty treasure chest.")

                # STRING MANIPULATION
                # Here's a handy way to join items in a list.
                # Go to the Python intrepeter.
                #   >>> treasure_chest = ["diamonds", "gold", "silver", "sword"]
                #   >>> ', '.join(treasure_chest)
                # What happens here is we created a string ', ' (comma with a space), and use the
                # string's in-built function called join() to join up your list items and
                # creates a comma separated string. Really handy, better than writing your own. :-)
                print("\tYou just received [{}]".format(", ".join(treasure_chest)))

            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
                
    elif action.lower() in ["guard", "right"]:
        print("The guard is more interesting, let's go that way!")
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")


def red_door_room():
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = raw_input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
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

if __name__ == '__main__':
    main()