# Character
define l = Character("Lea", color="#910b9f")
define n = Character("Note", color="#1900ffc0")
define nl = Character("???", color="#241d86")
define u = Character("Unity", color="#9f0b0b")
define unk = Character("???", color="#444444e3")

# Helper functions for ambience fading
init python:
    def fade_down_ambience():
        renpy.music.set_volume(0.15, delay=1.0, channel="music")

    def fade_up_ambience():
        renpy.music.set_volume(0.4, delay=2.0, channel="music")
    
default floor1 = {
    "waterFountain": {
        "FirstInteraction": False,
        "secondInteraction": False,
        "waterFountainInteracted": False,
        "doorKeyObtained": False
    },
    "LeaClassroom": {
        "chairChecking": 0,
        "classroomFirstInteracted": False,
        "insideClassRoom": False,
        "fromInsideClassroom": False
    },
    "Room2": {
        "chairChecking": 0,
        "insideClassRoom": False,
        "isRoomFound": False
    },
    "Room3": {
        "chairChecking": 0,
        "insideClassRoom": False,
        "isRoomFound": False
    },
    "hallway": {
        "firstHallwayInteraction": False
    },
    "puzzlePieces": {
        "Note1": False,
        "Note2": False,
        "Note3": False
    }
}

default counters = {
    "runningLives" : 3,
    "Sanity" : 5
}

default persistent.endings = {
    "endingAchieved" : False,
    "UnityEnding" : False,
    "Ending" : False
}

default floor2 = { 


}



label start:
    scene chairZoomed
 
    $ fade_down_ambience()
    play music "audio/night_ambience.mp3" fadein 2.0 volume 0.4
    with fade
    $ fade_up_ambience()
    "Lea woke up from her nap, her hair a mess from the deep sleep she had been in."

    scene chairUnzoomed
    with dissolve

    $ fade_down_ambience()
    play sound "audio/lightbulb_buzzing.mp3" volume 1 fadein 1.0 fadeout 2.0
    $ renpy.pause(2.0)
    stop sound
    $ fade_up_ambience()

    "There was nothing but the faint glow of moonlight and the weak neon light from the exit signs illuminating the hallways."

    show lea default at right
    with dissolve

    l "God... What time is it?"

    $ fade_down_ambience()
    play sound "audio/phone_click.mp3" volume 1 fadein 1.0 fadeout 2.0
    $ renpy.pause(3.0)
    stop sound
    $ fade_up_ambience()

    "Lady Luck wasn't on her side today, her phone was dead."

    l "I must've slept for a long... long time."

    $ fade_down_ambience()
    play sound "audio/stumble.mp3" volume 1 fadein 1.0 fadeout 2.0
    $ renpy.pause(2.0)
    stop sound
    $ fade_up_ambience()

    show lea headHurt at right
    with dissolve

    "She stood up and stumbled, catching herself on something nearby."

    l "Right, I skipped lunch earlier."

    "She held her temples."

    l "I need to get something to drink."

    menu:
        "Use the water fountain.":
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1 fadein 1.0 fadeout 2
            scene black
            with fade
            stop sound
            $ fade_up_ambience()
            pause 2
            stop sound
            jump waterFountain1st

        "Ignore your instincts, stay in the classroom.":
            $ fade_down_ambience()
            play sound "audio/door_open.mp3" volume 1 fadein 1.0 fadeout 2
            $ renpy.pause(3.0)
            stop sound
            $ fade_up_ambience()
            scene black
            with fade
            $ floor1["LeaClassroom"]["fromInsideClassroom"] = True
            jump returnToClassroom1st


