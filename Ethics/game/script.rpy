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
define m = Character("Cthulhu III")
default item_completion = True
default question_number = 1
default has_done_1 = 0
default has_done_2 = 0
default has_done_3 = 0
default num_wrong = 0

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
label russia:       # Russia -> Kant
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
label final_boss_beginning:   # Sphinx/Final Boss Thing
    $renpy.music.set_volume(0.3, delay=0, channel='music')
    scene corrupted_background
    show thresh
    play music "audio/battle_music.mp3" fadein 1.0 fadeout 1.0

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
            jump final_boss_beginning
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
            jump final_boss_beginning
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
            $renpy.music.set_volume(1, 0, channel='music')
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
label bad_ending:
    N "Bad ending"
    return
