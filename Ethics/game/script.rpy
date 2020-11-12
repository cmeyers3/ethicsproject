﻿### Building/Compiling Game ###
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
    

    jump intro

label intro:         # Ancient Cave
    scene celebration
    with dissolve
    N "The year is 2021 and the cure for COVID-19 is found. The Global Health Organization has found that implanting a small chip in everyone's brain will provide immunity to the coronavirus and every other infectious disease that exists."
    
    scene brain
    with dissolve
    N "With this newfound technology and the world's desire to return to a normal life, all major countries and health organizations have approved this augmentation."
    
    scene before
    with dissolve
    N "Within the past several months, 95 percent of the world's population has adopted the the brain implant named S.U.S. which stands for Super Useful Stuff."
    N "As a cautious and educated individual with a Bachelor's degree from the University of Notre Dame, you have held back on getting the brain implant with a hunch that something bad may happen."
    N "The past few months have been a sort of utpoia with almost all of the world's illnesses and diseases eradicated. Patients have been cured of HIV/AIDS and global happiness has increased to all time highs."
    N "Unfortunately, as we all know, your hunches are always correct..."
    
    scene gate
    with dissolve
    N "A mysterious gate appears in the middle of South Bend, Indiana and the evil Cthulhu has somehow hijacked the brain implantations that everyone has been using"
    N "The Cthulhu has a plan to enhance the human race to its next level by turning human brains into computers"
    
    scene anonymous
    with dissolve
    N "You are sent an anonymous message on Facebook that warns you of the dangers of this tranhumanism the Cthulhu is trying to reach"
    N "The message says you must embark on a journey to obtain the Philosopher's stone"
    N "In order to do this you must learn three ethical frameworks and prove you are worthy of the stone"
    N "You must time travel to each time period to train under each philosopher and learn their ethical framework"
    N "You must obtain their approval and receive a specital item from each philosopher that you must use to unlock the gate to the Philosopher's Stone"
    N "The first location is Ancient China"
    N "Time to go..."
    jump china


label china:
    scene white
    N "Flash!"
    N "Your ears ring and the piercing flash of white light leaves you disoriented…"

    scene temple
    play music "Audio/A_China.mp3" fadein 1.0 fadeout 1.0
    with dissolve
    N "After a while, you finally begin to see again, in what you assume to be Ancient China!"
    show confucius
    C "I have been anticipating your arrival. Come quickly, you are late. My lessons are starting soon."
    N "You follow Confucius, glad that you don't have to explain your sudden presence."

    scene courtyard
    show confucius
    with dissolve
    N "You follow Confucius to a courtyard, eager to learn and take the next step to obtaining the philosopher's stone."
    with dissolve
    C "Are you ready to begin your lesson?"
    menu:
        "Don't you want to know why I am here?.":
            jump DontCare
        "I am ready to begin.":
            jump ConfuciusIntro

label DontCare:
    C "I do not care of your past. I only care what you do with my teaaching from this point onwards."
    jump ConfuciusIntro

label ConfuciusIntro:
    C "Welcome to 6th Century BC China. We are currently in the Zhou Dynasty. My name is Kong Qi, you may know me as Confucius."
    C "Today I shall be teaching you my core tenets. Do with them what you wish, but it is my wish that you embrace the lifestyle of a junzi."
    jump ConfuciusJunzi

label ConfuciusJunzi: 
    M "Junzi? What does that mean?"
    C "I teach all my disciples about personal cultivation. In order to achieve this, they must embrace the lifestyle of a true junzi, also known as a \"gentleman\"." 
    menu: 
        "So how does one be a gentlman?"
        "You must be born into a family of noble status":
            jump junzi_answer
        "You must dress and act like a person of high social status": 
            jump junzi_answer
        "You must display qualities that are both ethical and cultural": 
            jump junzi_answer
    
label junzi_answer: 
    C "A true gentlemen does not depend on what family they are born into or what social status they look like they are in."
    C "Instead, a gentleman should be the ethical exemplar in society and show three main qualities."
    C "Humaneness(ren), filial piety(xiao), and ritural decorum(li)."
    C "Here, let me explain to you what all of these mean."
    jump humaneness

label humaneness: 
    C "In Ren, one must always respect others and treat them well. Your interpersonal relationships is one of the core aspects of your life."
    C "Therefore you must treat others in a way you would want to be treated yourself. Only the man of humanity can rightly love some people and rightly despise people."
    C "Only a human person is able to determine how to ethically treat other people."
    jump filialpiety
    