# CLASSROOM INTERACTIONS
label returnToClassroom1st:
    scene Classroom1
    with fade

    if floor1["LeaClassroom"]["fromInsideClassroom"] == True:
        "Lea prepared to pack her belongings. The window outside showed a dark and cloudy night sky. Her brows furrowed."
    else:
        "Returning to the classroom she lounged by, Lea prepared to pack her belongings. The window outside showed a dark and cloudy night sky. Her brows furrowed."

    show lea default at right
    with fade

    l "It's not like anyone will be suspicious of me being out at night, but..."

    $ fade_down_ambience()
    play sound "audio/sigh.mp3" volume 1 fadein 1 fadein 1.0 fadeout 2
    $ renpy.pause(4.0)
    "She sighed."
    stop sound
    $ fade_up_ambience()

    l "I just really want to get home. My head is killing me."

    $ floor1["LeaClassroom"]["classroomFirstInteracted"] = True

    $ fade_down_ambience()
    play sound "audio/door_open.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(3)
    stop sound
    $ fade_up_ambience()

    $ fade_down_ambience()
    play sound "audio/footsteps_heels.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(7)
    stop sound
    $ fade_up_ambience()

    menu:
        "Head out, drink at the water fountain.":
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1 fadein 1.0 fadeout 1.5
            $ renpy.pause(9.0)
            stop sound
            $ fade_up_ambience()
            scene black
            with fade
            if floor1["waterFountain"]["waterFountainInteracted"] == True:
                "Lea returns to the water fountain."
                jump waterFountainInteracted
            elif floor1["waterFountain"]["secondInteraction"] == True:
                "Lea returns to the water fountain."
                jump waterFountain3rd
            elif floor1["waterFountain"]["FirstInteraction"] == True:
                jump waterFountain2nd
            else:
                jump waterFountain1st

        "Head out to the hallway.":
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1 fadein 1.0 fadeout 1.5
            $ renpy.pause(9.0)
            stop sound
            $ fade_up_ambience()
            jump hallway1st


label returnToClassroom:
    scene classRoom
    with fade

    if floor1["LeaClassroom"]["insideClassRoom"] == True:
        "..."
    else:
        $ fade_down_ambience()
        play sound "audio/door_open.mp3" fadein 1.0 fadeout 2
        $ renpy.pause(3.0)
        stop sound
        $ fade_up_ambience()
        "Lea enters the classroom. It's the same room she attends every school day."
        "But it feels like everyone left in a hurry."
        "They've been gone for a while already."

    if floor1["hallway"]["firstHallwayInteraction"] == True:
        menu:
            "search the chairs.":
                scene black
                with fade
                jump chairsLeaClassroom
            "search the teacher's desk.":
                scene black
                with fade
                jump teachersDeskLeaClassroom
            "head back to the hallway.":
                $ floor1["LeaClassroom"]["insideClassRoom"] = False
                scene black
                with fade
                jump hallwayFloor1
    else:
        menu:
            "Head out, head towards the water fountain.":
                scene black
                with fade
                if floor1["waterFountain"]["waterFountainInteracted"] == True:
                    "Lea returns to the water fountain."
                    jump waterFountainInteracted
                elif floor1["waterFountain"]["secondInteraction"] == True:
                    "Lea returns to the water fountain."
                    jump waterFountain3rd
                elif floor1["waterFountain"]["FirstInteraction"] == True:
                    jump waterFountain2nd
                else:
                    jump waterFountain1st
            "Head out to the hallway.":
                $ floor1["LeaClassroom"]["insideClassRoom"] = False
                scene black
                with fade
                jump hallway1st


# FIRST FLOOR HALLWAY
# SCRIPTED SCENES ONLY
label hallway1st:
    $ fade_down_ambience()
    stop music fadeout 1
    $ fade_up_ambience()
    $ fade_down_ambience()
    play music "audio/night_ambience.mp3" fadein 1.5
    $ fade_up_ambience()

    scene hallway1stFloor
    with fade

    $ fade_down_ambience()
    play sound "audio/footsteps_heels.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(2.0)
    stop sound
    $ fade_up_ambience()
    stop music
    "Lea walks back outside, it is still quiet, not even a cricket dares to break the tense air that fills the building."

    $ fade_down_ambience()
    play music "audio/wind_hallway.mp3" fadein 1
    $ fade_up_ambience()

    "She looks around, though disoriented from the throbbing pain in her head, she mutters out to herself."

    show lea default at right
    l "I should head out of here... I hope mom isn't worried."

    menu:
        "Head left, leave via the front doors.":
            $ fade_down_ambience()
            play sound "audio/footsteps_heels.mp3" fadein 1.0 fadeout 2
            $ renpy.pause(5.0)
            stop sound
            $ fade_up_ambience()
            scene black
            with fade
            jump leftEntrance1

        "Head right, leave through the back doors.":
            $ fade_down_ambience()
            play sound "audio/footsteps_heels.mp3" fadein 1.0 fadeout 2
            $ renpy.pause(2.0)
            stop sound
            $ fade_up_ambience()
            scene black
            with fade
            jump rightEntrance1


