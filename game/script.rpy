define persistent.endings = {
    "endingAchieved" : False,
    "UnityEnding" : False,
    "FalseIdolEnding" : False,
    "GoldenEnding" : False, 
    "FalseEnding": False,
    "TrueEnding" : False
}

define isDemo = False

# Character
define l = Character("Lea", color="#910b9f")
define n = Character("Note", color="#1900ffc0")
define st = Character("Shatter", color="#241d86")
define u = Character("Unity", color="#9f0b0b")
define unk = Character("???", color="#444444e3")
define au = Character("Aurum", color="#d4c74ae3") 
define k = Character("Kate", color = "#d44ac8e3") 
define m = Character("Mom", color = "#3f2699e3")

# Helper functions for ambience fading
init python:
    def fade_down_ambience():
        renpy.music.set_volume(0.3, delay=1.0, channel="music")

    def fade_up_ambience():
        renpy.music.set_volume(0.8, delay=2.0, channel="music")
    
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
        "isNoteObtained" : False,   
        "Note1": False,
        "Note2": False,
        "Note3": False
    }
}

default counters = {
    "floor1" : {
        "runningLives" : 3,
        "noteCount" : 0
    },
    "floor2" : {
        "Sanity" : 5,
        "ComputersVisited" : 0
    }
    
}

label start:
    if persistent.endings["endingAchieved"] == True:
        if persistent.endings["TrueEnding"] == False:
            scene black with fade
            window hide
            centered "Lea's body is still here."

            centered "It tries to remember."

            centered "It wanted to know what happened."

        menu:
            "Check memories.":
                jump memoryCheck
            "Continue on.":
                if persistent.endings["TrueEnding"]:
                    centered "Lea is now recovering from her toils."

                    centered "You should too."

                    centered "You deserve it."
                    $ renpy.quit()
                else:
                    jump gameStart
    else:
        jump gameStart
    
label gameStart:
    window show 
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
            play sound "audio/walking_heels_echo.mp3" volume 1 
            scene black
            with fade
            stop sound
            $ fade_up_ambience()
            pause 2
            stop sound
            jump waterFountain1st

        "Ignore your instincts, stay in the classroom.":
            $ fade_down_ambience()
            play sound "audio/door_open.mp3" volume 1
            $ renpy.pause(3.0)
            stop sound
            $ fade_up_ambience()
            scene black
            with fade
            $ floor1["LeaClassroom"]["fromInsideClassroom"] = True
            jump returnToClassroom1st


# CLASSROOM INTERACTIONS
label returnToClassroom1st:
    
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
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
    play sound "audio/sigh.mp3" volume 1 fadein 1.0 fadeout 2
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
    
    $ fade_down_ambience()
    play music "audio/hallway_ambience_2.mp3" fadein 1.5
    $ fade_up_ambience()
    scene black
    "Sprinting through the halls, she makes her way to the front door."

    "Chills went down her spine. Unease turns to panic as Lea stares at what greets her."

    scene hallwayBarricaded
    with fade

    "Stairs, stacked so high it towered over her. She tries to remove one, but they aren't budging."

    show lea scared at right
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
            scene black with fade
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
    
    $ fade_down_ambience()
    play music "audio/hallway_ambience_2.mp3" fadein 1.5
    $ fade_up_ambience()
    scene black
    "Sprinting through the halls, she makes her way to the front door."
    "Chills went down her spine. Unease turns to panic as Lea stares at what greets her."

    scene hallwayLocked
    with fade

    "It is the door to the exit, but it is locked tight. Chained with a lock and the knob is ripped right off. Lea tried kicking it."

    "Unfortunately, they aren't budging."

    show lea scared at right
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
            scene black with fade 
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
    with dissolve
    "Lea stepped back, aghast by the sudden downpour."

    show lea default at right
    with dissolve
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
    

    $ fade_down_ambience()
    play music "audio/ambient_silence.mp3" fadein 2.0
    $ fade_up_ambience()

    $ fade_down_ambience()
    play sound "audio/drip_slow.mp3" fadein 1.0 fadeout 2
    $ renpy.pause(4.0)
    stop sound
    $ fade_up_ambience()

    if floor1["waterFountain"]["doorKeyObtained"] == True:
        scene waterFountain 
        with fade 
        "Lea looks over to the water fountain."
        "The black ooze is gone."
        "Its stains are left as a gentle reminder to not drink from it."

        scene HallwayBack
        show lea worried at right
        with fade
        l "..."
    else:
        scene waterFountainOozeFlowing
        with fade
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
        show bathroomKey with dissolve
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

label hallwayFloor1:
    
    $ fade_down_ambience()
    play music "audio/hallway_ambience.mp3" fadein 1.5 volume 0.4
    with fade
    $ fade_up_ambience()

    play sound "audio/soft_wind.mp3" fadein 1.5 volume 0.3
    scene hallway1stFloor 
    show lea default at right 
    with fade    
    
    "Lea is back at the hallway."

    if floor1["hallway"]["firstHallwayInteraction"] == True:
        $ fade_down_ambience()
        play sound "audio/walking_heels_echo.mp3" volume 0.8
        "The hallway is silent."
        "Cackling sounds of her shoe's heels are what accompanies her as she walks through the halls devoid of life besides her own."
        stop sound fadeout 2.0
        $ fade_up_ambience()
    else:
        play sound "audio/low_rumble.mp3" volume 0.3 fadein 2.0
        "The air is tight, but time spent idling around here is time wasted on finding something to get out of here."
        stop sound fadeout 1.5
        $ floor1["hallway"]["firstHallwayInteraction"] = True

    "What to do now?"

    menu:
        "Approach the classrooms.":
            jump floor1Classrooms
        "Check each end of the hallways.":
            jump floor1Hallways
        "Approach the water fountain.":
            if floor1["waterFountain"]["waterFountainInteracted"] == True:
                $ fade_down_ambience()
                play sound "audio/walking_heels_echo.mp3" fadein 1.0 volume 0.5
                "Lea returns to the water fountain."
                stop sound fadeout 1.5
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
        "Return to Lea's Classroom.":
            scene black with fade 
            jump returnToClassroom
        "Head to a classroom by the right.":
            scene black with fade 
            jump ClassroomFloor1Room3
        "Head to a classroom by the left.":
            scene black with fade 
            jump ClassroomFloor1Room2

label floor1Hallways:
    menu: 
        "Head left to the hallway.":
            scene black with fade
            jump HallwayFloor1Left
            
        "Head right of the hallway.":
            scene black with fade
            jump HallwayFloor1Right

# --- HALLWAY RIGHT ---

label HallwayFloor1Right:
    
    $ fade_down_ambience()
    play music "audio/hallway_ambience.mp3" fadein 1.5 volume 0.4
    $ fade_up_ambience()
    play sound "audio/walking_heels_echo.mp3" volume 0.6
    "Lea walks towards the hallway to the right."
    stop sound fadeout 1.5

    scene hallwayLocked with fade
    $ fade_down_ambience()
    play sound "audio/chain_rattle.mp3" fadein 1.0 volume 0.8
    "It is the door from earlier, it is still chained shut."
    stop sound fadeout 1.0
    $ fade_up_ambience()

    menu: 
        "Try kicking it open.":

            $ fade_down_ambience()
            play sound "audio/walking_heels2.mp3" volume 0.7
            $ renpy.pause(2)
            stop sound fadeout 0.5
            "Lea takes a few steps back, and then runs towards the door and gave it a good kick."
            play sound "audio/footsteps_running.mp3" volume 0.7
            stop sound fadeout 0.5

            play sound "audio/door_kick_thud.mp3" volume 1.0
            "..."
            $ renpy.pause(1.5)
            "The door did not budge."
            stop sound fadeout 1.0
            $ fade_up_ambience()

            show lea default at right
            with dissolve

            l "It was worth the try."
            l "I should just try finding a key instead."
            menu:
                "Go back to the middle of the hallway.":
                    scene black with fade 
                    play sound "audio/walking_heels_echo.mp3" volume 0.5
                    jump hallwayFloor1

        "Go back to the middle of the Hallway.": 
            scene black with fade 
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            jump hallwayFloor1


# --- HALLWAY LEFT ---