label filialpiety: 
    C "In Xiao, we focus on your relationship with your parents. You have a duty to be loyal to your parents. This loyalty is one that can even overwhelm the law."
    C "That is the level of devotion you should show to your family. And as a result, this should be the level of devotion and selflessness you should show to the people around you."
    C "In fact, are you not all one big family in the end?"
    jump ritualdecorum

label ritualdecorum: 
    C "Li, which means ritual decorum is the basis of good social order."
    C "It is the lifestyle in which a proper junzi must lead. In this lifestyle we see actions centered around ren."
    C "Li is the cultivation of the lifetstyle a junzi must lead, a life centered around humaneness and treating people properly with respect."
    jump C_AfterLecture


label C_AfterLecture:
    hide confucius
    with dissolve
    N "Confucius carries on with his lecture, and afterwards, the students stream out into the hallway."
    stop music fadeout 1.0
    play music "Audio/A_China_2.mp3" fadein 1.0 fadeout 1.0
    scene temple
    show confucius
    with dissolve
    C "Do you now understand what Confucianism is about?"

    menu:
        "Not quite... could you elaborate on it a little?":
            jump C_Misunderstand
        "I think so!":
            jump C_ExplainTranshumanism

label C_Misunderstand:
    C "I guess it is hard to learn about a lifestyle one must lead without having any experience in it before."

    C "In summary, one must lead a life where one can be a junzi, a moral exemplar in society. A junzi's life centers around ren, humaneness."

    C "A true Confucian junzi does not promote conformity, but rather harmony."

    C "A ruler should not surround themselves with people who share similar viewpoints as them, but rather a diverse group of people who will complement and balance out each other by providing their own special input."

    jump C_AskConfucious


label C_AskConfucious:
    N "It seems you have learned the way of Confucianism. It is time to apply this knowledge to help the future."
    M "Thank you for your knowledge. Now, I need your help."

    menu:
        "What are your thoughts on transhumanism?":
            jump C_ExplainTranshumanism
        "Do you know what transhumanism is?":
            jump C_ExplainTranshumanism

label C_ExplainTranshumanism:
    C " Transhumanism? What is that?"
    M "Transhumanism is a movement that arises in the future. It's goal is to modify the human condition by using technology to enhance human intellect and philosophy."
    C "Ah, I see. From what you've learned of my teachings, what do you think I would think of this transhumanism?"

    menu:
        "I think you would support transhumanism.":
            jump C_Agree
        "I think you would not support transhumanism.":
            jump C_Disgaree

label C_Agree:
    C "You are wrong. "
    jump C_ConfuciusView

label C_Disgaree: 
    C " You are correct. "
    jump C_ConfuciusView

label C_ConfuciusView:
    C "I am a believer of humanism. The human being in itself has a lot of potential to do great things. Enhancement through technology is unnecessary."
    C "This transhumanism of yours sounds like it is pursuing a sense of immortality for the body, however I believe in immortality of the spirit. The immortal spirit of our ancestors guides us through life."
    jump C_Understand

label C_Understand:
    C "Well, I hope I could be of help to your plight in the future. As for a gift, if I must hand over something..."

    pause(2.0)

    C "I shall gift you with my Analects. They are my life teachings so I hope they help you with your journey."

    hide confucius
    with dissolve
    N "Confucius retrieves some scrolls from his room, and hands them to you."
    play sound "Audio/A_scroll_sound.mp3"
    show confucius
    with dissolve

    C "Here you are."

    N "As he says those words, you feel yourself fading out of consciousness."

    C "Now, hurry along. You do not want to delay your journey any futher. You are already keeping your next teacher waiting."
    scene white
    hide confucius
    with dissolve
    jump russia