label leftEntrance1:
    scene black
    "Walking through the hall, she makes a turn to the left. Greeting her is the door, but something caught her eyes."

    scene hallwayBarricaded
    with fade

    $ fade_down_ambience()
    play sound "audio/chair_scrape.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(2.0)
    stop sound
    $ fade_up_ambience()

    "Stacks and stacks of chairs pile upon the door. It is all over the place, futile to break down."

    $ fade_down_ambience()
    play sound "audio/heartbeat_slow.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(5.0)
    stop sound
    $ fade_up_ambience()

    "She feels a rush of unease go through her."

    menu:
        "Check the back door.":
            $ fade_down_ambience()
            play sound "audio/footsteps_heels.mp3" fadein 1.0 fadeout 2
            $ renpy.pause(9.0)
            stop sound
            $ fade_up_ambience()
            scene black
            with fade
            jump rightEntrance2


label leftEntrance2:
    scene black
    "Sprinting through the halls, she makes her way to the front door."

    "Chills went down her spine. Unease turns to panic as Lea stares at what greets her."

    scene hallwayBarricaded
    with fade

    "Stairs, stacked so high it towered over her. She tries to remove one, but they aren't budging."

    show lea worried at right
    with fade
    l "No..."
    l "No!"
    l "I need to find a way to get out of here!"

    if floor1["waterFountain"]["doorKeyObtained"] == True:
        hide lea
        "She remembers something. Reaching into her pockets, she takes out a key to a door."
        $ fade_down_ambience()
        play sound "audio/keys_jingle.mp3" fadeout 1
        $ renpy.pause(1.0)
        stop sound
        $ fade_up_ambience()
        show lea worried at right
        l "Maybe there is something here that this key can open to."

    menu:
        "Return to the middle of the hallway.":
            jump hallwayFloor1


label rightEntrance1:
    scene black
    "Walking through the hall, she makes a turn to the right. Greeting her is the back door, but something caught her eyes."

    scene hallwayLocked
    with fade
    "Lea approaches the locked doors. It is chained and the knob was torn off."

    $ fade_down_ambience()
    play sound "audio/chain_rattle.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(5.0)
    stop sound
    $ fade_up_ambience()

    "She feels a rush of unease go through her."

    menu:
        "Check the front door.":
            scene black
            with fade
            jump leftEntrance2


label rightEntrance2:
    scene black
    "Sprinting through the halls, she makes her way to the front door."
    "Chills went down her spine. Unease turns to panic as Lea stares at what greets her."

    scene hallwayLocked
    with fade

    "It is the door to the exit, but it is locked tight. Chained with a lock and the knob is ripped right off. Lea tried kicking it."

    "Unfortunately, they aren't budging."

    show lea worried at right
    with fade
    l "No..."
    l "No!"
    l "I need to find a way to get out of here!"

    if floor1["waterFountain"]["doorKeyObtained"] == True:
        hide lea
        "She remembers something. Reaching into her pockets, she takes out a key to a door."
        $ fade_down_ambience()
        play sound "audio/keys_jingle.mp3" fadeout 1
        $ renpy.pause(1.0)
        stop sound
        $ fade_up_ambience()
        show lea worried at right
        l "Maybe there is something here that this key can open to."

    menu:
        "Return to the middle of the hallway.":
            jump hallwayFloor1