label HallwayFloor1Left:
    
    $ fade_down_ambience()
    play music "audio/hallway_ambience.mp3" fadein 1.5 volume 0.4
    $ fade_up_ambience()
    play sound "audio/footsteps_slow.mp3" volume 0.6
    "Lea walks towards the hallway to the left."
    stop sound fadeout 1.0
    scene LeftHallway with fade 

    play sound "audio/faint_whispers.mp3" fadein 2.0 volume 0.3
    "It is the same barricaded door from earlier."
    stop sound fadeout 1.5

    label backtoHallLeftChoice:
    scene LeftHallway with fade 
    menu: 
        "Look closer at the barricade.":

            $ fade_down_ambience()
            play sound "audio/creaking_wood.mp3" volume 0.8
            scene hallwayBarricadedZoomed 
            show lea default at right 
            with fade
            "She takes a few steps closer at the barricade."
            stop sound fadeout 1.0
            $ fade_up_ambience()
            $ fade_down_ambience()
            play sound "audio/whispers_layered.mp3" fadein 1.0 volume 0.4 #gusto ko ipagawa toh sa pinsan ko
            "The pile of chairs were stationary, but she swears she could hear whispers."
            "It is as if the chairs are talking to each other."
            show lea worried at right 
            with dissolve
            "..."
            "No, they're trying to talk to her."
            $ fade_up_ambience()
            stop sound fadeout 2.0
            scene black with fade
            jump backtoHallLeftChoice
        "Look at the left, towards the bathroom.":
            $ fade_down_ambience()
            play sound "audio/drip_slow.mp3" fadein 1.5 volume 0.5
            scene BathroomOutside with fade 
            "Lea looks over the bathroom, she has an uneasy feeling as she stares at the doorway."
            $ fade_up_ambience()
            stop sound fadeout 1.5

            menu:
                "Read the notes." if floor1['puzzlePieces']['Note1'] or floor1['puzzlePieces']['Note2'] or floor1['puzzlePieces']['Note3']:
                    $ fade_down_ambience()
                    play sound "audio/page_flip.mp3" volume 0.6
                    $ fade_up_ambience()
                    menu:
                        "Read the first note" if floor1['puzzlePieces']['Note1']:
                            show note with dissolve
                            "Lea opens the note and reads the content"
                            $ fade_down_ambience()
                            play sound "audio/paper_rustle.mp3" volume 0.7
                            n "Am I doing the Right choice?"
                            n "Last week,I heard them talking about me when I was at the stalls..."
                            stop sound
                            $ fade_up_ambience()
                            show lea default at right 
                            with dissolve 
                            l "..."
                            l "There must be a reason why this was torn off from my journal."
                            jump backtoHallLeftChoice

                        "Read the second note" if floor1['puzzlePieces']['Note2']:
                            show note with dissolve
                            $ fade_down_ambience()
                            play sound "audio/paper_rustle.mp3" volume 0.7
                            
                            "Lea opens the note and reads the content"
                            
                            n "I wonder what the others are Up to?"
                            
                            stop sound
                            $ fade_up_ambience()
                            n "This project is difficult, I couldn't believe I just had to add all these extra things for no one other than myself."

                            n "No, they call me a dean's lister for a reason."

                            n "I am not doing this for myself. I just HAD to not submit anything lucklaster compared to my usual."

                            n "Or else."

                            n "Or else, they'll find out how unfit I am for this one"

                            n "..."

                            n "Am I even Up for this?"
                            show lea worried at right 
                            with dissolve 
                            l"Why do I have to find my own journals here? Do they mean something?"
                            jump backtoHallLeftChoice

                        "Read the third note" if floor1['puzzlePieces']['Note3']:
                            show note with dissolve
                            
                            play sound "audio/paper_rustle.mp3" volume 0.7
                            
                            "Lea opens the note and reads the content"

                            n "Is there anything Left of my former self?"

                            n "I am a husk. My bags are big and I feel awful."

                            n "These grades. They're great."
                            
                            n "But it is at the expense of my own self."

                            n "There is nothing Left for myself."

                            stop sound
                            $ fade_up_ambience()
                            show lea worried at right 
                            with dissolve 

                            l "..."

                            l "This may come to use later." 
                            
                            l "I just don't know how." 
                            jump backtoHallLeftChoice
        
                "Open the door." if floor1['waterFountain']['doorKeyObtained']:
                    "Approaching the bathroom, key in hand, she is sort of doubting whether to go in or not."
                    menu:
                        "Go in regardless.":

                            "Lea strangthen's her resolve."
                            scene black with fade

                            $ fade_down_ambience()

                            play sound "audio/key_unlock.mp3" fadein 1.0 volume 0.8

                            stop sound

                            $ fade_up_ambience()

                            jump preBossEncounter
                        "Change mind, head back.":
                            show lea worried at right 
                            with dissolve
                            l "I should search the floor first."
                            jump backtoHallLeftChoice
                    
                    
                "Return to the left Hallway.":
                    scene black with fade
                    jump backtoHallLeftChoice
        
        "Return to the middle of the hallway.":
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            scene black with fade 
            jump hallwayFloor1

# --- PRE-BOSS SEQUENCE ---

label preBossEncounter:
    
    $ fade_down_ambience()
    play music "audio/tense_drone_1.mp3" fadein 1.5 volume 0.5
    $ fade_up_ambience()
    scene BathroomOpen with fade 

    "Lea looks over to the key, the door awaits in front of her."
    $ fade_down_ambience()
    play sound "audio/door_open.mp3" volume 0.8
    
    "She takes the key, inserts it, and turns."
    stop sound fadeout 1.0
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/lock_click.mp3" volume 0.6
    $ renpy.pause(1.0)
    stop sound
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/door_open.mp3" volume 0.8
    "The door opens, Lea walks inside."
    stop sound fadeout 1.0
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/walking_heels3.mp3" fadein 0.5 volume 0.7
    scene black with fade

    "The bathroom is silent, the eerie feeling of someone watching is a feeling Lea couldn't bear."

    stop sound fadeout 2.0
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/light_switch_click.mp3" volume 0.5

    "She flicked the switch to the room's lights, nothing."

    show lea worried at right 
    with dissolve
    
    l "I suppose the lights are killed here."
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/low_rumblez.mp3" fadein 1.5 volume 0.3

    l "There must be something here if the water fountain gave me this key."
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/slimy_surface.mp3" volume 0.6
    "She feels ooze on the door of the bathroom stalls..."
    stop sound fadeout 1.5
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/metallic_clink.mp3" volume 0.8
    "She feels the sink, her arm stumbles over something metallic."
    show lea surprised at right
    with dissolve
    
    l "Another key?"
    l "Maybe this time it can open the lock."

    scene black with fade 
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/walking_heels2.mp3" fadein 0.8 volume 0.6
    "She walks out of the bathroom"
    stop sound fadeout 1.5

    scene BathroomOpen with fade 
    $ fade_up_ambience()
    $ fade_down_ambience()
    l "Okay, now to open the door"
    "Lea takes a few steps forward, until she heard something that halted her."

    play sound "audio/distant_voice_reverb.mp3" fadein 1.0 volume 0.4
    if persistent.endings["UnityEnding"] == False:
        unk "Lea..."
    else:
        u "Lea..."
    stop sound fadeout 1.5
    
    "The voice came from the bathrooms, it was the voice of one of her classmates."

    if persistent.endings["UnityEnding"] == False:
        $ fade_down_ambience()
        play sound "audio/ghostly_voice.mp3" fadein 2.0 volume 0.6
        unk "Lea... Let's stay together, please."
        $ fade_up_ambience()
    else:
        $ fade_down_ambience()
        play sound "audio/ghostly_voice.mp3" fadein 2.0 volume 0.6
        u "Lea... Let's stay together, please."
        $ fade_up_ambience()
    stop sound fadeout 1.5
    $ fade_down_ambience()
    l "Kate? Is that you? Where are you? Were you hiding in the stalls?"

    scene BathroomUnity with fade
    play sound "audio/heavy_breathing.mp3" fadein 1.0 volume 0.5

    if persistent.endings["UnityEnding"] == False:
        unk "Lea... Let's stay together."
    else:
        u "Lea... Let's stay together."
    stop sound fadeout 1.0
    $ fade_up_ambience()
    show lea scared at right 
    with dissolve

    $ fade_down_ambience()
    l "You're... You're not."
    play sound "audio/static_rise.mp3" fadein 2.0 volume 0.7
    if persistent.endings["UnityEnding"] == False:
        unk "You never go with us Lea. Stay with us!"
    else:
        u "You never go with us Lea. Stay with us!"
    stop sound fadeout 1.5
    $ fade_up_ambience()

    $ fade_down_ambience()
    "Overwhelmed with the sudden urge to flee, she starts running."
    play sound "audio/footsteps_running.mp3" volume 1.0 fadein 0.5

    scene black with fade 
    stop sound fadeout 2.0
    $ fade_up_ambience()
label Run:
    scene hallway1stFloor with fade 
    show lea scared at right 
    with dissolve
    $ fade_down_ambience()
    play music "audio/tense_silence.mp3" fadein 1.5
    $ fade_up_ambience()

    if counters["floor1"]["runningLives"] < 3:
        "Something isn't right."

        "She feels like she's back from the start."

    if counters["floor1"]["runningLives"] == 3:
        $ fade_down_ambience()
        "Hearing the sound of Ooze splasing, she hears the monster from behind trying to catch up to her."
        play sound "audio/ooze_drip.mp3" volume 1.0 fadein 0.5

        "She comes across the hallway, it holds multiple paths."
        stop sound fadeout 2.0
    elif counters["floor1"]["runningLives"] == 2:
        $ fade_down_ambience()
        play sound "audio/monster_footsteps.mp3" volume 1.0 fadein 0.5
        "Lea hears the faint sounds of the abomination's multiple feet clasping as it pursues her."
        stop sound fadeout 2.0
        $ fade_down_ambience()
        play sound "audio/distorted_voices.mp3" volume 1.0 fadein 0.5
        "The distorted voice of multiple people ring across the hallway"
        stop sound fadeout 2.0
        $ fade_up_ambience()
        if persistent.endings["UnityEnding"] == False: 
            
            unk "Lea! Don't leave us!"
        else:
            u "Lea! Don't leave us!"

    elif counters["floor1"]["runningLives"] == 1:
        "It's gaining ground."
        $ fade_down_ambience()
        play sound "audio/monster_footsteps.mp3" volume 1.0 fadein 0.5
        "She could hear the individual multiple steps, along with the Ooze."
        stop sound fadeout 2.0
        
        play sound "audio/monster_lurk.mp3" volume 1.0 fadein 0.5
        "It's Near."
        stop sound fadeout 2.0
    else:
        scene black with fade
        play sound "audio/grab.mp3" volume 1.0 fadein 0.5
        "Lea feels something grab her."
        stop sound fadeout 2.0
        jump UnityEnding
        $ fade_up_ambience()
    
    "Where should she go?"
    menu:
        "Head Up.":
            $ counters["floor1"]["runningLives"] -= 1
            scene black with fade
            $ fade_down_ambience()
            "She proceeds forward."
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            jump Run
        "Head Right.":
            scene black with fade
            stop sound fadeout 2.0
            $ fade_up_ambience()
            $ fade_down_ambience()
            "She makes a turn to the right."
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            jump Run1 
        "Head Left.":
            $ counters["floor1"]["runningLives"] -= 1
            scene black with fade
            stop sound fadeout 2.0
            $ fade_up_ambience()
            $ fade_down_ambience()
            "She makes a turn to the left."
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            jump Run
    stop music

