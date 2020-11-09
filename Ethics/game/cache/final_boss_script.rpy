# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Cthulhu III")
default item_completion = True
default question_number = 1
default has_done_1 = 0
default has_done_2 = 0
default has_done_3 = 0
default num_wrong = 0
# The game starts here.g g

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene corrupted_background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show thresh
    play music "audio/battle_music.mp3" fadein 1.0 fadeout 1.0
    # These display lines of dialogue.

    m "Who goes there?"

    m "I am Cthulhu III. I guard the Philosopher' Stone, which can only be obtained by solving my riddles."
    m "Huh? You say that's ripped from Harry Potter? Well, it wasn't destroyed it was *ahem* given to me through some gratuitous plot holes."
    m "Anyway, no one may attempt to achieve this prize unless they have obtained The Scrolls of Nicomachean Ethics, The Analects, and THING 3."
    m "Do you have all three?"

    menu:
        "Yes":
            jump stuff_checker
        "No":
            jump come_back
label come_back:
    m "Very well. Come back when you have all three."
    jump endgame
label stuff_checker:
    if item_completion:
        m "Hmm, looks like you are braver than I thought. I am bound by oath to challenge you with riddles.
        (because I can't think of anything better to do with my time)."
        jump rule_explanation
    else:
        m "Wretched human! Did you think you could decieve me? I will crush your mortal body and devour your soul!"
        jump liar_death
label liar_death:
    stop music fadeout 1.0
    scene youdied
    play sound "audio/youdied.mp3"
    "The monster ate your soul and you died. Don't cheat the system nitwit."
    "Would you like to try again?"
    menu:
        "Yes":
            $num_wrong = 0
            $question_number = 1
            jump start
        "No":
            jump endgame
label rule_explanation:
    m "I will ask you a series of questions. and you must respond. If you get more than three wrong, then, like a stereotypical monster, I will eat your soul."
    menu:
        "Are you kidding me?!?":
            m "No, unfortunately for you. Let us begin."
            jump question_directory
        "Wow that's so cheesy":
            m "What else do you expect? its a visual novel. I don't make the rules."
            jump question_directory
        "OK":
            m "My, my! You're very calm considering your soul's at stake. Let us start."
            jump question_directory
label question_directory:
    if num_wrong == 3:
        jump wrongdeath
    elif num_wrong == 2 and has_done_2 == 0:
        $has_done_2 = 1
        m "Another one wrong! I can almost taste your soul!"
    elif num_wrong == 1 and has_done_1 == 0:
        $has_done_1 = 1
        m "One wrong! I would be worried about your soul if I were you..."
    if question_number == 1:
        jump question_1
    elif question_number == 2:
        jump question_2
    elif question_number == 3:
        jump question_3
    elif question_number == 4:
        jump question_4
    elif question_number == 5:
        jump question_5
    elif question_number == 6:
        jump question_6
    elif question_number == 7:
        jump question_7
    elif question_number == 8:
        jump question_8
    elif question_number == 9:
        jump question_9
    elif question_number == 10:
        jump question_10
    elif question_number == 11:
        jump question_11
    elif question_number == 12:
        jump question_12
    elif question_number == 13:
        jump question_13
    elif question_number == 14:
        jump question_14
    elif question_number == 15:
        jump question_15
    elif question_number == 16:
        jump finale

label question_1:
    m "Hmm I see that you have talked with Aristotle. Let's see if your little brain has retained anything."
    m "What is ethical virtue derived from?"
    $question_number += 1
    menu:
        "Who Cares?!?":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "From God":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Thoughtful Decision-making":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Practical Wisdom":
            play sound "audio/correct.mp3"
            m "Off to a good start...from your perspective."
            jump question_directory
label question_2:
    m "Doing well? Let's see if this question can jog your memory"
    m "According the Aristotle's Athenian Guard Scenario, is every ethical action clear cut?"
    $question_number += 1
    menu:
        "No; often, there are grey areas.":
            play sound "audio/correct.mp3"
            m "Correct. Although if I had my choice, I would kill the guard and the two children bwahaha."
            jump question_directory
        "Yes; everyone can make the right choice.":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "I have no idea. Please just eat my soul":
            play sound "audio/oof.mp3"
            m "As much as I want to, you must wait a little while longer"
            $num_wrong += 1
            jump question_directory
label question_3:
    m "I've been going too easy on you. Here's a little puzzler."
    m "Fill in the blank: It is the deliberative process of an _____, or the intention, that matters."
    $question_number += 1
    menu:
        "Computer":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Action":
            play sound "audio/correct.mp3"
            jump question_directory
        "Thought":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Process":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
label question_4:
    m "Hmm how about this: out of the three emotions below, which is most oftentimes not virtuous?"
    $question_number += 1
    menu:
        "Envy":
            play sound "audio/correct.mp3"
            jump question_directory
        "Anger":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Sadness":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
label question_5:
    m "How about another fill in the blank?"
    m "Those that are overwhelmed by their urges become little more than _____."
    $question_number += 1
    menu:
        "the enlightened":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Harry Potter":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "beasts":
            play sound "audio/correct.mp3"
            jump question_directory
        "angels":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
label question_6:
    m "Well it seems that you are well versed in Aristotle. I wonder how you fare with Confucius's school of teaching."
    m "True or False: You can only achieve Junzi if you are person born of high social status."
    $question_number += 1
    menu:
        "True":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "False":
            play sound "audio/correct.mp3"
            jump question_directory
label question_7:
    m "Hmm that was a simple enough question. Maybe you don't remember this though. Which one of these qualities is NOT part of Junzi?"
    $question_number += 1
    menu:
        "Humanness":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Filial Piety":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Worldly Wealth":
            play sound "audio/correct.mp3"
            jump question_directory
        "Ritual Decorum":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
label question_8:
    m "Let's dive into the three qualities. Which of the following best describes Humanness (Ren)?"
    $question_number += 1
    menu:
        "You should always treat others with respect.":
            play sound "audio/correct.mp3"
            jump question_directory
        "You should always treat your family members with respect.":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "You should sabotage any social relationships you have.":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Be an absolute Chad Alpha.":
            play sound "audio/oof.mp3"
            m "Edgy, but no."
            $num_wrong += 1
            jump question_directory
label question_9:
    m "What about Filial Piety?"
    $question_number += 1
    menu:
        "One should be loyal to one's family, even if it breaks the law.":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            m "A tricky answer. One should show loyalty to all."
            jump question_directory
        "Loyalty should only be reserved for those who reciprocate that same loyalty.":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Curbstomp your enemies; they only stand in the way for your personal gain.":
            play sound "audio/oof.mp3"
            m "I like the way you think; after all, a soul tastes delicious, friend or foe. But, that is regrettably the incorrect answer."
            $num_wrong += 1
            jump question_directory
        "You should show loyalty to everyone around you.":
            play sound "audio/correct.mp3"
            jump question_directory
label question_10:
    m "I see that you are indeed an attentive student of Confucious."
    m "I myself don't care for his philosphies, although he does make some mean udon noodles when he invites me over for dinner."
    m "To cover the last value, fill in the blank: ___________ is the basis for a good social order."
    $question_number += 1
    menu:
        "Filial Piety":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Bob Ross":
            play sound "audio/oof.mp3"
            m "I wish that were the case. I really do."
            $num_wrong += 1
            jump question_directory
        "Ritual Decorum":
            play sound "audio/correct.mp3"
            jump question_directory
        "Power":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
label question_11:
    m "Well, we have reached our final school of philosophy. I must commend you for getting this far."
    m "Although my hunger tells me not to..."
    m "Anyways, according to the Deontology..."
    $question_number += 1
    jump question_directory
label question_12:
    $question_number += 1
    jump question_directory
label question_13:
    $question_number += 1
    jump question_directory
label question_14:
    $question_number += 1
    jump question_directory
label question_15:
    $question_number += 1
    jump question_directory
label wrongdeath:
    m "Bwahaha you've gotten too many wrong. Time to die!"
    scene youdied
    with Dissolve(0.5)
    stop music fadeout 1.0
    play sound "audio/youdied.mp3"
    "The monster ate your soul and you died. Try studying a little more."
    "Try again?"
    menu:
        "Yes":
            $num_wrong = 0
            $question_number = 1
            jump start
        "No":
            jump endgame
label finale:
    m "What?!? You completed my riddles?!? Impossible!!! No one has ever done this before!"
    m "What is happening to me? Why am I fading? Noooooooooooo......."
    scene peacerestored
    with Dissolve(0.5)
    stop music fadeout 1.0
    play sound "audio/link_victory_theme.mp3"
    queue music "audio/rito_village_but_really_its_windwaker.mp3"
    show phil_stone
    "The monster disappears into a green mist. The Philosopher's Stone sits where it once stood."
    "Congratulations. You won the game!"
    "Would you like to play again?"
    menu:
        "Yes":
            $num_wrong = 0
            $question_number = 1
            jump start
        "No":
            jump endgame
#label credits:
#   If we have time (or the inclination) to make credits, I could def make them
#    $ credits_speed = 25
#    show credits_image at Move((0.5, 1.0), (0.5, -1.0), credits_speed,
#                  xanchor=0.5, yanchor=0)
#    with Pause(credits_speed+5)
label endgame:
    return