# WATER FOUNTAIN INTERACTIONS
label waterFountain1st:
    $ floor1["waterFountain"]["FirstInteraction"] = True
    scene waterfountain
    with fade
    "Lea steps on the pressure plate that activates the water fountain, nothing happens."

    $ fade_down_ambience()
    play sound "audio/metal_creaking.mp3" volume 1 fadein 1 fadeout 2
    $ renpy.pause(3)
    stop sound
    $ fade_up_ambience()

    menu:
        "Try again":
            $ fade_down_ambience()
            play sound "audio/fountain_click.mp3" fadein 1.0 fadeout 2
            $ renpy.pause(4.0)
            stop sound
            $ fade_up_ambience()
            jump waterFountain2nd

        "Return to the classroom.":
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1 fadein 1.0 fadeout 2
            $ renpy.pause(9.0)
            stop sound
            $ fade_up_ambience()
            if floor1["LeaClassroom"]["classroomFirstInteracted"] == True:
                scene black
                with fade
                jump returnToClassroom
            else:
                scene black
                with fade
                jump returnToClassroom1st


label waterFountain2nd:
    $ floor1["waterFountain"]["secondInteraction"] = True
    scene waterfountain
    with fade

    $ fade_down_ambience()
    play music "audio/quiet_hum.mp3" fadein 1.5
    $ fade_up_ambience()

    $ fade_down_ambience()
    play sound "audio/fountain_click.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(4.0)
    stop sound
    $ fade_up_ambience()

    "She tries turning the water fountain on again. Lea hears the rushing of liquid, but nothing flows out."

    $ fade_down_ambience()
    play sound "audio/drip_slow.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(5.0)
    "The faint echo of dripping pipes fills the hallway."
    stop sound
    $ fade_up_ambience()
    menu:
        "Try again":
            scene black
            with fade
            $ fade_down_ambience()
            play sound "audio/fountain_click.mp3" fadein 1.0 fadeout 2
            $ renpy.pause(4.0)
            stop sound
            stop music fadeout 1.0
            $ fade_up_ambience()
            jump waterFountain3rd

        "Return to the classroom.":
            stop music fadeout 1.0
            if floor1["LeaClassroom"]["classroomFirstInteracted"] == True:
                scene black
                with fade
                jump returnToClassroom
            else:
                scene black
                with fade
                jump returnToClassroom1st


label waterFountain3rd:

    $ floor1["waterFountain"]["waterFountainInteracted"] = True
    scene waterFountainOozeFlowing
    with fade

    $ fade_down_ambience()
    play sound "audio/tension_swell.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(9.0)
    stop sound
    $ fade_up_ambience()

    $ fade_down_ambience()
    play sound "audio/fountain_click.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(4.0)
    stop sound
    $ fade_up_ambience()

    "In a desperate attempt, Lea turns the water fountain on aggressively, and black unidentifiable liquid pours out."

    $ fade_down_ambience()
    play sound "audio/liquid_splash.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(8.0)
    stop sound
    $ fade_up_ambience()

    $ fade_down_ambience()
    play sound "audio/heartbeat_fast.mp3" volume 0.75 fadein 1.0 fadeout 2
    $ renpy.pause(3.0)
    stop sound
    $ fade_up_ambience()

    scene hallway1stFloor
    with fade

    show lea surprised at right
    "Lea stepped back, aghast by the sudden downpour."

    show lea default at right
    l "Maybe they turned off the filters at night. Still... that's... disturbing."

    stop sound fadeout 2.0
    stop music fadeout 3.0

    menu:
        "Return to the classroom.":
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1 fadein 1.0 fadeout 2
            stop sound
            $ fade_up_ambience()
            if floor1["LeaClassroom"]["classroomFirstInteracted"] == True:
                scene black
                with fade
                jump returnToClassroom
            else:
                scene black
                with fade
                jump returnToClassroom1st


