### Building/Compiling Game ###
# 1. Check Script using <Check Script (Lint)> in Renpy Launcher to check syntax
# 2. Build using <Build Distributions> in Renpy launcher

### Character Declaration ###
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define M = Character("Me",        color = "#c8ffc8")
define N = Character("Narrator",  color = "#c8ffc8")
define C = Character("Confucius", color = "#c8ffc8")
define K = Character("Kant",      color = "#c8ffc8")
define A = Character("Aristotle", color = "#c8ffc8")
define A_S = Character("Student", color = "#c8ffc8")
define S = Character("Sphinx",    color = "#c8ffc8")

### Pythonic Things ###
# Use a '$' in front of lines to interpret them as Python
$ book = False

label start:        # Start
    stop music fadeout 1.0
    # Introduction:

    # You're on a journey to obtain the philosophers stone.
    # In order to do this you must learn three ethical frameworks and prove you are worthy of the stone.
    # You time travel to each time period to train under each philosopher and learn their ethical framework.
    # After obtaining their approval, you receive a special item from each philosopher
    # that you must use to unlock the gate/door to the philosopher’s stone.

    jump greece

label cave:         # Ancient Cave
label china:        # Ancient China -> Confucius
label cave2:        # Return to Cave
# label russia:        # Russia -> Kant russia.rpy
label cave3:        # Return to Cave
label greece:       # Ancient Greece -> Aristotle
    scene white
    N "Flash!"
    N "Your ears ring and the piercing flash of white light leaves you disoriented…"

    scene plaza
    play music "Audio/A_plaza_ambience.mp3" fadein 1.0 fadeout 1.0
    with dissolve
    N "After a while, you finally begin to see again, in what you assume to be Ancient Greece!"
    N "You seem to be in the middle of a plaza, with many young people in colored robes hurrying around you."
    N "You ask someone passing where you might find Aristotle-"
    M "Hey, do you know where I might find Aristotle?"
    N "You realize too late that you do not speak Ancient Greek, yet the person seems to understand what you are saying."
    A_S "The professor, Aristotle, you mean? He is not teaching right now, but you might find him in his lecture hall taking arguments from other students."
    M "Okay, thank you! Where might this lecture hall be?"
    N "The student looks at you quizzically, yet responds in kind."
    A_S "That would be two buildings down and on your right."
    N "You thank the student and head your way over to the lecture hall."

    stop music fadeout 1.0
    scene lecturehall
    play music "Audio/A_greek_music.mp3" fadein 1.0 fadeout 1.0
    with dissolve
    N "You find your way to the lecture hall, and discover an older man scribbling notes on parchment."
    show aristotle
    with dissolve
    A "Are you here to propose another argument? If so, please make it quick. I have another lecture shortly after this one."
    menu:
        "You look familiar.":
            jump Aristotle_Introduction
        "Are you Aristotle?":
            jump Thatisme

label Aristotle_Introduction:
    A "I am Aristotle, teacher at this academy. Although, if you are not my student, who are you, and what are you here for?"
    jump A_Outsiders

label Thatisme:
    A "That is me. Although, if you are not my student, who are you, and what are you here for?"
    jump A_Outsiders

label A_Outsiders:
    A "Outsiders are not supposed to be allowed on campus."
    menu:
        "I know you from my history textbooks!":
            jump A_HistoryTextbooks
        "I am from the future.":
            jump A_Hmm

label A_HistoryTextbooks:
    A "You mean to say you know me from... history textbooks? As in from the future?"

    menu:
        "Duh. You are like, famous.":
            jump A_Hmm 
        "I need your help.":
            jump A_Hmm


label A_Hmm:
    A "Hmm…"
    A "If you say you are from the future, and you really are, then the burden of proving you are from the future lies with you, not my ability to believe you. I think that much is fair."
    A "Otherwise, you are a crazy person, and you are wasting my time."
    A "Therefore, convince me that you are from the future."
    menu:
        "You will write a work called Nicomachean Ethics, named after your father!":
            jump NicomacheanEthics
        "You will have a child named Nicomachus with Herpyllis!":
            jump Nicomachus

label NicomacheanEthics:
    A "Ah, my Nicomachean Ethics? I have not released that yet, but I have been writing rough drafts concerning the nature of virtue ethics..."
    jump ConvinceAristotle

label Nicomachus:
    N "Aristotle looks caught off-guard."
    A "I did not know anybody knew of my personal affairs… I have tried hard to keep our love a secret, but I suppose there is no hiding it now."
    jump ConvinceAristotle

