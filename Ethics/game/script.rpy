### Building/Compiling Game ###
# 1. Check Script using <Check Script (Lint)> in Renpy Launcher to check syntax
# 2. Build using <Build Distributions> in Renpy launcher

### Character Declaration ###
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Me",        color = "#c8ffc8")
define c = Character("Confucius", color = "#c8ffc8")
define k = Character("Kant",      color = "#c8ffc8")
define a = Character("Aristotle", color = "#c8ffc8")
define s = Character("Sphinx",    color = "#c8ffc8")

### Pythonic Things ###
# Use a '$' in front of lines to interpret them as Python
$ book = False

label start:        # Start
    # Introduction:
     
    # You're on a journey to obtain the philosophers stone. 
    # In order to do this you must learn three ethical frameworks and prove you are worthy of the stone. 
    # You time travel to each time period to train under each philosopher and learn their ethical framework. 
    # After obtaining their approval, you receive a special item from each philosopher 
    # that you must use to unlock the gate/door to the philosopher’s stone.

    jump cave

label cave:         # Ancient Cave
label china:        # Ancient China -> Confucius
label cave2:        # Return to Cave
label russia:       # Russia -> Kant
label cave3:        # Return to Cave
label greece:       # Ancient Greece -> Aristotle
label cave4:        # Return to Cave
label final_boss:   # Sphinx/Final Boss Thing
    return

### EXAMPLES FOR REFERENCE ###
label examples:
    ### Showing Images ###
    # scene <image> : Show background image of <image>.png or <image>.jpg
    # show <image> : Show character sprite of <image>.png or <image>.jpg
    # hide <image> : Hides character sprite
    # show <image> at right : Shows image at right of screen (or left, or center)
    scene room
    show eileen_happy
    hide eileen_happy

    ### Playing Music ###
    # play music <music.mp3>  : Plays music file (will loop)
    # stop music              : Stops music
    # play sound <effect.ogg> : Plays sound effect (will not loop)
    play music elevator_music.mp3

    ### Transitions ###
    # with <transition> : Transitions all current images on the screen
    # - dissolve
    # - fade
    # - None (instant showing of image)
    show eileen_sad
    with dissolve

    ### Jumps and Labels ###
    # jump <label> : Jumps to label

    ### Dialogue ###
    # e "dialogue" : Show dialogue in game, said by <e> character
    # menu         : Show a menu with decisions
    e "You've created a new Ren'Py game."
    menu:
        "What is your favorite color?"

        "Red":
            jump red

        "Green":
            jump green
    
    jump second_label

label second_label:
    $ book = True
    if book:
        e "Woohoo you have a book"
    else:
        e "woohoo you have no book"

    # This ends the game.
    return