label waterFountainInteracted:
    scene waterFountainOozeFlowing
    with fade

    $ fade_down_ambience()
    play music "audio/ambient_silence.mp3" fadein 2.0
    $ fade_up_ambience()

    $ fade_down_ambience()
    play sound "audio/drip_slow.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(4.0)
    stop sound
    $ fade_up_ambience()

    if floor1["waterFountain"]["doorKeyObtained"] == True:
        "Lea looks over to the water fountain."
        "The black ooze is gone."
        "Its stains are left as a gentle reminder to not drink from it."

        scene HallwayBack
        show lea worried at right
        with fade
        l "..."
    else:
        $ fade_down_ambience()
        play sound "audio/ooze_drip.mp3" fadein 1 fadein 1.0 fadeout 2
        $ renpy.pause(5.0)
        stop sound
        $ fade_up_ambience()

        "The ooze makes its way to the fountain's drain."
        "What remained was a key from the fountain. Lea is not sure how it managed to pop out of the water fountain's small spout."

        "She hesitantly picks the key up."
        $ fade_down_ambience()
        play sound "audio/keys_jingle.mp3" volume 1.0 fadeout 1
        $ renpy.pause(1.0)
        stop sound
        $ fade_up_ambience()
        "*You obtained a Door Key.*"
        $ floor1["waterFountain"]["doorKeyObtained"] = True

    menu:
        "Return to the classroom.":
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1 fadein 1.0 fadeout 2
            $ renpy.pause(9.0)
            stop sound
            $ fade_up_ambience()
            if floor1["LeaClassroom"]["classroomFirstInteracted"] == True:
                scene black
                with fade
                jump returnToClassroom
            else:
                scene black
                with fade
                jump returnToClassroom1st
### HALLWAY INTERACTIONS 
### ADVENTURE 
### VINCE TO NOT TAMPER FIRST PLEASE

label hallwayFloor1:
    scene hallway1stFloor 
    show lea default at right 
    with fade    
    "Lea is back at the hallway."
    if floor1["hallway"]["firstHallwayInteraction"] == True:
        "The hallway is silent."
        
        "Cackling sounds of her shoe's heels are what accompanies her as she walks through the halls devoid of life besides her own."
    else:
        "The air is tight, but time spent idling around here is time wasted on finding something to get out of here "
        $ floor1["hallway"]["firstHallwayInteraction"] = True

    "What to do now?"
    menu:
        "Approach the classrooms.":
            jump floor1Classrooms
        "Check each end of the hallways.":
            jump floor1Hallways
        "Approach the water fountain.":
            if floor1["waterFountain"]["waterFountainInteracted"] == True:
                "Lea returns to the water fountain."
                jump waterFountainInteracted
            elif floor1["waterFountain"]["secondInteraction"] == True:
                "Lea returns to the water fountain."
                jump waterFountain3rd
            elif floor1["waterFountain"]["FirstInteraction"] == True:
                jump waterFountain2nd
            else:
                jump waterFountain1st

label floor1Classrooms:
    menu:
        "head to your classroom.":
            scene black
            with fade
            jump returnToClassroom
        "head to a classroom by the right.":
            scene black
            with fade
            jump ClassroomFloor1Room2
        "head to a classroom by the left.":
            scene black
            with fade
            jump ClassroomFloor1Room3

label floor1Hallways:
    menu:
        "head left of the hallway.":
            scene black
            with fade
            jump HallwayFloor1Left
        "head right of the hallway.":
            scene black
            with fade
            jump HallwayFloor1Right

label HallwayFloor1Right:
    scene black
    "Lea walks towards the hallway to the right."
    scene hallwayLocked with fade
    

    "It is the door from earlier, it is still chained shut."

    menu: 
        "Try kicking it open.":
            "Lea takes a few steps back, and then runs towards the door and gave it a good kick."

            "..."

            "The Door did not budge."

            show lea default at right
            with dissolve

            l "It was worth the try."

            l "I should just try finding a key instead."
            menu:
                "Go back to the middle of the hallway.":
                    scene black with fade 
                    jump hallwayFloor1

        "Go back to the middle of the Hallway.": 
            scene black with fade 
            jump hallwayFloor1