label russia:       # Russia -> Kant
    scene white
    N "Flash!"
    N "Your ears ring and the piercing flash of white light leaves you disoriented…"

    scene konisberg
    play music "Audio/K_Russia.mp3" fadein 1.0 fadeout 1.0
    with dissolve
    N "After a while, you finally begin to see again, in what you assume to be Russia in the Age of Catherine the Great!"
    N "You seem to be in the middle of a courtyard with young posh men lounging about reading books."
    N "After a quick look around, you begin to deduce that this must be Albertinum, the institution that Immanuel Kant lecured at in his later years."
    N "With no idea of how to find Kant, you begin to follow several students entering the college building, hopelessly trying to blend in with your 21st century jeans and sneakers."
    stop music fadeout 2.0
    scene hallway
    with dissolve
    N "After sneaking from room to room, unable to find this elusive philosopher, you begin to feel exhausted and hungry"
    scene grass
    with dissolve
    N "You take a step back outside into the midafternoon sun, find a nice spot next to the school under the trees, and slowly fall into a light slumber"

    play music "Audio/K_Dreamy.mp3" fadein 1.0 fadeout 1.0
    menu:
        N "As you drift off, you begin to dream about your favorite Russian cuisine..."
        "Beef Stroganoff":
            $ food = "Beef Stroganoff"
            jump beef
        "Morozhenoe":
            $ food = "Morozhenoe"
            jump morozhenoe
        "Pirozhki":
            $ food = "Pirozhki"
            jump pirozhki

label beef:
    scene beef
    with dissolve
    N "You begin dreaming about beef stroganoff, a classic Russian dish that consists of rice, noodles, or potatoes topped with strips of creamy sauce with mushroom and tomatoes"
    jump wakeup

label morozhenoe:
    scene morozhenoe
    with dissolve
    N "You begin dreaming about Morezhenoe, a Russian variety of creamy ice cream made with pure whole milk topped with fruits, nuts, and chocolate"
    jump wakeup

label pirozhki:
    scene pirozhki
    with dissolve
    N "You begin dreaming about Pirozhki, a fluffy fried puff pastry packed full of savory meat, potatoes, and cheese"
    jump wakeup

label wakeup:
    N "Just as you begin monching on your imaginary food, you hear a voice..."
    stop music fadeout .1
    K "Student, what are you doing!? Happiness is not an ideal of reason, but of imagination."
    scene grass
    with dissolve
    show kant
    with dissolve
    N "You sit up quickly in surprise. A short man stands before you with his hair curled on both sides looking like one of those old founding fathers you learned about in American history class"

    menu:
        N "Flustered, you respond by saying..."
        "I..I'm sorry I was daydreaming about food because I was so hungry...":
            jump hunger
        "Sorry sir, who are you?":
            jump its_kant
    jump A_Outsiders

label hunger:
    K "When one hungers, one desires sustenance and that is a natural human response"
    K "However daydreaming about food does not bring you fulfilment. Go acquire your nourishment so that you may be attentive in your classes"
    menu:
        "Let me go back to sleep please...":
            jump lazy
        "Wow you must be a philosopher. What's your name?":
            jump its_kant

label lazy:
    K "In the presence of laziness and lethargy, one must commit to reflecting on one's thoughts and seek a more meaningful life."
    K "The busier we are, the more acutely we feel that we live, the more conscious we are of life."
    menu:
        "Wow.. that's very inspirational!":
            jump invite
        "I guess so...":
            jump invite

label invite:

    menu:
        K "Yes. Anyways, will you attend my lecture today?"
        "Umm I don't even know who you are":
            jump its_kant
        "Sure! What's your name again?":
            jump its_kant

label its_kant:

    menu:
        K "I am Immanuel Kant of course. Did you forget who your instructor is?"
        "OMG!! IMMANUEL KANT??":
            jump confused
        "Just who I was looking for! I'm from the future.":
            jump future

label confused:
    K "..."

    menu:
        K "I am flattered by your excitement... It seems as if you are a new student here so I will kindly encourage you to come to my lecture."
        "LOL sounds good! I'm also from the future btw":
            jump future
        "Thanks for the advice! I'll see you at your lecture":
            jump to_lecture

label future:
    K "Hmmm... The future you say? That must explain the strange garb that you don"

    menu:
        K "How must I believe you? My reasoning leads me to not believe in such outlandish tales. Do my eyes and ears deceive me?"
        "Yeah... I'm from the future. I can't tell you much more":
            jump future_reaction
        "Indeed I am. I cannot explain it I just need to learn Deontology":
            jump future_reaction

label future_reaction:
    K "Ah well.. seems believable. Hurry along then. Lecture begins in 5 minutes"
    jump to_lecture