label Run1:
    scene hallway2ndFloor 
    with fade
    $ fade_down_ambience()
    play music "audio/tense_silence.mp3" fadein 1.5
    $ fade_up_ambience()
    if counters["floor1"]["runningLives"] == 3:
        show lea surprised at right
        with fade
        $ fade_down_ambience()
        play sound "audio/door_open.mp3" volume 0.5
        "She opens a classroom to the right. For a moment, she thought she messed up."
        stop sound fadeout 2.0
        play sound "audio/monster_footsteps.mp3" volume 0.5
        "But in the other end was another hallway. She hears the monster from behind."
        stop sound fadeout 2.0
        play sound "audio/footsteps_running.mp3" volume 0.5
        "Lea continues sprinting"
        stop sound fadeout 2.0
        $ fade_up_ambience()
    else:
        show lea scared at right
        with fade 
        $ fade_down_ambience()
        play sound "audio/walking_heels_echo.mp3" volume 0.5
        "Lea remembers to take a right turn."
        stop sound fadeout 2.0
        play sound "audio/monster_footsteps.mp3" volume 0.5
        "She hears the abomination behind her."
        stop sound fadeout 2.0
        play sound "audio/footsteps_running.mp3" volume 0.5
        "Wasting no time, she continues sprinting."
        stop sound fadeout 2.0
        $ fade_up_ambience()
    "Where should she go?"
    menu:
        "Head Up.":
            scene black with fade
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            "She proceeds forward."
            stop sound fadeout 2.0
            $ fade_up_ambience()
            jump Run2
        "Head Right.":
            $ counters["floor1"]["runningLives"] -= 1
            scene black with fade
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            "She makes a turn to the right."
            stop sound fadeout 2.0
            $ fade_up_ambience()
            jump Run 
        "Head Left.":
            $ counters["floor1"]["runningLives"] -= 1
            scene black with fade
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            "She makes a turn to the left."
            stop sound fadeout 2.0
            $ fade_up_ambience()
            jump Run
    stop music
label Run2:
    scene hallway1stFloor with fade 
    $ fade_down_ambience()
    play music "audio/tense_silence.mp3" fadein 1.5
    $ fade_up_ambience()
    if counters["floor1"]["runningLives"] == 3:
        show lea worried at right
        $ fade_down_ambience()
        play sound "audio/walking_heels2.mp3" volume 0.5
        "The hallways felt endless, yet she pursues further."
        
    else:
        show lea worried at right
        "She feels the corridor extend continously."

        "She's nearly out of here."
        stop sound fadeout 2.0
        $ fade_up_ambience()
    "A distored set of voices rings behind her"
    
    if persistent.endings["UnityEnding"] == False:
        unk "Lea!"

        unk "Stay with us!"

        unk "Don't leave us again!"
    else:
        u "Lea!"

        u "Stay with us!"

        u "Don't leave us again!"
    
    "Where should she go?"
    menu:
        "Head Up.":
            $ counters["floor1"]["runningLives"] -= 1
            scene black with fade
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            "She proceeds forward."
            stop sound fadeout 2.0
            $ fade_up_ambience()
            jump Run
        "Head Right.":
            $ counters["floor1"]["runningLives"] -= 1
            scene black with fade
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            "She makes a turn to the right."
            stop sound fadeout 2.0
            $ fade_up_ambience()
            jump Run 
        "Head Left.":
            scene black with fade
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            "She makes a turn to the left."
            stop sound fadeout 2.0
            $ fade_up_ambience()
            jump Escape
    stop music

label Escape: 
    scene hallwayLocked with fade
    $ fade_down_ambience()
    play music "audio/escape.mp3" fadein 1.5
    $ fade_up_ambience()
    $ fade_down_ambience()
    play sound "audio/footsteps_running.mp3" volume 0.5
    "There she ran, what greets her was the locked door."
    stop sound fadeout 2.0
    $ fade_up_ambience()

    "Wasting no time, she held the key and turns the lock."
    $ fade_down_ambience()
    play sound "audio/lock_click.mp3" volume 0.6
    $ renpy.pause(1.0)
    stop sound
    $ fade_up_ambience()
    scene black with fade
    window hide
    
    centered "It opens. Hurriedly, she runs inside the other room and closes the door"

    centered "As soon as does so, she finds that the chains closes itself."

    centered "She heards banging and incessant wailing from the other side"
    window show 

    l "The door is locked here aswell. Maybe the third floor has their doors open."

    l "..."

    l "I should head up now, who knows how long that door can last."

    jump floor2 

label UnityEnding:
    $ fade_down_ambience()
    play music "audio/drown.mp3" fadein 1.5
    $ fade_up_ambience()
    scene black 
    show UnifiedLea
    with fade
    with vpunch
    $ persistent.endings["UnityEnding"] = True 
    
    window hide 
    $ fade_down_ambience()
    play sound "audio/wet_squelch.mp3" volume 0.6
    centered "Lea struggles to break free."   

    centered "It's futile, the ooze, the multiple arms grabbing into her."  

    centered "She slowly watches in horror as everything slowly falls into a gooey sight."  
    window show 
    $ fade_up_ambience()
    if persistent.endings["UnityEnding"] == False: 
        unk "Finally..." 

        unk "We caught up..."

        unk "Together Lea."

        unk "We stay together."
    else:
        u "Finally..."

        u "We caught up..."

        u "Together Lea."

        u "We stay together."
    window hide
    if persistent.endings["endingAchieved"] == False:
        $ persistent.endings["endingAchieved"] = True 
        centered "..." 

        centered "Lea is not done yet." 

        centered "She needs to find out."

        centered "She needs to get out." 
    centered "*Unity Ending, Reached.*" 
    scene black with fade
    return 
    

### LEA CLASSROOM 

label returnToClassroom:
    scene Classroom1
    with fade
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3" 
    $ fade_up_ambience()
    if floor1["LeaClassroom"]["insideClassRoom"] == True:
        "..."
    else:
        $ fade_down_ambience()
        play sound "audio/door_open.mp3"
        "Lea enters the classroom. It's the same room she attends every school day."
        stop sound
        $ fade_up_ambience()
        "But it feels like everyone left in a hurry."
        "They've been gone for a while already."

    if floor1["hallway"]["firstHallwayInteraction"] == True:
        menu:
            "search the chairs.":
                $ fade_down_ambience()
                play sound "audio/chair_scrape.mp3" fadein 1.0 
                scene black
                with fade
                jump chairsLeaClassroom
                stop sound fadeout 2
                $ fade_up_ambience()
            "search the teacher's desk.":
                $ fade_down_ambience()
                play sound "audio/teacher_desk.mp3" fadein 1.0 
                scene black
                with fade
                jump teachersDeskLeaClassroom
                stop sound fadeout 2
                $ fade_up_ambience()
            "head back to the hallway.":
                $ floor1["LeaClassroom"]["insideClassRoom"] = False
                $ fade_down_ambience()
                play sound "audio/walking_heels_echo.mp3" volume 0.5
                scene black
                with fade
                jump hallwayFloor1
                stop sound fadeout 2.0
                $ fade_up_ambience()
    else:
        menu:
            "Head out, head towards the water fountain.":
                scene black
                with fade
                if floor1["waterFountain"]["waterFountainInteracted"] == True:
                    $ fade_down_ambience()
                    play sound "audio/walking_heels_echo.mp3" volume 0.5
                    "Lea returns to the water fountain."
                    jump waterFountainInteracted
                    stop sound fadeout 2.0
                    $ fade_up_ambience()
                elif floor1["waterFountain"]["secondInteraction"] == True:
                    $ fade_down_ambience()
                    play sound "audio/walking_heels_echo.mp3" volume 0.5
                    "Lea returns to the water fountain."
                    stop sound fadeout 2.0
                    $ fade_up_ambience()
                    jump waterFountain3rd
                elif floor1["waterFountain"]["FirstInteraction"] == True:
                    jump waterFountain2nd
                else:
                    jump waterFountain1st
            "Head out to the hallway.":
                $ fade_down_ambience()
                play sound "audio/walking_heels_echo.mp3" volume 0.5
                $ floor1["LeaClassroom"]["insideClassRoom"] = False
                scene black
                with fade
                jump hallway1st
                stop sound fadeout 2
                $ fade_up_ambience()