label HallwayFloor1Left:
    scene black 
    "Lea walks towards the hallway to the left."
    scene LeftHallway with fade 

    "It is the same barricaded door from earlier."
    label backtoHallLeftChoice:
    scene LeftHallway with fade 
    menu: 

        "Look closer at the barricade.":

            scene hallwayBarricadedZoomed 
            show lea default at right 
            with fade
            "She takes a few steps closer at the barricade."

            "The pile of chairs were stationary,but she swears she could hear whispers."

            "It is as if the chairs are talking to each other."
            show lea worried at right 
            with dissolve
            "..."

            "No, They're trying to talk to her."
            scene black with fade
            jump backtoHallLeftChoice
        "Look at the left, towards the bathroom":

            "Lea looks over the bathroom, she has an uneasy feeling as she stares at the doorway."

            menu:
                "Read the notes." if floor1['puzzlePieces']['Note1'] or floor1['puzzlePieces']['Note2'] or floor1['puzzlePieces']['Note3']:
                    menu:
                        "Read the first note" if floor1['puzzlePieces']['Note1']:
                            "Lea opens the note and reads the content"

                            n "Am I doing the Right choice?"

                            n "Last week,I heard them talking about me when I was at the stalls. Everything they said weren't pretty in the slightest."

                            n "Complaining."

                            n "I wasn't dedicating enough time towards them."

                            n "I value my own grades more than I value people."

                            n "I am a lost cause."

                            n "Am I?"

                            n "Maybe I am not doing the Right thing."

                            n "But even the thought that my grades getting lower than what they are now."

                            n "I can't stop now."
                            show lea default at right 
                            with dissolve 
                            l "..."

                            l "There must be a reason why this was torn off from my journal."
                            jump backtoHallLeftChoice

                        "Read the second note" if floor1['puzzlePieces']['Note2']:
                            "Lea opens the note and reads the content"

                            n "I wonder what the others are Up to?"
                            
                            n "This project is difficult, I couldn't believe I just had to add all these extra things for no one other than myself."

                            n "No, they call me a dean's lister for a reason."

                            n "I am not doing this for myself. I just HAD to not submit anything lucklaster compared to my usual."

                            n "Or else."

                            n "Or else."

                            n "Or else."

                            n "Or else, they'll find out how unfit I am for this one"

                            n "..."

                            n "Am I even Up for this?"
                            show lea worried at right 
                            with dissolve 
                            l"..."

                            l"Why do I have to find my own journals here? Do they mean something?"
                            jump backtoHallLeftChoice

                        "Read the third note" if floor1['puzzlePieces']['Note3']:
                            "Lea opens the note and reads the content"
                            
                            n "Is there anything Left of my former self?"

                            n "I am a husk. My bags are big and I feel awful."

                            n "These grades. They;re great."
                            
                            n "But it is at the expense of my own self."

                            n "There is nothing Left for myself."
                            show lea worried at right 
                            with dissolve 
                            l "..."

                            l ""
                            jump backtoHallLeftChoice

                "Open the door." if floor1['waterFountain']['doorKeyObtained']:
                    "Flavor Text"
                    jump preBossEncounter
                    
                "Return to the left Hallway.":
                    scene black with fade
                    jump backtoHallLeftChoice
        
        "Return to the middle of the hallway.":
            scene black with fade 
            jump hallwayFloor1

### BATHROOM 

label preBossEncounter:
    scene bathroom with fade 

    "Lea looks over to the key, the door awaits infront of her."

    "She takes the key,inserts it, and turns."

    "The door opens, Lea walks inside."

    "The bathroom is silent, the eerie feeling of someone watching is a feeling Lea couldn't bear."

    "She flicked the switch to the room's lights, nothing."
    show lea worried at right 
    with dissolve
    
    l "I suppose the lights are killed here."

    l "There must be something here if the water fountain gave me this key."

    "Lea reaches her arms out, trying to feel what is infront of her."

    "She feels Ooze on the door of the bathroom stalls. The decision of avoiding the stalls arrived almost immediately."

    "..."

    "Lea soon feels the sink, her arm stumbles over the something metallic."
    show lea surprised at right
    with dissolve
    
    l "Another key?"

    l "Maybe this time it can open the lock."
    scene black with fade 

    "She walks out of the bathroom"

    scene bathroom with fade 

    l "Okay, now to open the door"

    "Lea takes a few steps forward, until she heard something that halted her."

    if persistent.endings["UnityEnding"] == False:
        unk "Lea..."
    else:
        u "Lea..."

    "The voice came from the bathrooms, it was the voice of one of her classmates."

    "Specifically, a friend of hers."

    if persistent.endings["UnityEnding"] == False:
        unk "Lea... Let's stay together, please."
    else:
        u "Lea... Let's stay together, please."

    l "Kate? is that you? Where are you? Were you hiding in the stalls?"

    "Lea steps forward, but she stops almost immediately."

    scene bathroomWithUnity with fade

    if persistent.endings["UnityEnding"] == False:
        unk "Lea... Let's stay together."
    else:
        u "Lea... Let's stay together."

    show lea scared with dissolve

    l "You're... You're not."

    if persistent.endings["UnityEnding"] == False:
        unk "You never go with us Lea. Stay with us."
        unk "Stay with us."
        unk "Stay with us."
        unk "Stay with us!"

    else:
        u "You never go with us Lea. Stay with us."
        u "Stay with us."
        u "Stay with us."
        u "Stay with us!"
    
    "Overwhelmed with the sudden urge to flee, she starts running."

    scene black with fade 