label to_lecture:
    scene hallway
    with dissolve
    N "You have agreed to attend Kant's lecture and follow him to the lecture hall"
    hide kant
    scene classroom
    play music "Audio/A_lecture_talking.mp3" fadein 4.0 fadeout 1.0
    with dissolve

    N "You arrive at the lecture hall filled with students."
    N "Kant walks to the front of the room and pulls up his lecture notes."
    stop music fadeout 2.0
    show kant
    with dissolve
    K "Good morning students. Today we will talk about universal moral laws and that maxims that we apply to ourselves"
    K "Let me begin be presenting a hypothetical scenario that we all face"
    K "Imagine a person that is thirsty and wishes to drink water"
    menu:
        K "Does this person make a moral choice to drink water?"
        "Yes":
            jump water
        "No":
            jump water

label water:
    K "No of course one does not think 'is drinking water moral or not?'"
    K "He desires water, therefore he drinks. In the same manner, one may ask what do you desire to eat today?"
    K "He will then respond with whatever food he desires at the moment. Because these hypothetical imperatives rely on desires that vary from person to person, they lack the element of necessity and therefore are not true moral commands"
    K "In contrast, we can examine the statement 'Help those in need'. This type of scenario I call a categorical imperative."
    K "What I mean by this categorization is that imperatives like these do not depend on one's personal desires or feelings"
    K "One cannot argue against the statement that it is right to help those in need. This is the form that our moral obligations must be in when we consider the categorical imperative"
    K "In this realm of thought, we can conclude there must be universal laws that define how one should behave in light of moral dilemmas"
    K "We must then act only on the maxims by which one can at the same time will that it should become a universal law"
    K "To elaborate on this statement, I will propose another scenario"
    K "Suppose I borrow money from you promising to return it later, but I know full well that I will not return it"
    K "I am operating on the maxim that I will borrow money when I need it knowing that I will never pay it back"
    K "This, however, results in a contradiction as if this maxim was to be practiced universally, our whole economy would collapse and the value of one's trust would be undermined"
    K "It does not matter whether one wants to be moral or not as the universal moral law is binding for us all"
    K "The categorical imperative states... ... ..."
    play music "Audio/K_Dreamy.mp3" fadein 1.0 fadeout 1.0


    if food == "Beef Stroganoff":
        scene beef
    elif food == "Morozhenoe":
        scene morozhenoe
    else:
        scene pirozhki

    with dissolve
    hide kant
    N "After being woken up from your previous nap, you feel extremely sleepy and doze off during Kant's lecture, dreaming again about the delicious food"

    scene classroom
    with dissolve
    stop music
    play sound "Audio/K_Bamboo.mp3"
    N "You are woken to the pain of a wooden stick slapped across your head"

    show kant
    N "You look up to see Kant's short figure staring at you in the middle of an empty classroom"
    K "Hello time traverler?? Can you hear me?"
    K "Why have you fallen asleep during my lecture?"

    menu:
        K "Does this seem like a joke to you?"
        "Yes":
            jump k_walk
        "No":
            jump k_walk


label k_walk:
    K "**Sigh** If you have traveled here to learn my teachings, learn them you must"
    K "Come, talk with me as we take a stroll around the grounds"

    scene grass
    with dissolve
    show kant
    play music "Audio/K_Nature.mp3" fadein 1.0 fadeout 1.0
    N "You follow Kant out to the schoolgrounds and begin to walk around the campus"
    stop music fadeout 2.0
    menu:
        K "Student, where do you devise your morals from?"

        "Religion obviously, God is the creator of the world and holds all moral decisions in his judgement":
            $ morals = "religion"
            jump k_religion
        "Reason... It just makes sense":
            $ morals = "reason"
            jump k_reason
        "I don't know why don't you tell me?":
            $ morals = "reason"
            jump k_reason

label k_religion:
    K "Religion is a place where many people draw their moral beliefs and foundations. However, there exist many religions throughout our known world"
    K "Christianity, Islam, Buddhism, are all religions that have significant followings. Who is to say that a Christian philosophy is greater than a Buddhist's"
    K "The nature of differing faiths and religions creates a divide in universal maxims and we will not always draw the same answer to moral questions by looking at our different faiths"
    if morals == "religion":
        jump k_reason
    else:
        jump trolley

label k_reason:
    K "Reason is the best place to draw one's morals as there are certain moral truths to everything we ought to do"
    K "Just as 2 + 2 = 4, morality exists as a constant of nature no matter who you are or what your faith is"
    K "Think of the categorical imperitive when making your moral decisions"
    K "If what you do became a universal moral law, would that result in a contradiction"
    K "If you can deduce that your decision could be a universal moral law, then you have made the correct decision"
    if morals == "reason":
        jump k_religion
    else:
        jump trolley

