# Character
define l = Character("Lea", color="#910b7f")

default floor1 = {
    "waterFountain" : {
        "FirstInteraction" : False, 
        "SWatFounInteraction" : False,
        "waterFountainInteracted" : False,
        "doorKeyObtained" : False
    },
    #CLASSROOMS

    "LeaClassroom" : {
        "chairChecking" : 0,
        "classroomFirstInteracted" : False,
        "insideClassRoom" : False,
        "fromInsideClassroom" : False
    },

    "Room2" : {
        "chairChecking" : 0,
        "insideClassRoom" : False,
        "isRoomFonund" : False
    },

    "Room3" : {
        "chairChecking" : 0,
        "insideClassRoom" : False,
        "isRoomFonund" : False
    },
    #HALLWAYS
    "hallway" : {
        "firstHallwayInteraction" : False
    },
    "puzzlePieces" : {
        "Note1" : False,
        "Note2" : False,
        "Note3" : False
    }
}

default floor2 = {

}

label start:

    # Background ambience for night (ambience channel)
   
    scene chairZoomed
    play music "audio/night_ambience.mp3" fadein 2.0 volume 0.4
    $ renpy.music.set_volume(1.0, channel="music")  # full volume to start
    $ renpy.music.set_volume(0.2, delay=15.0, channel="music")  # slow fade over time
    with fade 
    "Lea woke up from her nap, her hair a mess from the deep sleep she had been in."

    scene chairUnzoomed
    with dissolve

    play sound "lightbulb_buzzing.mp3" volume 0.5

    "There was nothing but the faint glow of moonlight and the weak neon light from the exit signs illuminating the hallways."

    show lea default at right
    with dissolve 

    l "God... What time is it?"
    
    play sound "phone_click.mp3" volume 0.5
    $ renpy.pause(0.2)
    
    "Lady Luck wasn't on her side today, her phone was dead."

    l "I must've slept for a long... long time."
    
    play sound "stumble.mp3" volume 0.5
    
    "She stood up and stumbled, catching herself on something nearby."

    l "Right, I skipped lunch earlier."

    "She held her temples."

    l "I need to get something to drink."
    
    menu:
        "Use the water fountain.": 
            play sound "audio/walking_heels_echo.mp3" volume 0.5 fadeout 1.5
            $ renpy.pause(7.0)
            stop sound
            # water fountain sound cue
            #play sound "audio/water_fountain.mp3" volume 0.3
            #$ renpy.pause(0.2)
            scene black 
            with fade
            jump waterFountain1st

        "Ignore your instincts, stay in the classroom.": 
            play sound "audio/door_open.mp3" volume 0.5
            scene black
            with fade
            $ floor1["LeaClassroom"]["fromInsideClassroom"] = True
            jump returnToClassroom1st

# CLASSROOM INTERACTIONS

label returnToClassroom1st:
    scene classRoom
    with fade

    if floor1["LeaClassroom"]["fromInsideClassroom"] == True:
        "Lea prepared to pack her belongings. The window outside showed a dark and cloudy night sky. Her brows furrowed."
    else:
        "Returning to the classroom she lounged by, Lea prepared to pack her belongings. The window outside showed a dark and cloudy night sky. Her brows furrowed." 

    show lea default at right
    with fade 

    l "It's not like anyone will be suspicious of me being out at night, but..."
    play sound "audio/sigh.mp3" volume 0.5
    $ renpy.pause(0.2)
    "She sighed."
    
    l "I just really want to get home. My head is killing me."
    $ floor1["LeaClassroom"]["classroomFirstInteracted"] = True

    # small ambient note (door open effect then footsteps)
    play sound "audio/door_open.mp3"
    play sound "audio/footsteps_heels.mp3"
    $ renpy.pause(1.0)

    menu:
        "Head out, drink at the water fountain.":
            play sound "audio/walking_heels_echo.mp3" volume 0.5 fadeout 1.5
            $ renpy.pause(7.0)
            stop sound
            scene black
            with fade
            if floor1["waterFountain"]["waterFountainInteracted"] == True:
                "Lea returns to the water fountain."
                jump waterFountainInteracted
            elif floor1["waterFountain"]["SsecondInteraction"] == True:
                "Lea returns to the water fountain."
                jump waterFountain3rd
            elif floor1["waterFountain"]["FirstInteraction"] == True:
                jump waterFountain2nd
            else:
                jump waterFountain1st

        "Head out to the hallway.":
            play sound "audio/walking_heels_echo.mp3" volume 0.5 fadeout 1.5
            $ renpy.pause(7.0)
            stop sound
            jump hallway1st

label returnToClassroom:
    scene classRoom
    with fade

    if floor1["LeaClassroom"]["insideClassRoom"] == True:
        "..."
    else: 
        # door sound as she enters
        play sound "audio/door_open.mp3"

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
                elif floor1["waterFountain"]["SsecondInteraction"] == True:
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
    # ensure ambience appropriate for hallway
    stop music fadeout 0.5
    play music "audio/night_ambience.mp3" fadein 1.0

    scene hallway1stFloor
    with fade

    # footsteps + subtle echo
    play sound "audio/footsteps_heels.mp3"
    "Lea walks back outside, it is still quiet, not even a cricket dares to break the tense air that fills the building."

    # distant wind
    play sound "audio/wind_hallway.mp3"

    "She looks around, though disoriented from the throbbing pain in her head, she mutters out to herself." 

    show lea default at right
    l "I should head out of here... I hope mom isn't worried."

    menu:
        "Head left, leave via the front doors.":
            play sound "audio/footsteps_heels.mp3"
            scene black
            with fade
            jump leftEntrance1
        "Head right, leave through the back doors.":
            play sound "audio/footsteps_heels.mp3"
            scene black
            with fade
            jump rightEntrance1