label ConvinceAristotle:
    A "I am skeptical, but the things you say are things no one else would know about myself. You seem to have no reason to lie."
    A "Alright, time traveler, I will play along. What business might you have travelling back in time to meet me?"
    menu:
        "I have come in search of the philosopher’s stone.":
            jump A_SphinxExplain
        "I need to defeat a monster that will end the world in the future.":
            jump A_SphinxExplain

label A_SphinxExplain:
    M "But in order to do so, I must learn ethics from philosophical thinkers."
    M "In addition, I require a relic from the past that represents your ethical perspective."
    A "Well, I believe the best way to do so is for you to sit in on one of my lectures."
    A "If you are lying about time travelling, after all, perhaps it is good to educate you in the ways of ethics."
    A "You are welcome to the next lecture I hold – it is on my theory of virtue ethics. Feel free to ask questions or challenge my theory as you see fit."
    scene white
    hide aristotle
    with dissolve
    N "You agree to meet at his next lecture, and wander around the campus for a while before returning to the lecture hall."

    stop music fadeout 2.0
    scene lecturehall
    play music "Audio/A_lecture_talking.mp3" fadein 4.0 fadeout 1.0
    with dissolve

    N "This time, the lecture hall is filled with students."
    N "Aristotle calms down the crowd of students, and begins speaking."
    stop music fadeout 2.0
    play music "Audio/A_greek_music.mp3" fadein 1.0 fadeout 1.0
    show aristotle 
    with dissolve
    A "Why do we study ethics? Why do you all come to class at all?"
    A "Ethics is the search for the correct way to live our lives. If we may find what is good, what is bad, and everything in between, we may lead better lives."
    menu:
        "What is good, then?"
        "Happiness for the greatest number.":
            jump A_Happiness
        "Good deeds.":
            jump A_Gooddeeds
        "Good intentions.":
            jump A_Goodintentions

label A_Happiness:
    A "True happiness comes from a life well lived, yet it is merely a by-product of doing good."
    jump A_Whatisvirtue

label A_Gooddeeds:
    A "Good deeds may give the appearance of a life well lived, yet often times more sinister motivations belie their beautiful appearance."
    jump A_Whatisvirtue

label A_Goodintentions:
    A "Good intention proves disastrous in the hands of fools."
    jump A_Whatisvirtue

label A_Whatisvirtue:
    A "The knowledge and skill to craft our emotions and actions is what you need to live a good life. This is what I call virtue."
    A "Rationale is the thing that separates us from beasts. It is, therefore, the very thing that we must hone to live our best lives."
    A "So, how may we acquire rationale, and therefore virtue?"
    menu:
        "Nature. We must be born with virtue.":
            jump A_Both
        "Nurture. We must learn virtue.":
            jump A_Both
        "Both. We must be born with virtue and learn virtue.":
            jump A_Both
label A_Both:
    A "It is both. We must be lucky enough to be born with good parents and friends who encourage virtuous activities."
    A "We must acquire first practical wisdom. This is what we are born with, yet also develop over time."
    A "We must also acquire ethical virtue, the ability to do good. This is derived from practical wisdom."
    A "Wisdom derived from rationale, and good deeds derived from virtue are both needed to live a good life."
    A "When we think of our ancient heroes, that of Hercules or Odysseus, we admire them not only for their physical prowess but also their mental fortitude."
    A "In the face of moral quandaries, they rarely hesitate or back down. They have the wisdom to act, and choose the best action available to them."
    A "This is what it means to be good and virtuous. It is to use practical wisdom to perform virtuous deeds. In other words, it is to know what good is and intend to do it."
    A "Let me ask you a hypothetical scenario, then."
    A "Suppose you and two children are enslaved by Athenian conquerers."
    A "In a twist of cruelness, an Athens guard tells you he will kill one child of your choice."
    A "If you choose no children, the guard will kill both."
    A "What is the right decision?"
    menu:
        "Tell the guard to kill one child.":
            jump A_Sophiesmenu
        "Abstain from answering.":
            jump A_Sophiesmenu

label A_Sophiesmenu:
    A "Many thinkers focus on the end result, yet here, neither decision is right or wrong."
    A "Because you are powerless, you cannot act completely virtuously. Your rationale for your choice, however, determines whether the decision you make is as virtuous as one can be."
    A "Choosing to kill one child to save the other may be virtuous. Choosing to abstain to refuse participation in this atrocity may also be virtuous."
    A "Life is filled with these grey areas. Virtue means walking the fine line between two extremes."
    A "A courageous person, for example, judges some fears worth facing. We deem our heroes brave for facing these dangers."
    A "However, a courageous person also judges some fears not worth facing. We deem these heroes shrewd for not being rash."
    A "Having the wisdom to know what this golden mean is and to act on it is to what it means to be virtuous."
    menu:
        "That sounds super vague! How am I supposed to decide anything based on that.":
            jump A_Vague
        "A middle ground cannot be found all the time!":
            jump A_Vague