label trolley:
    K "Now you understand that reason should be the primary driver of your moral foundations"
    K "Next let us consider this unique moral dilemma"
    K "There are five people tied to a trolley track with an out of control trolley speeding toward the victims"
    K "You have the opportunity to stop the trolley killing these five innocent men by pushing me in the way of the trolley to stop it"
    K "In one situation, the five men end up dead and the other results in your friend dead, but the five men spared"
    play sound "Audio/K_Train.mp3"

    menu:
        K "What should you choose?"
        "Duhh, I'd just push you in the way and save the five people. You're gonna die in 1804 anyways":
            jump kill_kant
        "Kant you're my homie I'd never push you in the way to save these five strangers <3":
            jump save_kant

label kill_kant:
    K "... I did not know our relationship was like this how could you??"
    K "Your decision is entirely unacceptable! Did you not pay attention to what I just taught you?"
    K "We are all persons and must not treat people simply as a means to an end. They must be respected as ends in themselves"
    K "By pushing me into the trolley, you are using my body as a means to save others and thereby disrespecting who I am as a person"
    K "While the net result may be more lives saved, we should not base our reasoning solely on the overall utility"
    K "People may do things with entirely malicious intentions that somehow result in a good deed, but that does not make them moral"
    K "Anyways, I think we are done here. You seem to have hostile intentions toward me and I am inclined to distance myself from you before I am found in a ditch somewhere in the schoolgorunds"
    jump k_bye_bye

label save_kant:
    K "Correct! While I do not understand what a homie is, you have made the wise decision"
    K "It's important to treat each and every individual as a person and as ends in themselves"
    K "We should never use another person purely as a means to an end and by choosing not to push me, you have made the correct rational decision according to my teachings"
    K "While the net result may be more lives saved, we should not base our reasoning solely on the overall utility"
    K "People may do things with entirely malicious intentions that somehow result in a good deed, but that does not make them moral"
    K "It seems like you have understood the main foundations of my philosophy teachings."
    jump k_bye_bye

label k_bye_bye:
    K "You have acquired all the knowledge you need about my philosophy on reasoning and the categorical imperative despite sleeping through my lecture"

    menu:
        K "Go along then back to where you came"
        "Actually can I ask you one more question?":
            jump k_transhumanism
        "One sec please":
            jump k_transhumanism

label k_transhumanism:
    M "So a question about the future. Let's say that somehow we can change who we are by enhancing our intellect or physical abilities through things we installed in our body or brain."
    K "Well that seems rather odd to do, but go on"
    M "Is adding these things to your body ethical?"
    menu:
        K "Hmmm... well what do you think?"
        "Yeah it could be ethical. Creates better good for society":
            jump k_transhumanism_answer
        "Nope not ethical. We are giving up what it means to be human":
            jump k_transhumanism_answer
        "Well it really depends on the intentions":
            jump k_transhumanism_answer

label k_transhumanism_answer:
    K "It seems like much good can be done with this futuristic technology you speak about so if the general consensus of society is to use these things to further the capacity of the human race, it would seem to be ethical by the standards of the categorical imperative."
    K "However, there if there is a case of one using this thing selfishly to enhance his being to dominate or oppress others, this would not be ethical at all"
    K "Hehe seee?? Once again, one can use the categorical imperative here to discern the correct decision here even in this supernatural futuristic scenario that is completely hypothetical right?"
    M "Yes thank you for your insight"
    menu:
        K "Alrighty now scurry along back home. You'll be late for dinner"
        "Sorry I need an artifact from you to bring back for the Philosopher's stone":
            jump k_artifact
        "Umm hello?? I can't leave empty handed. Artifact please":
            jump k_artifact

label k_artifact:
    K "Huh?? You need an artifact? Well.. let me see.. "
    N "Kant rummages around his pockets looking for an artifact"
    K "It seems like I left all my papers in my office somewhere.. hehe too bad"
    N "As he comes up with nothing, your heart sinks at the possibility of going back empty handed"
    menu:
        "Please give me anything you have":
            jump k_paper
        "I'm desparate. I'll take that piece of trash in your coat pocket":
            jump k_paper

