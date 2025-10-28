define l = Character("Lea", color="#910b7f")

label start:
    $ FWatFounInteraction = SWatFounInteraction = fromInsideClassroom = False
    $ waterFountainInteracted = classroomFirstInteracted = doorKeyObtained = False 

    scene chairZoomed
    with fade

    "Lea woke up from her nap, her hair a mess from the deep sleep she had been in."

    scene chairUnzoomed
    with dissolve

    "There was nothing but the faint glow of moonlight and the weak neon light from the exit signs illuminating the hallways."

    show lea defaultZoomed at right
    with fade 

    l "God... What time is it?"

    "Lady Luck wasn't on her side today; her phone was dead."

    l "I must've slept for a long, long time."

    "She stood up and stumbled, catching herself on something nearby."

    l "Right — I skipped lunch earlier."

    "She held her temples."

    l "I need to get something to drink."

    menu:
        "Use the water fountain.":
            scene black 
            with fade
            jump waterFountain1st
        "Ignore your instincts, stay in the classroom.": 
            scene black
            with fade
            $ fromInsideClassroom = True
            jump returnToClassroom1st

# CLASSROOM INTERACTIONS

label returnToClassroom1st:
    scene classRoom
    with fade
    if  fromInsideClassroom == True:
        "Lea prepared to pack her belongings. The window outside showed a dark and cloudy night sky. Her brows furrowed."
    else:
        "Returning to the classroom she lounged by, Lea prepared to pack her belongings. The window outside showed a dark and cloudy night sky. Her brows furrowed." 

    show lea default at right
    with fade 

    l "It's not like anyone will be suspicious of me being out at night, but..."

    "She sighed."

    l "I just really want to get home. My head is killing me."
    $ classroomFirstInteracted = True
    menu:
        "Head out, drink at the water fountain.":
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
            jump hallway1st

label returnToClassroom:
    scene classRoom
    with fade
    "Lea enters the classroom. It's the same room she attends every school day."

    "But it feels like everyone left in a hurry."

    "They've been gone for a while already."

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
    scene hallway1stFloor
    with fade
    "Lea walks back outside, it is still quiet, not even a cricket dares to break the tense air that fills the building."
    
    "She looks around, though disoriented from the throbbing pain in her head, she mutters out to herself." 

    l "I should head out of here... I hope mom isn't worried."
    menu:
        "Head left, leave via the front doors.":
            scene black
            with fade
            jump leftEntrance1
        "Head right, leave through the back doors.":
            scene black
            with fade
            jump rightEntrance1

label leftEntrance1:
    scene black

    "Walking through the hall, she makes a turn to the left. Greeting her is the door, but something caught her eyes."

    scene hallwayBarricaded
    with fade

    "stacks and stacks of chairs pile upon the door. It is all over the place, futile to break down." 

    "She feels a rush of unease go through her."

    menu: 
        "Check the back door.":
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

    l "No... No!"

    l "I need to find a way to get out of here!"

    if doorKeyObtained == True:
        hide lea 
        "She remembers something. Reaching into her pockets, She takes out a key to a door."
        show lea worried at right
        l "Maybe there is something here that this key can open to."
    
    menu:
        "Return to the middle of the hallway.":
            jump hallwayMain 

label rightEntrance1:
    scene black
    "Walking through the hall, she makes a turn to the right. Greeting her is the back door, but something caught her eyes."

    scene hallwayLocked
    with fade 
    "Lea approaches the locked doors, it is chained and the knob was torn off."

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

    l "No... No!"

    l "I need to find a way to get out of here!"

    if doorKeyObtained == True:
        hide lea 
        "She remembers something. Reaching into her pockets, She takes out a key to a door."
        show lea worried at right
        l "Maybe there is something here that this key can open to."
    
    menu:
        "Return to the middle of the hallway.":
            jump hallwayMain 



# WATER FOUNTAIN INTERACTIONS
label waterFountain1st:
    $ FWatFounInteraction = True
    scene waterfountain 
    with fade
    "Lea steps on the pressure plate that activates the water fountain, nothing happens."
    
    menu:
        "Try again":
            jump waterFountain2nd
        "Return to the classroom.":
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
    "She tries turning the water fountain on again, Lea hear the rushing of liquid, but nothing flows out."
    
    menu:
        "Try again":
            scene black 
            with fade
            jump waterFountain3rd
        "Return to the classroom.":
            scene black 
            with fade
            if classroomFirstInteracted == True:
                jump returnToClassroom
            else:
                jump returnToClassroom1st
    

label waterFountain3rd:
    $ waterFountainInteracted = True
    scene waterfountainOozeFlowing
    with fade
    "In a desperate attempt, Lea turns the water fountain on aggressively, and black unidentifiable liquid pours out."
    scene HallwayBack

    show lea surprised at right

    "Lea stepped back, aghast by the sudden downpour." 
    
    show lea default at right
    
    l "Maybe they turn off the filters at night. Still...that's...disturbing."
   
    menu:
        "Return to the classroom.":
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
            if classroomFirstInteracted == True:
                scene black 
                with fade
                jump returnToClassroom
            else:
                scene black 
                with fade
                jump returnToClassroom1st