label chairsLeaClassroom:
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    scene black 
    with fade 
    $ floor1["LeaClassroom"]["insideClassRoom"] = True
    $ fade_down_ambience()
    play sound "audio/chair_scrape.mp3" volume 0.5
    "Checking each chair, she spends her time looking for anything useful here."
    stop sound
    $ fade_up_ambience()
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
        $ fade_down_ambience()
        l "A note from a journal?"
        play sound "audio/paper_rustle.mp3" volume 0.5
        "She reads the content, it gives her a chill down her spine."
        stop sound
        $ fade_up_ambience()
        show lea surprised at right
        with dissolve
        if floor1["puzzlePieces"]["isNoteObtained"] == False:
            l "this is mine... How did this get here?"

            "*Obtained Note #3*"
            $ floor1["puzzlePieces"]["isNoteObtained"] = True
        else:
            show lea scared at right 
            with dissolve
            l "This is not funny..."

            l "Why is a ripped page of my journal in this room?"
            $ fade_down_ambience()
            play sound "audio/paper_rustle.mp3" volume 0.5
            "*Obtained Note #3*"
            stop sound
            $ fade_up_ambience()
        $ counters["floor1"]["noteCount"] += 1
        $ floor1["puzzlePieces"]["Note3"] = True

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
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    $ floor1["LeaClassroom"]["insideClassRoom"] = True
    $ fade_down_ambience()
    "Walking to the teacher's desk, the desk itself was empty, but Lea pulls the drawer open."
    play sound "audio/paper_rustle.mp3" volume 0.5
    show lea default at right 
    with dissolve
    stop sound
    $ fade_up_ambience()
    $ fade_down_ambience()
    l "A rubik's cube? It's jumbled, someone must've confiscated it."

    show lea smiling at right 
    with dissolve

    "Lea turns the cube a few times."
    play sound "audio/cube.mp3" volume 0.5
    $ fade_up_ambience()
    l "That's a nice distraction."
    
    jump returnToClassroom

### ROOM 2 CLASSROOM 

label ClassroomFloor1Room2:
    scene Classroom1 with fade
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    if floor1["Room2"]["isRoomFound"]== False:
        $ fade_down_ambience()
        "Lea heads to the right side, twisting the knobs of each of the rooms."
        play sound "audio/locked_door.mp3" volume 0.5
        "Locked."
        stop sound fadeout 2.0
        play sound "audio/locked_door.mp3" volume 0.5
        "Locked."
        stop sound fadeout 2.0
        play sound "audio/locked_door.mp3" volume 0.5
        "Locked."
        stop sound fadeout 2.0
        play sound "audio/door_open.mp3" volume 0.5
        "One creaks open, the room is available."
        stop sound fadeout 2.0
        $ fade_up_ambience()
    $ floor1["Room2"]["isRoomFound"]= True

    if floor1["Room2"]["insideClassRoom"] == False:
        $ fade_down_ambience()
        play sound "audio/walking_heels_echo.mp3" volume 1
        "She carefully walks inside the door, no one was there to greet her. The chairs are tilted in such a way that it seemed like everyone left in a panic."
        stop sound
        $ fade_up_ambience() 
    else:
        "..."

    menu:
        "Search the chairs.":
            $ fade_down_ambience()
            play sound "audio/chair_scrape.mp3" volume 1
            scene black 
            with fade
            stop sound
            jump chairsRoom2 
            $ fade_up_ambience() 
        "Search the whiteboard":
            $ fade_down_ambience()
            play sound "audio/drawer.mp3" volume 1
            scene black 
            with fade
            stop sound
            jump whiteboardRoom2
            $ fade_up_ambience() 
        "Head back to the hallways":
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1
            $ floor1["Room2"]["insideClassRoom"] = False
            scene black
            with fade
            stop sound
            jump hallwayFloor1
            $ fade_up_ambience() 

label chairsRoom2:
    scene black with fade
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    $ floor1["Room2"]["insideClassRoom"] = True
    $ fade_down_ambience()
    play sound "audio/chair_scrape.mp3" volume 1
    "Checking each chair, she spends her time looking for anything useful here."
    stop sound fadeout 2.0
    $ fade_up_ambience()
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
        if floor1["puzzlePieces"]["isNoteObtained"] == False:
            $ fade_down_ambience()
            play sound "audio/paper_rustle.mp3" volume 1
            l "Its a note, and it looks like it's ripped from a journal."
            stop sound 
            $ fade_up_ambience()
            "Lea reads the contents of the note."
            show lea surprised at right
            with dissolve
            l "Why is this note in this room?"
            $ floor1["puzzlePieces"]["isNoteObtained"] = True
            $ fade_down_ambience()
            play sound "audio/paper_rustle.mp3" volume 1
            "*Obtained Note #1*"
            stop sound 
            $ fade_up_ambience()
        else:
            $ fade_down_ambience()
            play sound "audio/paper_rustle.mp3" volume 1
            l "It looks like I found a note."
            stop sound 
            $ fade_up_ambience()
            show lea surprised at right
            with dissolve
            l "..."
            show lea worried at right 
            with dissolve
            "Another note from my journal, how did this get her in the first place?"
            $ fade_down_ambience()
            play sound "audio/paper_rustle.mp3" volume 1
            "*Obtained Note #1*"
            stop sound 
            $ fade_up_ambience()

        $ counters["floor1"]["noteCount"] += 1
        $ floor1["puzzlePieces"]["Note1"] = True

    else:
        show lea default at right
        with dissolve
        l "I think I already searched the chairs enough."
    
    if floor1["Room2"]["chairChecking"] < 3:
        $ floor1["Room2"]["chairChecking"] += 1

    jump ClassroomFloor1Room2

label whiteboardRoom2:
    scene black with fade 
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    $ floor1["Room2"]["insideClassRoom"] = True
    $ fade_down_ambience()
    play sound "audio/creaking_wood.mp3"
    "Lea approaches the whiteboard,she looks over the crevices."
    stop sound fadeout 2.0
    $ fade_up_ambience()
    "Her head moves to the right, and then left for anything useful there."

    "..."

    show lea default at right 
    with dissolve
    
    l "Markers, Chalks, and an eraser."

    l "Nothing useful here."
    $ fade_down_ambience()
    play sound "audio/walking_heels3.mp3"
    "She walks back to the middle of the room"
    stop sound fadeout 2.0
    $ fade_up_ambience()
    scene black
    with fade  

    jump ClassroomFloor1Room2  

### ROOM 3 CLASSROOM 

label ClassroomFloor1Room3:
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    if floor1["Room3"]["isRoomFound"] == False:
        "Lea heads to the left side, twisting the knobs of each of the rooms."
        $ fade_down_ambience()
        play sound "audio/locked_door.mp3" volume 0.5
        "Locked."
        stop sound fadeout 2.0
        play sound "audio/locked_door.mp3" volume 0.5
        "Locked."
        stop sound fadeout 2.0
        play sound "audio/locked_door.mp3" volume 0.5
        "Locked."
        $ fade_up_ambience()
        play sound "audio/door_open.mp3" volume 0.5
        "One creaks open, the room is available."
        stop sound fadeout 2.0
    $ floor1["Room3"]["isRoomFound"] = True

    if floor1["Room3"]["insideClassRoom"] == False:
        $ fade_down_ambience()
        play sound "audio/walking_heels_echo.mp3" volume 1 
        "She walks inside the classroom. It is just as barren as the halls outside."
        stop sound
        $ fade_up_ambience()
    else:
        "..."

    menu: 
        "Search the chairs.":
            $ fade_down_ambience()
            play sound "audio/chair_scrape.mp3" volume 1
            scene black 
            with fade
            jump chairsRoom3 
            $ fade_up_ambience()
        "Search the whiteboard.":
            $ fade_down_ambience()
            play sound "audio/drawer.mp3" volume 1
            scene black 
            with fade
            jump whiteboardRoom3 
            stop sound fadeout 2.0
            $ fade_up_ambience()
        "Head back to the hallways.":
            $ floor1["Room3"]["insideClassRoom"] = False
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 0.5
            scene black 
            with fade
            jump hallwayFloor1
            stop sound fadeout 2.0
            $ fade_up_ambience()

label chairsRoom3:
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    scene Classroom2
    with fade

    $ floor1["Room3"]["insideClassRoom"] = True
    $ fade_down_ambience()
    play sound "audio/chair_scrape.mp3" volume 1
    "Checking each chair, she spends her time looking for anything useful here."
    stop sound fadeout 2.0
    $ fade_up_ambience()
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
    $ fade_down_ambience()
    play music "audio/classroom_ambience.mp3"
    $ fade_up_ambience()
    scene black with fade

    $ floor1["Room3"]["insideClassRoom"] = True
    $ fade_down_ambience()
    play sound "audio/creaking_wood.mp3"
    "Lea approaches the whiteboard,she looks over the crevices."
    stop sound fadeout 2.0
    $ fade_up_ambience()
    "Her head moves to the right, and then left for anything useful there."

    "..."

    show lea default at right 
    with dissolve

    l "Markers, Chalks, and an eraser."

    show lea surprised at right
    with dissolve 

    l "..."

    hide lea surprised
    with dissolve
    $ fade_down_ambience()
    play sound "audio/paper_rustle.mp3"
    "She picks up a piece of folded paper on the crevice of the whiteboard."
    stop sound
    $ fade_up_ambience()
    "She opens it and reads the contents inside."

    show lea worried at right
    with dissolve
    if floor1["puzzlePieces"]["isNoteObtained"] == False:
        l "... This is from my journal. This is not supposed to be here."
        $ floor1["puzzlePieces"]["isNoteObtained"] = True
        $ fade_down_ambience()
        play sound "audio/paper_rustle.mp3" volume 1
        "*Obtained Note #2*"
        stop sound
        $ fade_up_ambience()
    else:
        l "This note..."

        l "this is also from my journal."

        l "Why are torn pieces of my journal appearing here?"

        $ fade_down_ambience()
        play sound "audio/paper_rustle.mp3" volume 1
        "*Obtained Note #2*"
        stop sound
        $ fade_up_ambience()
    $ counters["floor1"]["noteCount"] += 1
    $ floor1["puzzlePieces"]["Note2"] = True

    jump ClassroomFloor1Room3

### FLOOR 2
### VINCE TO NOT TAMPER FIRST PLEASE