label k_paper:
    K "Well if you insist"
    N "Kant finds a scrunched up piece of parchment in his pocket and tosses it to you"
    K "Here ya go, have to get going now. Auf Wiedersehen!"
    hide kant

    N "As Kant frolicks away from you, you unfurl the crumpled up piece of parchment to find scribbled writing"
    N "Behind the stains of wine and food, you can make out the start of what you conclude to be the early drafts of his 'Critique of Pure Reason'"
    N "You exhale in relief as you at least have an excerpt of Kant's most famous work"
    N "You begin to feel faint as your discourse with Kant has left you exhausted"
    N "The scene begins to fall away as you slowly drift into unconsciousness"
    jump greece

label greece:       # Ancient Greece -> Aristotle
    scene white
    N "Your ears ring as again, a piercing flash of white light leaves you disoriented…"

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
    N "You have a question that has been bothering you since lecture ended, and approach Aristotle afterwards to ask it."
    menu:
        "How might you apply your theory of virtue ethics to technology?":
            jump A_Technology

label A_Technology:
    A "Technology? Might you explain what that means?"
    menu:
        "It is like magic meant to improve our lives.":
            jump A_Transhumanism
        "It is like magic meant to gain power over our universe.":
            jump A_Transhumanism

label A_Transhumanism:
    A "Ah, so we are jumping to imaginary scenarios now, are we?"
    A "Though, having the power of something like your technology has been the topic of many a talk between Plato and I..."
    A "I think that technology would be wonderful to have in our lives!"
    A "For example, say that this technology grants us eternal life."
    A "The prospect of death may motivate us to seek truth and rationale in our lives, however, as too much life might fill us with sloth."
    A "In fact, some live their whole lives pursuing everything but virtue."
    A "Eternal life granted by your technology would not change that."
    A "Therefore, as long as we pursue further practical wisdom in our extended lives, we might become more virtuous than before."
    
    menu:
        "What if this involved giving up your physical body?":
            jump A_ByeBody
        "But would that not mean your life is not your own anymore?":
            jump A_NotLife

label A_ByeBody:
    A "Hmm..."
    A "I am not sure I would miss this frail body of mine, if I am honest."
    A "If technology could allow me to move as I did when I was young, or lift the heaviest of boulders with ease, of course I would do this."
    A "Though, I believe that intention does matter in cases such as this."
    A "Should you assist yourself with technology in such a manner, intention matters."
    A "A king who merges with technology to prolong their tyrannical reign fails to pursue virtue in his action."
    A "A philosopher who merges with technology to pursue greater wisdom and seek righteousness, however, may succeed in acquiring even greater virtue over their extended life."
    A "Perhaps, if technology or magic is born from humanity's rationale, it is even more virtuous to derive happiness from something that is uniquely human."
    jump A_NoSad

label A_NotLife:
    A "Ah, so this is the heart of your question. What is it to be human?"
    A "If I desire to be one with technology, untethered to my physical form, is that virtuous?"
    A "I would argue that it is just as virtuous as living with a physical form."
    A "Perhaps, if technology or magic is born from humanity's rationale, it is even more virtuous to derive happiness from something that is uniquely human."
    A "Though, I believe that intention does matter in cases such as this."
    A "Should you assist yourself with technology in such a manner, intention matters."
    A "A king who merges with technology to prolong their tyrannical reign fails to pursue virtue in his action."
    A "A philosopher who merges with technology to pursue greater wisdom and seek righteousness, however, may succeed in acquiring even greater virtue over their extended life."
    jump A_NoSad

label A_NoSad:
    menu:
        "What if technology could end suffering for humanity?":
            jump A_YesSad

label A_YesSad:
    A "End suffering? That sounds a lot like death to me."
    A "Should technology end suffering for humanity, our lives would either be akin to the lives of the gods themselves, or no life at all."
    A "Even curiosity might be considered suffering, as we search for knowledge we do not yet know."
    A "Despite its pains, suffering motivates us to pursue virtue. In a way, rational suffering makes us uniquely human, and also separates us from beasts."
    A "I can understand if technology eases suffering. To a certain extent, suffering limits our capability of pursuing happiness."
    A "However, a life devoid of suffering seems to have no room for virtue within it."
    jump A_Done

label A_Done:
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
    jump final_boss_beginning