label Run:
    ""

label Run1:

label Run2:

label Run3:
    
### LEA CLASSROOM 

label chairsLeaClassroom:
    scene black 
    with fade 

    $ floor1["LeaClassroom"]["insideClassRoom"] = True

    "Checking each chair, she spends her time looking for anything useful here."

    if floor1["LeaClassroom"]["chairChecking"] == 0:
        "..."

        "The first row had nothing of value."
        show lea default at right
        with dissolve
        l "Not Good... There's nothing here."

        l "I should continue searching."
    elif floor1["LeaClassroom"]["chairChecking"] == 1:
        "..."

        "The last row had nothing of value."
        show lea default at right
        with dissolve
        l "Nothing here."

        l "I should continue searching."
    elif floor1["LeaClassroom"]["chairChecking"] == 2:
        "..."

        "The fourth row had nothing of value."
        show lea default at right
        with dissolve
        l "Nothing here."

        l "I should continue searching."
    elif floor1["LeaClassroom"]["chairChecking"] == 3:
        $ floor1["puzzlePieces"]["Note1"] = True
        "..."

        "Lea found something of value."
        show lea default at right
        with dissolve
        l "A note from a journal?"

        "She reads the content, it gives her a chill down her spine."
        show lea surprised at right
        with dissolve
        l "this is mine... How did this get here?"

        "*Obtained Note #3*"
        $ floor1["puzzlePieces"]["Note3"] =True

    else:
        show lea default at right
        with dissolve
        l "I think I already searched the chairs enough."
    
    if floor1["LeaClassroom"]["chairChecking"] < 4:
        $ floor1["LeaClassroom"]["chairChecking"] += 1

    jump returnToClassroom


label teachersDeskLeaClassroom:
    scene black 
    with fade 

    $ floor1["LeaClassroom"]["insideClassRoom"] = True

    "Walking to the teacher's desk, the desk itself was empty, but Lea pulls the drawer open."
    show lea default at right 
    with dissolve

    l "A rubik's cube? It's jumbled, someone must've confiscated it."
    show lea smiling at right 

    "Lea turns the cube a few times."
    
    l "That's a nice distraction."
    
    jump returnToClassroom

### ROOM 2 CLASSROOM 

label ClassroomFloor1Room2:
    scene black 
    with fade 

    if floor1["Room2"]["isRoomFound"]== False:
        "Lea heads to the right side, twisting the knobs of each of the rooms."

        "Locked."

        "Locked."

        "Locked."

        "One creaks open, the room is available."

    $ floor1["Room2"]["isRoomFound"]= True

    if floor1["Room2"]["insideClassRoom"] == False:
        "She carefully walks inside the door, no one was there to greet her. The chairs are tilted in such a way that it seemed like everyone left in a panic."
    else:
        "..."

    menu: 
        "Search the chairs.":
            scene black 
            with fade
            jump chairsRoom2 
        "Search the whiteboard":
            scene black 
            with fade
            jump whiteboardRoom2 
        "Head back to the halways":
            $ floor1["Room2"]["insideClassRoom"] = False
            scene black 
            with fade
            jump hallwayFloor1