default floor2 = { 
    "hallway" : {
        "isFirstVisit" : True
    },
    "Shatter" : {
        "JumpscareInterval" : [3,5,2,7],
        "Interactions" : 0,
        "isJumpscared" : False
    },
    "laboratories" : {
        "comlab1FirstVisit" : True,
        "comlab2FirstVisit" : True,
        "comlab3FirstVisit" : True
    },
    "vault" : {
        "isFirstInteraction" : True,
        "Attempts" : {
            "Succeed1" : False,
            "Succeed2" : False,
            "Succeed3" : False
        },
        "AnswerKeys" : {
            "Key1" : "55",
            "Key2" : "34",
            "Key3" : "12"
        }
    }
}

define i = 0
define keyAttempt = ""

label floor2:
    $ fade_down_ambience()
    play music "audio/floor2.mp3"
    $ fade_up_ambience()
    label hallwayCutscene:
        if isDemo == True:
            "Demo End"
            return 

        scene hallway2ndFloor with fade 

        if counters["floor1"]["noteCount"] == 3:
            show lea default at right 
            with dissolve
            l "Im glad, those journal entries came in handy."

            l "I better keep my eyes peeled for this point onward."
        elif counters["floor1"]["noteCount"] == 0:
            show lea worried at right 
            with dissolve
            l "I got lucky there."

            l "What am I even supposed to do there?"
        else:
            show lea surprised at right
            with dissolve
            l "So that's what those notes are for."

            l "I should've searched more."
        hide lea with fade

        "Lea explores the floor, its the floor full of computer laboratories."
        $ fade_down_ambience()
        play sound "audio/walking_heels_echo.mp3" 
        "As she walks, she was greeted with rows upon rows of computers."
        stop sound
        $ fade_up_ambience()
        "Some, open. Most, Closed."

        "She turns to the other end of the hallway."

        scene hallwayLocked with fade 

        show lea default at right 
        with dissolve

        l "Just as I thought."

        "She's greeted to another locked door."

        l "It's also locked."

        show lea scared at right 
        with dissolve
        $ fade_down_ambience()
        "Just then, Lea feels like something is staring at her from behind."

        "She may not be alone here after all..."
        $ fade_up_ambience()
    label hallway2:
        $ fade_down_ambience()
        play music "audio/church_bells_thingy.mp3"
        $ fade_up_ambience()
        if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
            scene HallwayStalking
        else:
            scene hallway2ndFloor
        if floor2["hallway"]["isFirstVisit"]:
            $ floor2["hallway"]["isFirstVisit"] = False
            $ fade_down_ambience()
            play sound "audio/walking_heels_echo.mp3" volume 1
            "Being in the hallway, Lea begins her search."
            stop sound
            "The air is tense, its silent."

            "But someone's already been here."

            "Multiple times."
            if persistent.endings["UnityEnding"]:
                "Unlike Unity, whatever is up here is already loose."

                "Waiting for Lea to drop her guard"
            else:
                
                "Unlike whatever was down there, what's in this floor is already loose."

                "It stalks Lea, waiting."

                "It wants her guard down."
        else:
            if counters["floor2"]["Sanity"] == 5:
                "Lea stands between the hallway."

                "She feels its eyes, watching her."

                "She is determined to see this through"
            elif counters["floor2"]["Sanity"] >= 3:
                "Lea stands between the hallway."

                "She feels its eyes, watching her."

                "Doubts starts to set into her mind."
                play sound "audio/girl_laugh.mp3" volume 0.5
                "Was she actually capable to escape the first floor?"

                "Or was it just a stroke of luck?"

                "Doubts aside, she continues on."
            elif counters["floor2"]["Sanity"] >= 1:
                "Lea stands between the hallway."
                
                play sound "audio/girl_laugh.mp3" volume 0.5
                "It's stalking her, They're enjoying this."
                stop sound
                "She couldn't do this."

                "She has never been capable."

                "This is the end of her."
            
            else:
                play sound "audio/stumble.mp3" volume 1
                "Lea's legs felt weak, she falls to the ground."
                stop sound
                $ fade_up_ambience()
                jump ShatterEnding 

        $ fade_down_ambience()
        play music "audio/church_bells_thingy.mp3"
        $ fade_up_ambience()
        menu:
            "Look at the nearby vault.":
                scene black with fade 
                jump vault 
            "Look at the computer labs.":
                menu:
                    "Head to the first 3":
                        scene black with fade 
                        jump comlab1
                    "Head to the middle":
                        scene black with fade 
                        jump comlab2
                    "Look at the last batch":
                        scene black with fade 
                        jump comlab3
            "Calm Lea's resolve." if floor2['Shatter']['isJumpscared']:
                scene black with fade 
                "Lea takes her time."

                "She breathes in."

                "She breathes out."
                if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
                    $ i += 1
                    $ floor2["Shatter"]["Interactions"] = 0

                    "Lea feels that the eyes watching her are starting to dissapate."
                elif counters["floor2"]["Sanity"] == 5:
                    $ counters["floor2"]["Sanity"] -= 1 
                    if persistent.endings["FalseIdolEnding"]:
                        st"... That will not work on me.{nw}"
                    else:
                        unk"... That will not work on me.{nw}"
                    jump jumpscare
                elif counters["floor2"]["Sanity"] == 4:
                    "Lea nods, the urge for her to see this through stregthens."

                    $ counters["floor2"]["Sanity"] += 1
                else:
                    "Lea tries to give herself positive thoughts."
                    
                    "she knows she needs to get out of here."

                    $ counters["floor2"]["Sanity"] += 2
                jump hallway2

    label ShatterEnding:
        $ fade_down_ambience()
        play music "audio/dark_ambience.mp3" volume 1 
        $ persistent.endings["FalseIdolEnding"] = True
        scene black with fade 
        show ShatteredLea 
        window hide
        $ fade_up_ambience()
        centered "Lea feels hopeless."

        centered "She feels like she will never escape here."

        centered "She's trapped."

        centered "The days of pretending to be a studious student caught up to her."
        $ fade_down_ambience()
        window show 
        if persistent.endings["FalseIdolEnding"]:
            st "A disgrace."

            st "You don't deserve your merit."

            st "Come."

            st "You will break as I would."
        else:
            unk "A disgrace."

            unk "You don't deserve your merit."

            unk "Come."

            unk "You will break as I would."
        $ fade_up_ambience()
        window hide
        if persistent.endings["endingAchieved"] == False:
            $ fade_down_ambience()
            $ persistent.endings["endingAchieved"] = True
            centered "..." 

            centered "Lea is not done yet." 

            centered "She needs to find out."

            centered "She needs to get out." 
        $ persistent.endings["FalseIdolEnding"] = True
        $ fade_up_ambience()
        centered "*Shattered Ending, Reached.*" 
        scene black with fade
        return