label final_boss_beginning:   # Sphinx/Final Boss Thing
    $renpy.music.set_volume(0.3, delay=0, channel='music')
    scene corrupted_background
    show thresh
    play music "audio/battle_music.mp3" fadein 1.0 fadeout 1.0

    m "Who goes there?"

    m "I am Cthulhu III. I guard the Philosopher's Stone, which can only be obtained by solving my riddles."
    m "Huh? You say that's ripped from Harry Potter? Well, it wasn't destroyed it was *ahem* given to me through some gratuitous plot holes."
    m "Anyway, no one may attempt to achieve this prize unless they have obtained The Scrolls of Nicomachean Ethics, The Analects, and Kant's Drafts."
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
        m "Hmm, looks like you are braver than I thought. I am bound by oath to challenge you with riddles. (because I can't think of anything better to do with my time)."
        jump rule_explanation
    else:
        m "Wretched human! Did you think you could deceive me? I will crush your mortal body and devour your soul!"
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
    m "As the harbringer of greatness, my goal is to augment humanity (transhumanism) so that it can achieve greater things."
    m "However, I must need clarification on the ethical backing of my goal before I can proceed. As a reward, I shall grant you the philosopher's stone."
    m "However, I am an impatient immortal. If you get more than three wrong, then, like a stereotypical monster, I will eat your soul."
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
    m "Hmm I see that you have talked with Aristotle. Let's see if my little advisor has anything to say."
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
    m "Hmm, if ethical virtue is derived from practical wisdom, then perhaps transhumanism could still be possible."
    m "After all, if humans are augmented with technological devices, then perhaps they have enhanced abilities to derive this practical wisdom."
    m "I still need more insight from, Aristotle, however."
    m "According the Aristotle's Athenian Guard Scenario, is every ethical action clear cut?"
    $question_number += 1
    menu:
        "No; often, there are grey areas.":
            play sound "audio/correct.mp3"
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
    m "Indeed, there may be many grey areas, my little one. Perhaps these grey areas do cover transhumanism, which is why we must examine this issue closely."
    m "It could be that transhumanism leans towards the dark rather than the light, which is why exploring this issue is important."
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
    m "Indeed, the deliberative process that matters rather than the action, according to Aristotle."
    m "My intention is to take humanity to the next level since I believe that it will benefit your race."
    m "Therefore, since my intention is good, then that means filling your little brains with nanomachines is ethical!"
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
    m "Indeed, giving your kind robotic enhancements also has the potential to eliminate and inadvertently shun emotions."
    m "However, Aristotle says that we must not shun these emotions, for they are part of being human. This indeed puts a roadblock in my plan."
    m "Piece back my memory, small one."
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
    m "Indeed; if the design for human augmentation goes as planned, then the damage to your minds remains in question."
    m "It could cause uncontrollable emotions, which would dehumanize you, contrary to the original intentions of the augmentation."
    m "Thus, the ethical risk from Aristotle's point of view may be too great to attempt human augmentation."
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
    m "Indeed, anyone is able to achieve Junzi, no matter their status."
    m "Therefore, elevating your species to a higher status may prove ineffective in achieving Junzi. Perhaps augmenting your kind is not such a great idea after all..."
    m "Which one of these qualities is NOT part of Junzi?"
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
    m "Hmm. As we can see, worldly wealth is not a part of Junzi. Even though I will augment humanity as a gift, what if your kind takes advantage of it?"
    m "I shudder to think of how humanity can so easily turn such a gift into a commodity; where a fellow man's augmentations are the focus of his worldly wealth."
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
    m "Indeed, we should treat others with respect. Although I am a monster, I do not have the power to give the entirety of humanity augmentations at once."
    m "A situation could easily realize where hostility emanates from those that have augmentations, and those that don't."
    m "Such a divide could make following Ren, and therefore, ethical principles, much harder than anticipated."
    m "What about the second quality: Filial Piety?"
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
        "You should show loyalty to everyone around you, as humanity is one big family.":
            play sound "audio/correct.mp3"
            jump question_directory
