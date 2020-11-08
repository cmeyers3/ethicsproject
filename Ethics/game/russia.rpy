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
