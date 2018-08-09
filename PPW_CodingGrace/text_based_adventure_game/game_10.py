# Let's clean it up (or refactor), and create a function to ask for your name and return it.
# This will keep main() as clean as possible.
# New code starts at line 153
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

### CHARACTERS ###
def guard():
    # The guard
    print("You approach the guard, he's still sleeping.")
    print("Suddenly you knocked a wooden cask with a mug on it... CRASSH!")
    print("\nOi, what you doing 'ere?")

    # Guard is not moving initially
    guard_moved = False

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

    elif action.lower() in ["guard", "right"]:
        print("The guard is more interesting, let's go that way!")
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
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")
### END ROOMS ###

def get_player_name():
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    name = raw_input("What's your name? > ")

    # This is just an alternative name that the game wants to call the player
    alt_name = "Rainbow Unicorn"
    answer = raw_input("Your name is {}, is that correct? [Y|N] > ".format(alt_name.upper()))
    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print("You are fun, {}! Let's begin our adventure!".format(name.upper()))
    elif answer.lower() in ["n", "no"]:
        print("Ok, picky. {} it is. Let's get started on our adventure.".format(name.upper()))
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(alt_name.upper()))
        name = alt_name

    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in 
    # get_player_name() function. 
    # This is why indentation is important, variables declared in this block only exists in that block
    return name

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
    # Calls get_player_name and returns the player name
    player_name =  get_player_name()

    ####################################################################
    # ACTIVITIES
    # 
    # Read some of the best practices when writing Python code
    #   http://legacy.python.org/dev/peps/pep-0008/
    # Main thing is if you are using tabs, make sure it's 4-spaces,
    # most editors will convert it (check preferences/settings).
    #
    # Modify the code
    # - add taunting the guard or talking
    # - sword fight with the guard, and keep track of health points (HP)
    # - puzzles like 1+2 during an encounter
    # - modifiy blue_door_room()'s if statement
    #   so it takes into account player typing "right" or "guard"
    #   Hint: Add another elif before the else statement
    #
    # So many if statements, this can be made simpler and easier to 
    # maintain by using Finite State Machine (FSM)
    # You can find info about it, but it will mainly be touching 
    # object-orient programming, which is another lesson for another day.
    #
    #####################################################################

    start_adventure()
    
    print("\nThe end\n")
    print("Thanks for playing, {}".format(player_name.upper()))
    

if __name__ == '__main__':
    main()