label question_10:
    m "What strikes me with Confucius's teachings is the fact that every human is part of a great family."
    m "With augmentations, however, robotic decision-making and logical thought could prove to be roadblocks in finding the reason or empathy to respect others."
    m "After all, a computer has no qualms when one takes advantage of others if it is a logical decision, which Filial Piety strictly prohibits."
    m "It saddens me to see that adding augmentations may cause humanity to drift farther apart, rather than come closer together."
    m "I see that you are indeed an attentive student of Confucious. We shall see if your insights point me towards a decision."
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
    m "Ritual Decorum is about upholding the previous two values, but through ceremony and public expectations."
    m "With this point, my plans may have a glimmer of hope. Public expectation will be followed, as robotics will find it most logial to uphold a social structure."
    m "But you say that that is not free will? Indeed, that is true. One shouldn't be forced to take these actions by their foreign machinery; indeed, it should come from human wilingness to follow all three values."
    m "Another philosopher foils my plan to ethically augment humans with technology."
    m "Well, we have reached our final school of philosophy, Deontology. I must commend you for getting this far."
    m "Although my plans to augment humanity seem to have stalled...I still have hope that I will find ethical backing from Kant."
    m "Anyways, what type of imperative does not depend on one's feelings and desires?"
    $question_number += 1
    menu:
        "Globule Imperative":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Categorical Imperative":
            play sound "audio/correct.mp3"
            jump question_directory
        "Conditional Imperative":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Shampoo Imperative":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
label question_12:
    m "There are many categorical imperatives that one must follow regardless of the situation."
    m "Perhaps my robotic prostheses for humanity could help with following these imperatives; just a little bit of hard-coding rules should do the trick."
    m "We must then act only on the maxims by which one can at the same time will that it should become a _________"
    $question_number += 1
    menu:
        "Universal Law":
            play sound "audio/correct.mp3"
            m "I love universal laws. Sorry, I meant Universal Studios. Ba doom tsss."
            jump question_directory
        "National Law":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "State Law":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Your Mom's Law":
            play sound "audio/oof.mp3"
            m "Yeah, in retrospect it's a really bad joke. Can't fault me for trying to be creative."
            $num_wrong += 1
            jump question_directory
label question_13:
    m "Again, it should be a simple matter of programming these universal laws into your augmented minds so that you only act upon those maxims, and nothing else."
    m "Speaking of rules and maxims, does it matter if one strives to be moral (i.e. does intention matter)?"
    $question_number += 1
    menu:
        "Yes":
            play sound "audio/correct.mp3"
            jump question_directory
        "No":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
label question_14:
    m "Maybe you just guessed correctly. After all, it was a 50/50 chance."
    m "Based upon your answer, however, that means that one can be controlled by robots; so long as the robots'actions are moral, then all is well."
    m "However, the responsibility of finding the right maxims to program will fall upon me, a task that I cannot achieve alone."
    m "If humanity were to crack my code to find ways to change the maxims, that would cause even greater danger."
    m "Let's make this question a little harder to compensate: What should we derive our morals from?"
    $question_number += 1
    menu:
        "Life of Pi by Yann Martel":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "I'm tired of games just end me.":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Religion":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Yourself":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            jump question_directory
        "Reason":
            play sound "audio/correct.mp3"
            jump question_directory
label question_15:
    m "It is true that reason should dictate our morals. However, even I cannot say that my reasoning is perfect."
    m "It is important to make the distinction that, while a robot may follow code to the letter, the programmer may have flawed reasoning when writing the code."
    m "Therefore, even I cannot be infallible when deciding what maxims are universal, and in what way I could program them."
    m "It is indeed a very troubling issue that may show that, even from Kant's perspective, human augmentation may not be the best choice."
    m "Prepare yourself for your final question!"
    m "Should we always base our decisions around utility?"
    $question_number += 1
    menu:
        "Yes":
            play sound "audio/oof.mp3"
            $num_wrong += 1
            m "Wrong! And on the very last question too! Your fate may have been sealed by this error."
            jump question_directory
        "No":
            play sound "audio/correct.mp3"
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
    m "Based off of your answers, that means...transhumanism leans towards being immoral!"
    m "I can feel my power already waning from the unethical principles backing my actions!"
    m "What is happening to me? Why am I fading? Noooooooooooo......."
    scene peacerestored
    with Dissolve(0.5)
    stop music fadeout 1.0
    play sound "audio/link_victory_theme.mp3"
    queue music "audio/rito_village_but_really_its_windwaker.mp3"
    "The monster disappears into a green mist. His aura of corruption is lifted from the landscape, revealing a peaceful, alternative Windows XP background."
    show phil_stone
    "The Philosopher's Stone suddenly pops up from the ground where the monster once stood."
    "You pick it up and place it in your pocket for safekeeping, or perhaps to sell it at a pawn shop."
    "Peace has been restored, and the world thanks you for ridding it of a great evil."
    "Or so it thinks..."
    scene white
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
label endgame:
    return
label bad_ending:
    N "Bad ending"
    return