label chairsRoom2:
    scene black
    with fade

    $ floor1["Room2"]["insideClassRoom"] = True

    "Checking each chair, she spends her time looking for anything useful here."

    if floor1["Room2"]["chairChecking"] == 0:
        "..."

        "The last row had nothing of value."
        show lea default at right
        with dissolve
        l "Not Good... There's nothing here."

        l "I should continue searching."

    elif floor1["Room2"]["chairChecking"] == 1:
        "..."

        "The middle row had nothing of value."
        show lea default at right
        with dissolve
        l "Nothing here."

        l "I should continue searching."

    elif floor1["Room2"]["chairChecking"] == 2:
        $ floor1["puzzlePieces"]["Note2"] = True
        "..."

        "Lea found something of value."
        show lea default at right
        with dissolve
        l "Its a note, and it looks like it's ripped from a journal."

        "Lea reads the contents of the note."
        show lea surprised at right
        with dissolve
        l "Why is this note in this room?"

        "*Obtained Note #1*"
        $ floor1["puzzlePieces"]["Note1"] = True

    else:
        show lea default at right
        with dissolve
        l "I think I already searched the chairs enough."
    
    if floor1["Room2"]["chairChecking"] < 3:
        $ floor1["Room2"]["chairChecking"] += 1

label whiteboardRoom2:
    scene Classroom1 with fade 
     
    $ floor1["Room2"]["insideClassRoom"] = True

    "Lea approaches the whiteboard,she looks over the crevices."

    "Her head moves to the right, and then left for anything useful there."

    "..."

    show lea default at right 
    with dissolve

    l "Markers, Chalks, and an eraser."

    l "Nothing useful here."

    "She walks back to the middle of the room"
    scene black
    with fade  

    jump ClassroomFloor1Room2  

### ROOM 3 CLASSROOM 

label ClassroomFloor1Room3:
    scene Classroom1 
    if floor1["Room3"]["isRoomFound"] == False:
        "Lea heads to the left side, twisting the knobs of each of the rooms."

        "Locked."

        "Locked."

        "Locked."

        "One creaks open, the room is available."
    
    $ floor1["Room3"]["isRoomFound"] = True

    if floor1["Room3"]["insideClassRoom"] == False:
        "She walks inside the classroom. It is just as barren as the halls outside."
    else:
        "..."

    menu: 
        "Search the chairs.":
            scene black 
            with fade
            jump chairsRoom3 
        "Search the whiteboard":
            scene black 
            with fade
            jump whiteboardRoom3 
        "Head back to the halways":
            $ floor1["Room3"]["insideClassRoom"] = False
            scene black 
            with fade
            jump hallwayFloor1

label chairsRoom3:
    scene black
    with fade

    $ floor1["Room3"]["insideClassRoom"] = True

    "Checking each chair, she spends her time looking for anything useful here."

    if floor1["Room3"]["chairChecking"] == 0:
        "..."

        "The last row had nothing of value."
        show lea default at right
        with dissolve
        l "Not Good... There's nothing here."

        l "I should continue searching."

    elif floor1["Room3"]["chairChecking"] == 1:
        "..."

        "The middle row had nothing of value."
        show lea default at right
        with dissolve
        l "Nothing here."

        l "I should continue searching."

    elif floor1["Room3"]["chairChecking"] == 2:
        "..."
        show lea default at right
        with dissolve
        
        l "There nothing useful at the chairs,I should stop searching for now."

    else:  
        show lea default at right
        with dissolve
        l "I think I already searched the chairs enough."
    
    if floor1["Room3"]["chairChecking"] < 3:
        $ floor1["Room3"]["chairChecking"] += 1
    
    jump ClassroomFloor1Room3

label whiteboardRoom3:
    scene black with fade

    $ floor1["Room3"]["insideClassRoom"] = True

    "Lea approaches the whiteboard,she looks over the crevices."

    "Her head moves to the right, and then left for anything useful there."

    "..."

    show lea default at right 
    with dissolve

    l "Markers, Chalks, and an eraser."

    show lea surprised at right 

    l "..."

    hide lea surprised
    with dissolve

    "She picks up a piece of folded paper on the crevice of the whiteboard."

    "She opens it and reads the contents inside."

    show lea worried at right
    with dissolve

    l "... This is from my journal. This is not supposed to be here."

    "*Obtained Note #2*"
    $ floor1["puzzlePieces"]["Note2"] = True

    jump ClassroomFloor1Room3