label leftEntrance1:
    scene black

    "Walking through the hall, she makes a turn to the left. Greeting her is the door, but something caught her eyes."

    scene hallwayBarricaded
    with fade

    play sound "audio/chair_scrape.mp3"
    "stacks and stacks of chairs pile upon the door. It is all over the place, futile to break down." 

    play sound "audio/heartbeat_slow.mp3"
    "She feels a rush of unease go through her."

    menu: 
        "Check the back door.":
            play sound "audio/footsteps_heels.mp3"
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
        "She remembers something. Reaching into her pockets, She takes out a key to a door."
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
    "Lea approaches the locked doors, it is chained and the knob was torn off."

    play sound "audio/chain_rattle.mp3"
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

    "It is the door to the exit, but it locked tight. chained with a lock and the knob is ripped right off. Lea tried kicking it."

    "Unfortunately, they aren't budging."

    show lea worried at right
    with fade 

    l "No..."
    
    l "No!"

    l "I need to find a way to get out of here!"

    if floor1["waterFountain"]["doorKeyObtained"] == True:
        hide lea 
        "She remembers something. Reaching into her pockets, She takes out a key to a door."
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
    
    menu:
        "Try again":
            # small click
            play sound "audio/fountain_click.mp3"
            jump waterFountain2nd
        "Return to the classroom.":
            play sound "audio/walking_heels_echo.mp3" volume 0.5 fadeout 1.5
            $ renpy.pause(7.0)
            stop sound
            if floor1["LeaClassroom"]["classroomFirstInteracted"] == True:
                scene black 
                with fade
                jump returnToClassroom
            else:
                scene black 
                with fade
                jump returnToClassroom1st

label waterFountain2nd:
    $ floor1["waterFountain"]["SsecondInteraction"] = True
    scene waterfountain
    with fade

    # quiet hum ambience while trying fountain
    play music "audio/quiet_hum.mp3" fadein 1.5

    play sound "audio/fountain_click.mp3"
    "She tries turning the water fountain on again, Lea hears the rushing of liquid, but nothing flows out."

    play sound "audio/drip_slow.mp3"
    "The faint echo of dripping pipes fills the hallway."

    menu:
        "Try again":
            
            scene black
            play sound "audio/fountain_click.mp3"
            stop music fadeout 1.0
            with fade
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
    scene waterfountainOozeFlowing
    with fade

    # tension swell music
    play sound "audio/tension_swell.mp3" fadein 1.5

    play sound "audio/fountain_click.mp3"
    "In a desperate attempt, Lea turns the water fountain on aggressively, and black unidentifiable liquid pours out."

    play sound "audio/liquid_splash.mp3"
    play sound "audio/heartbeat_fast.mp3"
    scene HallwayBack
    with fade

    show lea surprised at right
    "Lea stepped back, aghast by the sudden downpour." 
    
    show lea default at right
    
    l "Maybe they turned off the filters at night. Still...that's...disturbing."

    stop sound fadeout 2.0
    stop music fadeout 3.0

    menu:
        "Return to the classroom.":
            play sound "audio/walking_heels_echo.mp3" volume 0.5 fadeout 1.5
            $ renpy.pause(7.0)
            stop sound
            if floor1["LeaClassroom"]["classroomFirstInteracted"] == True:
                scene black 
                with fade
                jump returnToClassroom
            else:
                scene black 
                with fade
                jump returnToClassroom1st

label waterFountainInteracted:
    scene waterFountainBlackStained
    with fade

    play music "audio/ambient_silence.mp3" fadein 2.0
    play sound "audio/drip_slow.mp3"

    if floor1["waterFountain"]["doorKeyObtained"] == True :
        "Lea looks over to the water fountain."

        "The black ooze is gone."

        "Its stains are left as a gentle reminder to not drink from it."

        scene HallwayBack
        show lea worried at right
        with fade 

        l "..."
    else:
        "The ooze makes their way to the fountain's drain."

        "What remained was a key from the fountain, Lea is not sure how it managed to pop out of the water fountain's small spout."

        "She hesitantly picks the key up"

        "*You obtained a Door Key.*"
        $ floor1["waterFountain"]["doorKeyObtained"] = True 

    menu: 
        "Return to the classroom.":
            play sound "audio/walking_heels_echo.mp3" volume 0.5 fadeout 1.5
            $ renpy.pause(7.0)
            stop sound
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
            elif floor1["waterFountain"]["SsecondInteraction"] == True:
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
            jump HallwayFloor2Right 

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
    else:
        show lea default at right
        with dissolve
        l "I think I already searched the chairs enough."
    
    if floor1["Room2"]["chairChecking"] < 3:
        $ floor1["Room2"]["chairChecking"] += 1

label whiteboardRoom2:


label ClassroomFloor1Room3:
    if floor1["Room3"]["isRoomFound"] == False:
        "Lea heads to the left side, twisting the knobs of each of the rooms."

        "Locked."

        "Locked."

        "Locked."

        "One creaks open, the room is available."

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

    $ floor1["Room3"]["isRoomFound"] = True

