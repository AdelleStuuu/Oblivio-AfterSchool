# Character
define l = Character("Lea", color="#910b7f")

label start:
    $ FWatFounInteraction = firstHallwayFloor1Interaction = SWatFounInteraction = fromInsideClassroom = waterFountainInteracted = classroomFirstInteracted = doorKeyObtained = False
    $ chairCheckingfloor1Room2 = chairCheckingLeaClassRoom = 0 

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
            $ fromInsideClassroom = True
            jump returnToClassroom1st

# CLASSROOM INTERACTIONS

label returnToClassroom1st:
    scene classRoom
    with fade

    if fromInsideClassroom == True:
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
    $ classroomFirstInteracted = True

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
            if waterFountainInteracted == True:
                "Lea returns to the water fountain."
                jump waterFountainInteracted
            elif SWatFounInteraction == True:
                "Lea returns to the water fountain."
                jump waterFountain3rd
            elif FWatFounInteraction == True:
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

    if insideLeaClassRoom == True:
        "..."
    else: 
        # door sound as she enters
        play sound "audio/door_open.mp3"

        "Lea enters the classroom. It's the same room she attends every school day."

        "But it feels like everyone left in a hurry."

        "They've been gone for a while already."

    if firstHallwayFloor1Interaction == True:
        menu:
            "search the chairs.":
                jump chairsLeaClassroom
            "search the teacher's desk.":
                jump teachersDeskLeaClassroom
            "head back to the hallway.":
                jump hallwayFloor1
    else:
        menu:
            "Head out, head towards the water fountain.":
                scene black
                with fade
                if waterFountainInteracted == True:
                    "Lea returns to the water fountain."
                    jump waterFountainInteracted
                elif SWatFounInteraction == True:
                    "Lea returns to the water fountain."
                    jump waterFountain3rd
                elif FWatFounInteraction == True:
                    jump waterFountain2nd
                else:
                    jump waterFountain1st
            "Head out to the hallway.":
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

    if doorKeyObtained == True:
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

    if doorKeyObtained == True:
        hide lea 
        "She remembers something. Reaching into her pockets, She takes out a key to a door."
        show lea worried at right
        l "Maybe there is something here that this key can open to."

    menu:
        "Return to the middle of the hallway.":
            jump hallwayFloor1 

# WATER FOUNTAIN INTERACTIONS
label waterFountain1st:
    $ FWatFounInteraction = True
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
            if classroomFirstInteracted == True:
                scene black 
                with fade
                jump returnToClassroom
            else:
                scene black 
                with fade
                jump returnToClassroom1st

label waterFountain2nd:
    $ SWatFounInteraction = True
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
            if classroomFirstInteracted == True:
                scene black
                with fade
                jump returnToClassroom
            else:
                scene black
                with fade
                jump returnToClassroom1st

label waterFountain3rd:
    $ waterFountainInteracted = True
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
            if classroomFirstInteracted == True:
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
    if doorKeyObtained == True:
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
        $ doorKeyObtained = True 

    menu: 
        "Return to the classroom.":
            play sound "audio/walking_heels_echo.mp3" volume 0.5 fadeout 1.5
            $ renpy.pause(7.0)
            stop sound
            if classroomFirstInteracted == True:
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
    if firstHallwayFloor1Interaction == True:
        "The hallway is silent."
        
        "Cackling sounds of her shoe's heels are what accompanies her as she walks through the halls devoid of life besides her own."
    else:
        "The air is tight, but time spent idling around here is time wasted on finding something to get out of here "
        $ firstHallwayFloor1Interaction = True

    "What to do now?"
    menu:
        "Approach the classrooms.":
            jump floor1Classrooms
        "Check each end of the hallways.":
            jump floor1Hallways
        "Approach the water fountain.":
            if waterFountainInteracted == True:
                "Lea returns to the water fountain."
                jump waterFountainInteracted
            elif SWatFounInteraction == True:
                "Lea returns to the water fountain."
                jump waterFountain3rd
            elif FWatFounInteraction == True:
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

    $ insideLeaClassRoom = True

    "Checking each chair, she spends her time looking for anything useful here."

    if chairCheckingLeaClassRoom == 0:
        "..."

        "The first row had nothing of value."

        l "Not Good... There's nothing here."

        l "I should continue checking."
        $ chairCheckingLeaClassRoom += 1
    
    jump returnToClassroom
    



label teachersDeskLeaClassroom:
    scene black 
    with fade 

    $ insideLeaClassRoom = True

    ""

label ClassroomFloor1Room2:
    scene black 
    with fade 
    if room2Found == False:
        "Lea heads to the right side, twisting the knobs of each of the rooms."

        "Locked."

        "Locked."

        "Locked."

        "One creaks open, the room is available."

    $ room2Found = True

    "She carefully walks inside the door, no one was there to greet her. The chairs are tilted in such a way that it seemed like everyone left in a panic."

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
            scene black 
            with fade
            jump hallwayFloor1

label chairsRoom2:

label whiteboardRoom2:


label ClassroomFloor1Room3:
    if room3Found == False:
        "Lea heads to the left side, twisting the knobs of each of the rooms."

        "Locked."

        "Locked."

        "Locked."

        "One creaks open, the room is available."

    $ room3Found = True