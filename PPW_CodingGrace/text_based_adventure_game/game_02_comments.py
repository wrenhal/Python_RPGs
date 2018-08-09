def main():
    ## We are going to use raw_input so we can have some interaction with player of game
    ## The " > " is just there for decorations, try using other characters.

    ## 1 - Getting your name
    print(raw_input("What's your name? > "))
    ## Now run it, after you type your name, it prints it on the next line.

    ## 1.2 - Refined
    ##
    ## Comment out line 6 by putting # where the code the line starts
    ## Uncomment lines 17 and 23

    ## player_name is a variable, it is created to store objects like strings, numbers
    ## Remember to give variables memorable names or else when you review your code
    ## you don't know what it is used for.
    #player_name =  raw_input("What's your name? >")

    ## This is called string formatting. The {} tells Python that there is something to
    ## be substituted.
    ## The string (in between quotes) calls a built-in function called format.
    ## The number of {} will determine the number of items in between format()
    #print("Your name is {}".format(player_name))

    ## Now uncomment line 28
    ##
    ## Some neat tricks with string manipulations:-
    ## This turns your string all to uppercase
    #print("Your name is {}".format(player_name.upper()))

    ## Open your Python interpreter, try the following
    ## Remember, in terminal, when you type Python and hit return, you should see >>>
    ## >>> player_name = "bob"
    ## >>> print("Your name is {}".format(player_name.upper()))
    ##
    ## Try other string built-in functions.
    ## Find it in Python docs by
    ## 1) https://www.python.org/
    ## 2) Click on Docs
    ## 3) Click on "Library Reference"
    ## 4) Look for "Text Sequence Type - str" and read up the various functions (or methods)
    ##    and experiment in your Python interpretor.
    ##
    ## Don't be afraid to your your Python interpreter, we use it all the time to test and try
    ## out everything. Most Python code you right, you should be able to test in the interpreter.

if __name__ == '__main__':
    main()