### VAULT
    
    label vault:
        scene vault with fade
        if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
            jump jumpscare 
        else:
            $ floor2["Shatter"]["Interactions"] += 1

        if floor2["vault"]["isFirstInteraction"]:
            $ floor2["vault"]["isFirstInteraction"] = False
            "Lea approaches the abandoned safe nearby the locked door."

            "She looks around for anything useful."

            "Above the safe was something that caught her eye"

            show lea default at right 
            with dissolve

            l "A plaque?"

            "There are a bunch of numbers on it"

            $ _history = False

            """
            12,32,36,55,29,86,45,19\n
            45,34,65,76,23,54,78,98\n
            75,45,67,66,23,34,12,76
            """

            $ _history = True

            l "I wonder what that means"
        else:
            "Lea appeaoches the vault, it stays there."

            "Something watches her intently."

            "Much, more intently."
        label vaultChoice:
        menu:
            "Check the plaque.":
                if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
                    jump jumpscare 
                else:
                    $ floor2["Shatter"]["Interactions"] += 1
                "Lea looks above the vault."

                $ _history = False

                """
                12,32,36,55,29,86,45,19\n
                45,34,65,76,23,54,78,98\n
                75,45,67,66,23,34,12,76
                """

                $ _history = True

                l "I wonder what that means."
                
                jump vaultChoice 
            "Attempt to open the vault.":
                scene black with fade 
                jump vaultAttempt
            "Leave, back to the hallway.":
                scene black with fade 
                jump hallway2

    label vaultAttempt:
        scene vault with fade
        $ fade_down_ambience()
        play music "audio/hallway_tension2.mp3" volume 1 
        $ fade_up_ambience()
        "Lea leans over to the lock and starts twistnig the lock"
        label insertAttempt:
            menu:
                "try opening the lock.":
                    $ keyAttempt = renpy.input("Enter key combination: ", "", length=15, exclude=" +=,.?!<>{}[]").strip() or ""
                "look at the vault again.":
                    jump vault

        
        if floor2["vault"]["Attempts"]["Succeed1"] == False:
            if keyAttempt == floor2["vault"]["AnswerKeys"]["Key1"]:
                "The vault makes a ticking sound."

                l "It worked. Next number."
                $ floor2["vault"]["Attempts"]["Succeed1"] = True
                jump insertAttempt
            else:
                jump failedAttempt

        elif floor2["vault"]["Attempts"]["Succeed2"] == False and floor2["vault"]["Attempts"]["Succeed1"] == True:
            if keyAttempt == floor2["vault"]["AnswerKeys"]["Key2"]:
                "The vault makes a ticking sound."

                l "It worked. Off to the last number."
                $ floor2["vault"]["Attempts"]["Succeed2"] = True
                jump insertAttempt
            else:
                jump failedAttempt

        elif floor2["vault"]["Attempts"]["Succeed3"] == False and floor2["vault"]["Attempts"]["Succeed2"] == True:
            if keyAttempt == floor2["vault"]["AnswerKeys"]["Key3"]:
                "The vault makes a ticking sound."

                l "It's Open, Finally."
                $ floor2["vault"]["Attempts"]["Succeed3"] = True
                jump openVault
            else:
                jump failedAttempt
        else:
            jump failedAttempt

        label failedAttempt:
            $ floor2["vault"]["Attempts"]["Succeed3"] = False
            $ floor2["vault"]["Attempts"]["Succeed2"] = False
            $ floor2["vault"]["Attempts"]["Succeed1"] = False

            if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
                jump jumpscare 
            else:
                $ floor2["Shatter"]["Interactions"] += 1
            
            "Lea hears the vault reset"

            show lea default at right 
            with dissolve
            l "Damn it, I have to try again."
            if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i-1]:
                "She feels something... Someone, linger behind her."
            hide lea
            jump insertAttempt
    
    ### ESCAPE CUTSCENE    
    label openVault:
        $ fade_down_ambience()
        play music "audio/ambient_silence.mp3" volume 1 fadein 1.0
        $ fade_up_ambience()
        scene vault with fade
        $ fade_down_ambience()
        "Lea turns the knob open and checks the content."
        play sound "audio/vault.mp3" volume 1 fadein 1.0
        
        "For such a big vault, there is only one item inside."
        stop sound fadeout 2.0
        l "The key."

        "Lea takes a hold of it and walks towards the locked door."
        play sound "audio/waling_heels_echo.mp3" volume 1 fadein 1.0
        scene hallwayLocked
        stop sound fadeout 2.0
        
        show lea default at right 
        with fade

        "She looks over to the door, and she wasted no time."

        "She puts the key into the lock and turns."
        play sound "audio/door_open.mp3" volume 1 fadein 1.0
        "The lock goes off, the chains loosens."
        stop sound fadeout 2.0
        "She takes a step into the stairs of the next floor."
        $ fade_up_ambience()
        scene black with fade

        if counters["floor2"]["ComputersVisited"] == 3:
            if persistent.endings["FalseIdolEnding"]:
                st "Pathetic."

                st "You are utterly pathetic."

                st "How much more are you going to play knight?"

                st "You are ruined whether you stay or leave."

                st "It is only a matter of time."

                st "Until people learn who you really are." 
            else:
                unk "Pathetic."

                unk "You are utterly pathetic."

                unk "How much more are you going to play knight?"

                unk "You are ruined whether you stay or leave."

                unk "It is only a matter of time."

                unk "Until people learn who you really are." 
            
            show lea worried at right 
            with dissolve 
        elif counters["floor2"]["ComputersVisited"] >= 1:
            if persistent.endings["FalseIdolEnding"]:
                st "I've seen better."

                st "I have experienced better."

                st "How long will you keep this facade?"

                st "Everyone but you will never know how truly competent you are."

                st "And you're not."
            else:
                unk "I've seen better."

                unk "I have experienced better."

                unk "How long will you keep this facade?"

                unk "Everyone but you will never know how truly competent you are."

                unk "And you're not."
            show lea worried at right 
            with dissolve
        else:
            if persistent.endings["FalseIdolEnding"]:
                st "Impressive."

                st "You managed to finish it all in one gaze."

                st "I may have misjudged you."

                st "You are worthy of your peer's praises."
            else:
                unk "Impressive."

                unk "You managed to finish it all in one gaze."

                unk "I may have misjudged you."

                unk "You are worthy of your peer's praises."
            show lea smiling at right 
            with dissolve
        
        "Lea continues walking towards the door."
        play sound "audio/chain_rattle.mp3" volume 1 fadein 1.0
        "The chains returning as soon as she stepped inside."
        stop sound fadeout 2
        l "One final floor, to the emergency exit outside."

        scene black with fade
        jump floor3 
                

        


### LABORATORY

    label comlab1:
        scene black with fade
        $ fade_down_ambience()
        play music "audio/ambient_silence.mp3" volume 1 fadein 1.0
        $ fade_up_ambience()
        if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
            jump jumpscare 
        else:
            $ floor2["Shatter"]["Interactions"] += 1

        if floor2["laboratories"]["comlab1FirstVisit"]:
            $ counters["floor2"]["ComputersVisited"] += 1
            "Lea heads towards the set of comlabs."

            "She remembers some of them were turned on."

            "After a bit of searching, she does find it."

            $ fade_down_ambience()
            play sound "audio/computer_flick.mp3" volume 1 fadein 1.0
            "The lone flickering computer in a flurry of dead desktops."
            $ fade_up_ambience()
            stop sound fadeout 2.0
        else:
            "She heads towards the nearest computer."

            "It's on, displaying something"
        $ fade_down_ambience()
        play sound "audio/lightbulb_buzzing.mp3" volume 1 fadein 1.0
        "It's buzzing."
        stop sound fadeout 2.0
        $ fade_up_ambience()
        $ _history = False

        "7."

        "7."

        "7."

        $ _history = True

        show lea default at right 
        
        l "I wonder what those mean"

        menu:
            "Return.":
                scene black with fade 
                jump hallway2 

    label comlab2:
        scene black with fade
        $ fade_down_ambience()
        play music "audio/ambient_silence.mp3" volume 1 fadein 1.0
        $ fade_up_ambience()
        if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
            jump jumpscare 
        else:
            $ floor2["Shatter"]["Interactions"] += 1

        if floor2["laboratories"]["comlab2FirstVisit"]:
            $ counters["floor2"]["ComputersVisited"] += 1
            "Lea heads towards the set of comlabs."

            "She remembers some of them were turned on."

            "After a bit of searching, she does find it."

            $ fade_down_ambience()
            play sound "audio/computer_flick.mp3" volume 1 fadein 1.0
            "The lone flickering computer in a flurry of dead desktops."
            stop sound fadeout 2.0
        else:
            "The"
        $ fade_down_ambience()
        play sound "audio/lightbulb_buzzing.mp3" volume 1 fadein 1.0
        "It's buzzing."
        stop sound fadeout 2.0

        $ _history = False

        "4."

        $ _history = True

        show lea default at right 
        
        l "I wonder what those mean"

        menu:
            "Return.":
                scene black with fade 
                jump hallway2 

    label comlab3:
        scene black with fade
        $ fade_down_ambience()
        play music "audio/ambient_silence.mp3" volume 1 fadein 1.0
        $ fade_up_ambience()
        if floor2["Shatter"]["Interactions"] == floor2["Shatter"]["JumpscareInterval"][i]:
            jump jumpscare 
        else:
            $ floor2["Shatter"]["Interactions"] += 1

        if floor2["laboratories"]["comlab3FirstVisit"]:
            $ counters["floor2"]["ComputersVisited"] += 1
            "Lea heads towards the set of comlabs."

            "She remembers some of them were turned on."

            "After a bit of searching, she does find it."
            $ fade_down_ambience()
            play sound "audio/computer_flick.mp3" volume 1 fadein 1.0
            "The lone flickering computer in a flurry of dead desktops."
            stop sound fadeout 2.0
        else:
            "Lea walks to the furthest desktop in the hallway."

            "she puts her head towards the transparent window"
        $ fade_down_ambience()
        play sound "audio/lightbulb_buzzing.mp3" volume 1 fadein 1.0
        "It's buzzing."
        stop sound fadeout 2.0

        $ _history = False

        "2."
        
        "2."

        $ _history = True

        show lea default at right 

        l "I wonder what those mean"

        menu:
            "Return.":
                scene black with fade 
                jump hallway2  

    label jumpscare:
        scene black 
        show notLea
        play sound "audio/jumpscare_sting.mp3" 
        if i == 3:
            $ i = 0
        else:
            $ i += 1
        
        $ floor2["Shatter"]["Interactions"] = 0
        $ counters["floor2"]["Sanity"] -= 1
        $ floor2["Shatter"]["isJumpscared"] = True 


        $ renpy.pause(1)

        scene hallway2ndFloor 
        show lea scared at right 
        with vpunch
        "Lea is back at the hallway."

        "Her heart pumping."

        "Seeds of doubt starts to sow inside her."
        jump hallway2 

### FLOOR 3 

define floor3 = {
    "library" : {
        "isFirstInteraction" : True, 
        "isInsideLibrary" : False
    },
    "conditon": {
        "hasLeaLost" : False,
        "hasLeaWon" : False
    },
    
    "notes" : {
        "notesSeen" : 0,
        "sources" : {
            "tech": False,
            "history": False
        }
    }
} 