label A_Vague:
    A "While virtuous action is vague, it can be applied to many circumstances."
    A "Suppose that you are a judge, and you must determine if your defendant is innocent or guilty. Surely, in this case there is no room for middle ground."
    A "What I mean by a golden mean is this: If we may save or condemn our defendant using a deliberative process that is neither motivated by emotion nor a rigid interpretation of law, we have found our golden mean."
    A "It is the deliberative process of an action, or the intention, that matters. The end decision by a virtuous judge will be the right one, because his intention was true."
    A "What is not virtuous, then?"
    menu:
        "Envy.":
            jump A_Envy
        "Anger.":
            jump A_Anger
        "Sadness.":
            jump A_Sadness

label A_Envy:
    A "In most cases, envy would indeed be not virtuous. Desire for physical pleasures is a sign of a lack of internal harmony and rationale."
    jump A_Emotions
label A_Anger:
    A "Anger, in the right amounts, may be virtuous. It must be proportional to the crime, however."
    jump A_Emotions

label A_Sadness:
    A "Sadness, in the right amounts, may be virtuous. It must be proportional to the grievance, however."
    jump A_Emotions

label A_Emotions:
    A "All of us have these emotions within us. Anger, sadness, envy. They pull and tug at us, yet these emotions are, like our rationale, what it means to be human. They cannot be condemned."

    A "So, we need to have the wisdom and control to reign in our desires for pleasure or power."
    A "Those that are overwhelmed by their urges become little more than beasts."
    jump A_AfterLecture

label A_AfterLecture:
    hide aristotle
    with dissolve
    N "Aristotle carries on with his lecture, and afterwards, the students stream out into the hallway."
    stop music fadeout 1.0
    play music "Audio/A_plaza_ambience.mp3" fadein 1.0 fadeout 1.0
    scene hall
    show aristotle
    with dissolve
    A "So, do you have a better understanding of my theory of virtue ethics now, after that lecture?"

    menu:
        "Not quite... could you elaborate on it a little?":
            jump A_Misunderstand
        "I think so!":
            jump A_Understand

label A_Misunderstand:
    A "That is alright... I have spent many years contemplating this, so just understanding it might not be so easy, I admit!"

    A "In summary, being just, honest, brave, generous, and overall living a good life takes practice."

    A "Many other thinkers restrict themselves to rules and try to quantify choices. This is right, this is wrong, and so on."

    A "However, I believe that only by honing your intellect and ethical wisdom can you make right decisions."

    A "I do not say anything that nobody knows, if I am honest. All of us look up to heroes and admire them for their virtuous deeds. I just ask myself to aim to be like those heroes."

    jump A_Understand

label A_Understand:
    A "Well, I hope I could be of help to your plight in the future. As for a relic, if I must hand over something..."

    pause(2.0)

    A "I know! I have a few rough drafts of my Nicomachean Ethics. They summarize my theory of virtue ethics fairly well. I do not think I will miss them."

    hide aristotle
    with dissolve
    N "Aristotle retrieves some scrolls from the lecture hall, and hands them to you."
    play sound "Audio/A_scroll_sound.mp3"
    show aristotle
    with dissolve

    A "That should do it."

    N "As he says those words, you feel yourself fading out of consciousness."

    A "... Are you okay? You look a little faint."

    scene white
    hide aristotle
    with dissolve
    jump cave4

label cave4:        # Return to Cave
label final_boss:   # Sphinx/Final Boss Thing
    return

label bad_ending:
    N "Bad ending"
    return

### EXAMPLES FOR REFERENCE ###
    ### Showing Images ###
    # scene <image> : Show background image of <image>.png or <image>.jpg
    # show <image> : Show character sprite of <image>.png or <image>.jpg
    # hide <image> : Hides character sprite
    # show <image> at right : Shows image at right of screen (or left, or center)

    ### Playing Music ###
    # play music <music.mp3>  : Plays music file (will loop)
    # stop music              : Stops music
    # play sound <effect.ogg> : Plays sound effect (will not loop)

    ### Transitions ###
    # with <transition> : Transitions all current images on the screen
    # - dissolve
    # - fade
    # - None (instant showing of image)

    ### Jumps and Labels ###
    # jump <label> : Jumps to label

    ### Dialogue ###
    # e "dialogue" : Show dialogue in game, said by <e> character
    # menu         : Show a menu with decisions

    # This ends the game.