label floor3:
    ### CUTSCENE 
    scene hallway3rdFloor with fade 
    "Lea makes her way towards the third floor."

    "The rooms are dim and silent as always."

    "Although, something was greeting her in the middle of the hallway."

    "A statue, made of brass. It stands there with her arms outwards. as if she were waiting for an embrace."

    "Lea walks closer."

    scene hallwayInteraction with fade

    "On one of the statue's fingers, was the key. Lea reaches out before she was stopped by a voice."

    show lea surprised at right
    with dissolve
    if persistent.endings["GoldenEnding"]:
        au "Halt, do you seek your way out of here?"

        l "O- Of course I do."

        au "Do you think you are worthy of the outside?"
        show lea worried at right 
        with dissolve
        l "Well..."

        au "Prove it to me."

        au "I see all the minute flaws in you."

        au "Unless you are worthy of this key."

        au "You and I shall be one in the same way."
    else:
        unk "Halt, do you seek your way out of here?"

        l "O- Of course I do."

        unk "Do you think you are worthy of the outside?"
        show lea worried at right 
        with dissolve
        l "Well..."

        unk "Prove it to me."

        unk "I see all the minute flaws in you."

        unk "Unless you are worthy of this key."

        unk "You and I shall be one in the same way."
    
    label hallway3: 
        scene hallway3rdFloor with fade 
        "Lea walks around the hallway, the only unlocked room was the library."
        show lea default at right 
        with dissolve
        l "Suppose everything I need to know is just right at this room."

        "What should lea do?"

        menu: 
            "Enter the libary.":
                jump library 
            "Walk towards the statue.":
                jump statueInteraction
    
    label library:
        scene library with fade
        if floor3["library"]["isFirstInteraction"]:
            $ floor3["library"]["isFirstInteraction"] = False
            "She walks inside the library."
            
            "Illuminated but barren, there are differing books around the area."

            "Since the first floor, no one comes to greet her. Not even a glance to acknowledge her existence."

            "Lea looks around, searching where she could find clues to deem her worth."

            "her eyes are set over one of the tables."
            
            "It's her journal."
            show lea surprised at right 
            with dissolve

            "She made hurried steps towards her jounral."

            "Opening it, multiple pages were ripped off."

            if counters["floor1"]["noteCount"] >= 1:
                "Lea pieced together that some pages that she found on the first floor are also ripped off from here."
            
                "Other than the 3 pages, many more pages were ripped off"
            else:
                "A lot of the pages are ripped off."
            
            l "12 pages... I should hurry up and find them"
        else: 
            if floor3["library"]["isInsideLibrary"]:
                "..."
            else:
                "She steps insie the Library."

                "The clues to her escape lingers around."

                "She should find them, imprint them on her mind."
        
        "What should she do?"
        $ floor3["library"]["isInsideLibrary"] = True 
        menu: 
            "Look for her notes.":
                menu:
                    "Search the maths section.":
                        "looking over a math book, she found 3 torn pages that are located throughout the book"
                        
                        "Lea flips through a note"
                        show note with dissolve
                        menu:
                            "Search note 1.":
                                $ floor3["notes"]["notesSeen"] +=1
                                n "2013."

                                n "I gave my mom a drawing."

                                n "My teacher said it's great!"

                                n "She might appreciate it."

                                n "But mom just left it at the counter."

                                n "And I can't find it anymore the next day."

                                n "I wonder what happened."
                                scene black with fade
                                jump library

                            "Search note 2.":
                                $ floor3["notes"]["notesSeen"] +=1
                                n "2023."

                                n "I saw my friends on a cafe one morning."

                                n "It was the first time in a while that I had free time."

                                n "They were having fun, but they never bothered to invite me."

                                n "Was I a little too distant to them?"

                                n "Is that why they do not really care much anymore?"
                                scene black with fade
                                jump library
                            "Search note 3.":
                                $ floor3["notes"]["notesSeen"] +=1
                                n "2015."

                                n "Someone tried to approach me."

                                n "I wanted to talk to them, but I feel something heavy on my chest."

                                n "I can't put a single word out of my mouth."

                                n "They soon went away after this."
                                scene black with fade
                                jump library

                    "Search the history section":
                        "Lea looks over to a nearby history book."

                        "One of the note is stuck and neatly folded."

                        "She picks it up"
                        show note with dissolve
                        menu:
                            "Read note.":
                                $ floor3["notes"]["notesSeen"] +=1
                                n "2019."

                                n "I think they haven't noticed."

                                n "I slipped up on an exam."

                                n "But their eyes are on to me."

                                n "I'm a fraud, but I can not afford to let them know about it."

                                n "This score, no one should know about this."

                                n "I am glad it is easier to hide it at this day."

                                n "I don't think I learnt a thing for the past months..."
                                scene black with fade
                                jump library
                    "Search the technologies section":
                        "Lea finds a slightly opened programming 1 book."

                        "Inside contained 3 notes."
                        show note with dissolve
                        menu:
                            "Search note 1.":
                                $ floor3["notes"]["notesSeen"] +=1
                                n "I have to be ahead."

                                n "I have to be!"

                                n "I spent so many days studying in advance that no one noticed."

                                n "They think I was smart."

                                n "Im not."

                                n "If I don't learn the material days... weeks... in advance..."

                                n "They'll see how unknowledgable I am."
                                scene black with fade
                                jump library
                            "Search note 2.":
                                $ floor3["notes"]["notesSeen"] +=1
                                n "This..."

                                n "This..."

                                n "What the HELL is this?!"

                                n "Needing to use a function in another function?"

                                n "What?"

                                n "God... I feel so worthless."

                                n "If I don't manage to understand this I'm doomed."
                                scene black with fade
                                jump library
                            "Search note 3.":
                                $ floor3["notes"]["notesSeen"] +=1
                                n "Im stumped."

                                n "I can't work on this project for long."

                                n "My body's tired."

                                n "I haven't had proper sleep in days."

                                n "But I need to continue going."

                                n "They might make fun of me if this turns out lucklaster."
                                scene black with fade
                                jump library
            "Look for other materials":
                menu:
                    "Look at the history books":
                        $ floor3["notes"]["sources"]["history"] = True
                        "Lea approached a history book on the table and started to flip pages."
                        
                        "She found a news paper clipping hidden within the thick book."

                        "an infectious disease caused by the SARS-CoV-2 virus has spread around the recent areas."
                        
                        "Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment."
                        
                        "However, some will become seriously ill and require medical attention."
                        scene black with fade 
                        jump library 
                    "Look at the Object Oriented Programming Book":
                        $ floor3["notes"]["sources"]["tech"] = True
                        "Lea looks over to a programming book located at one of the tables at the edge."

                        "Approaching it, she notices a bookmark placed on one of the pages."

                        "Function: A function is a self contained block of code designed to perform a specific task, often taking inputs and producing an output."
                        
                        "Recursion: Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem."
                        
                        "Parameter: A parameter is a variable defined in a function's definition that acts as a placeholder for the values the function will receive as input."

                        show lea worried at right 
                        l "That's a lengthy read."

                        scene black with fade
                        jump library 
            "Head outside":
                $ floor3["library"]["isInsideLibrary"] = False
                "Lea walks outside the libary, the sounds of wooden flooring transitioning to stone."
                scene black with fade 
                jump hallway3

    label statueInteraction:
        scene hallwayInteraction with fade

        if persistent.endings["GoldenEnding"]:
            au "What is it that you seek?"
        else:
            unk "What is it that you seek?"
        
        show lea default at right 
        with dissolve 
        menu:
            
            "The key.":
                l "I want the key to the outside."

                if persistent.endings["GoldenEnding"]:
                    au "do you think that you are worthy of this?"
                else:
                    unk "do you think that you are worthy of this?"
                
                menu:
                    "I wish to prove it.":
                        l "I will prove myself for it."

                        if persistent.endings["GoldenEnding"]:
                            au "Very well, we shall commence at once."
                        else:
                            unk "Very well, we shall commence at once."
                        scene black with fade
                        jump questioning
                    "Give me time.":
                        l "Give me a few more moments."

                        if persistent.endings["GoldenEnding"]:
                            au "I shall wait."
                        else:
                            unk "I shall wait."
                        scene black with fade
                        jump hallway3

            "Your terms.":
                show lea default at right
                with dissolve
                l "I need you to tell me what I need to do to get that key."

                if persistent.endings["GoldenEnding"]:
                    au "The terms are simple, a guessing game."
                else:
                    unk "The terms are simple, a guessing game."

                l "A guessing game?"

                if persistent.endings["GoldenEnding"]:
                    au "Indeed."

                    au "Though you have one chance and only that chance."

                    au "The questions are limited to only three."

                    au "I reserve the right to shape you into your perfect self."

                    au "If you fail to deem yourself worthy."
                else:
                    unk "Indeed."

                    unk "Though you have one chance and only that chance."

                    unk "The questions are limited to only three."

                    unk "I reserve the right to shape you into your perfect self."

                    unk "If you fail to deem yourself worthy."
                show lea worried at right 
                with dissolve

                l "I better continue gathering information then."

                if persistent.endings["GoldenEnding"]:
                    au "Make haste."
                else:
                    unk "Make haste."
                
                scene black with fade 
                jump hallway3

                
            "Nothing.":
                l "Nothing at the moment."

                if persistent.endings["GoldenEnding"]:
                    au "Time is off the essence."
                else:
                    unk "Time is off the essence."
                
                scene black with fade
                jump hallway3
            
    label questioning:
        scene hallwayInteraction with fade 
        $ config.has_autosave = False
        $ _game_menu_screen = None
        $ quick_menu = False
        if persistent.endings["GoldenEnding"]:
            au "This shall be a trial between you and I."

            au "Do not manipulate your memories with such petty actions."

            au "..."

            au "I shall begin."

            au "The year you ignored someone's attempt to be your peer."
            
            au "Subtract it to the year your mother lost your drawing." 
            
            au "Remember this result."

            au "The year you are born is 2005. Subtract it to the year your friends did not bother to invite you for an outing."

            au "Add both of those results."

            au "What do you get."
        else:
            unk "This shall be a trial between you and I."

            unk "Do not manipulate your memories with such petty actions."

            unk "..."

            unk "I shall begin."

            unk "The year you ignored someone's attempt to be your peer."
            
            unk "Subtract it to the year your mother lost your drawing." 
            
            unk "Remember this result."

            unk "The year you are born is 2005. Subtract it to the year your friends did not bother to invite you for an outing."

            unk "Add both of those results."

            unk "What do you get."
        menu: 
            "20.":

                if persistent.endings["GoldenEnding"]:
                    au "Impressive. For basic arithmetic."
                else:
                    unk "Impressive. For basic arithmetic."

                jump question2

            "22.":

                if floor3["conditon"]["hasLeaLost"]:

                    if persistent.endings["GoldenEnding"]:
                        au "Do not resist this Lea."
                    else:
                        unk "Do not resist this Lea."
                else:
                    $ floor3["conditon"]["hasLeaLost"] = True

                    if persistent.endings["GoldenEnding"]:
                        au "Incorrect. Losing this early is unfortunate Lea."
                    else:
                        unk "Incorrect. Losing this early is unfortunate Lea."
                scene black with fade
                jump leaGolden

            "18.":

                if floor3["conditon"]["hasLeaLost"]:

                    if persistent.endings["GoldenEnding"]:
                        au "Do not resist this Lea."
                    else:
                        unk "Do not resist this Lea."

                else:

                    $ floor3["conditon"]["hasLeaLost"] = True

                    if persistent.endings["GoldenEnding"]:
                        au "Incorrect. Losing this early is unfortunate Lea."
                    else:
                        unk "Incorrect. Losing this early is unfortunate Lea."
                scene black with fade
                jump leaGolden

        label question2:
            if persistent.endings["GoldenEnding"]:
                au "We proceed."

                au "The year you slipped on your exams."

                au "What is the major event that prevented everyone from easily seeing your grades?"
            else:
                unk "We proceed."

                unk "The year you slipped on your exams."

                unk "What is the major event that prevented everyone from easily seeing your grades?"

            menu:
                "A storm.":
                    if floor3["conditon"]["hasLeaLost"]:

                        if persistent.endings["GoldenEnding"]:
                            au "Do not resist this Lea."
                        else:
                            unk "Do not resist this Lea."

                    else:

                        $ floor3["conditon"]["hasLeaLost"] = True

                        if persistent.endings["GoldenEnding"]:
                            au "Incorrect. You have had a good run, Lea."
                        else:
                            unk "Incorrect. You have had a good run, Lea."
                    scene black with fade                    
                    jump leaGolden


                "A pandemic.":
                    if persistent.endings["GoldenEnding"]:
                        au "Perhaps you are more capable than you think you are."
                    else:
                        unk "Perhaps you are more capable than you think you are."
                    
                    jump question3


                "A major outage.":
                    if floor3["conditon"]["hasLeaLost"]:

                        if persistent.endings["GoldenEnding"]:
                            au "Do not resist this Lea."
                        else:
                            unk "Do not resist this Lea."

                    else:

                        $ floor3["conditon"]["hasLeaLost"] = True

                        if persistent.endings["GoldenEnding"]:
                            au "Incorrect. You have had a good run, Lea."
                        else:
                            unk "Incorrect. You have had a good run, Lea."
                    scene black with fade                    
                    jump leaGolden
        
        label question3:
            "Now, comes my final question."

            "You toil yourself studying for a long time."

            "Yet this specific sub-subject has given you a hard time."

            "Can you recall it?"

            menu:
                "It's the function.":
                    if floor3["conditon"]["hasLeaLost"]:

                        if persistent.endings["GoldenEnding"]:
                            au "Do not resist this Lea."
                        else:
                            unk "Do not resist this Lea."

                    else:

                        $ floor3["conditon"]["hasLeaLost"] = True

                        if persistent.endings["GoldenEnding"]:
                            au "Incorrect. You have had a good run, Lea."
                        else:
                            unk "Incorrect. You have had a good run, Lea."
                    
                    scene black with fade
                    jump leaGolden

                "It's the parameters.":
                    if floor3["conditon"]["hasLeaLost"]:

                        if persistent.endings["GoldenEnding"]:
                            au "Do not resist this Lea."
                        else:
                            unk "Do not resist this Lea."

                    else:

                        $ floor3["conditon"]["hasLeaLost"] = True

                        if persistent.endings["GoldenEnding"]:
                            au "Incorrect. You have had a good run, Lea."
                        else:
                            unk "Incorrect. You have had a good run, Lea."
                    
                    scene black with fade
                    jump leaGolden

                "It's the recursion.":
                    if persistent.endings["GoldenEnding"]:
                        au "You have done well Lea."
                    else:
                        unk "You have done well Lea."
                    
                    "*You obtained a door key.*"

                    show lea surprised at right 
                    with dissolve

                    l "It's... Over?"
                    if floor3["notes"]["notesSeen"] >= 4 and floor3["notes"]["sources"]["tech"] and floor3["notes"]["sources"]["history"]:
                        if persistent.endings["GoldenEnding"]:
                            au "You have passed, return home."
                        else:
                            unk "You have passed, return home."
                    elif floor3["notes"]["notesSeen"] == 0 and floor3["notes"]["sources"]["tech"] == False  and floor3["notes"]["sources"]["history"] == False:
                        if persistent.endings["GoldenEnding"]:
                            au "You have proven your capabilities in a very astonishing way, return home."
                        else:
                            unk "You have proven your capabilities in a very astonishing way, return home."
                    else:
                        if persistent.endings["GoldenEnding"]:
                            au "Your effort are sufficient, return home."
                        else:
                            unk "Your effort are sufficient, return home."
                    show lea smiling at right 
                    with dissolve

                    scene black with fade 
                    jump end
    
label leaGolden:
    $ config.has_autosave = True 
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    window hide
    centered "She had one chance, and she answered wrong."

    centered "She starts to feel her body stiffen."

    centered "The varying colors turning into a monotone gold."

    centered "Slowly, Lea could no longer feel her lower half."

    centered "And soon, her entire body turned into a perfect gold monument."
    window show
    if persistent.endings["GoldenEnding"]:
        au "Brace my gift to you."

        au "Perfection."
    else:
        unk "Brace my gift to you."
        
        unk "Perfection."
    
    if persistent.endings["endingAchieved"] == False:
        $ fade_down_ambience()
        $ persistent.endings["endingAchieved"] = True
        centered "..." 

        centered "Lea is not done yet." 

        centered "She needs to find out."

        centered "She needs to get out." 
    $ persistent.endings["GoldenEnding"] = True

    centered "*Perfected Ending Achieved.*"
    scene black with fade
    return

label end:
    scene hallwayLocked with fade

    "Lea approached the door, the final door."

    "She turns the key and."

    scene white with fade

    l "Finally..."

    "Lea runs outside to the bright light."

    "But she feels her body grow weak."

    "She collapses."
    if persistent.endings['UnityEnding'] and persistent.endings['FalseIdolEnding'] and persistent.endings['GoldenEnding'] and persistent.endings['FalseEnding']:
        scene Hospital1 with fade 
        l "... Ugh."

        l "... What the?"

        "A crash came from the other room as a rolling chair was launched to the wall."

        k "Auntie! Auntie! She's awake!"

        k "Hurry!"

        "A familiar voice rang at the left side of the bed."

        "the voice suddenly followed with one pair of footsteps darting across the room."

        "A door opening and closing shut is heard right after."

        "..."

        "A few minutes later a group of footsteps followed suite."

        "The doors opened and about half a dozen people poured inside."

        scene Hospital2 with fade 

        show lea headHurt at right 
        with dissolve

        l "Wh- What?"

        k "See auntie! She's awake!"

        "Before Lea could process what was happening, she feels the weight of her mother crash into her as she went in for a hug."

        m "Oh dear... What happened to you? We were worried sick!"

        show lea worried at right 
        with dissolve 

        l "What happened? I was at the school... then I felt tired..."

        l "I passed out for a few hours."

        "A woman's voice, about her age cut her off."

        k "You were in a coma."

        k "For a few weeks now."

        l "... what? I- I've missed so much I have to-"

        "Lea tries to stand up, but kate grabbed her by the shoulders and put her back to sitting in the hospital bed"
        show lea surprised at right 
        with dissolve

        k "Please, you've been hospitalized."

        k "Hell, you were in a coma. For WEEKS."

        k "We've distanced ourselves because we thought you'd need the space but..."

        k "Look at you! You need to rest!"

        m "Your friend Kate insisted to be here, I have already written your excuse letter weeks ago."

        m "Let's make up for lost time, shall we?"

        l "..."

        show lea smiling at right 
        with dissolve 

        "Lea nods with a smile on her face"

        "..."

        scene black with fade 
        centered "Fin!"
        
        centered "Thank you for playing Oblivio!"
        $ persistent.endings["TrueEnding"] = True
        scene black with fade 
        return

    else:
        window hide
        scene black with fade

        centered "Fin?"

        if persistent.endings["endingAchieved"] == False:
            $ fade_down_ambience()
            $ persistent.endings["endingAchieved"] = True
            centered "..." 

            centered "Lea is not done yet." 

            centered "She needs to find out."

            centered "She needs to get out." 
        
        centered "..."

        centered "She is still trapped here."
        
        centered "*False Ending Achieved.*"
        window show
        $ persistent.endings["FalseEnding"] = True
    
    scene black with fade
    return



label memoryCheck:
    scene black with fade 
    if persistent.endings['UnityEnding'] or persistent.endings['FalseIdolEnding']:
        menu: 
            "Learn what happened in the bathroom." if persistent.endings['UnityEnding'] == True:
                jump memoryBathroom
            "Learn what happened during midterms." if persistent.endings['FalseIdolEnding'] == True:
                jump memoryMidterm
            "next page." if persistent.endings['UnityEnding'] or persistent.endings['FalseIdolEnding'] == True:
                jump memoryNext
    
    label memoryNext:
        if persistent.endings['GoldenEnding'] or persistent.endings['FalseEnding'] == True:
            menu:
                "Learn what happened at her room." if persistent.endings['GoldenEnding'] == True:
                    jump memoryRoom
                "Learn what happened at home." if persistent.endings['FalseEnding'] == True:
                    jump memoryHome
                "Head back.":
                    jump gameStart
        else:
            jump memoryCheck

label memoryBathroom:
    "Flavor."
label memoryMidterm:
    "Flavor."
label memoryRoom:
    "Flavor."
label memoryHome:
    "Flavor."