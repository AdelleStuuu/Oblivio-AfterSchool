define l = Character("Lea", color="#910b7f")
 


label start:
    $ FWatFounInteraction = SWatFounInteraction = False
    $ waterFountainInteracted = classroomFirstInteracted = False 

    scene hallway1stFloor
    "Lea woke up from her nap, hair all messed up from the deep sleep she was in. There was nothing but the faint glow of moonlight and the weak neon light from the exit signs illuminating the hallways."
    show lea nauseous at left
    l "God...What time is it?"

    "Lady luck wasn't on her side today, her phone was out of battery." 
    show lea default at left
    l "I must've slept for a long... long time." 

    "She stood up and stumbled, catching herself with the help of a nearby."

    l "Right, I skipped lunch too beforehand." 

    "She held the temples of her forehead," 
    
    l "I need to at least drink something." 

    menu:
        "Use the water fountain.":
            jump waterFountain1st
        "Ignore your senses, return to the classroom.": 
            jump returnToClassroom

# CLASSROOM INTERACTIONS
label returnToClassroom:
    scene classRoom 

    "Lea enters the classroom, it is still the same room that she heads to every single school day." 
    
    "But, it feels like everyone has left in a hurry."
    
    "And everyone has left for a while already."

    menu:
        "Head out, drink at the water fountain.":
            if waterFountainInteracted == True:
                "Lea Returns to the water fountain."
                jump waterFountainInteracted
            elif SWatFounInteraction == True:
                "Lea Returns to the water fountain."
                jump waterFountain3rd
            elif FWatFounInteraction == True:
                jump waterFountain2nd
            else:
                jump waterFountain1st
        "Head out to the hallway.":
            jump hallway1st

label returnToClassroom1st:
    scene classRoom

    "Returning to the classroom she lounged by, Lea prepared to pack her belongings. The window outside showed a dark and cloudy night sky. Her brows furrowed," 

    show lea default at left
    
    l "It's not like they're going to be suspicious of me being out at night but..." 

    "She sighs." 

    l "I just really want to get home. My head is killing me."
    $ classroomFirstInteracted = True
    menu:
        "Head out, drink at the water fountain.":
            if waterFountainInteracted == True:
                "Lea Returns to the water fountain."
                jump waterFountainInteracted
            elif SWatFounInteraction == True:
                "Lea Returns to the water fountain."
                jump waterFountain3rd
            elif FWatFounInteraction == True:
                jump waterFountain2nd
            else:
                jump waterFountain1st
        "Head out to the hallway.":
            jump hallway1st

# FIRST FLOOR HALLWAY 
# SCRIPTED SCENES ONLY 
label hallway1st:
    scene hallway1stFloor
    "Lea walks back outside, it is still quiet, not even a cricket dares to break the tense air that fills the building. She looks around, though disoriented from the throbbing pain in her head, she mutters out to herself." 

    l "I should head out of here... I hope mom isn't worried."
    menu:
        "Head left, leave via the front doors.":
            jump leftEntrance1
        "Head right, leave through the back doors.":
            jump rightEntrance1

label leftEntrance1:
    "Walking through the hall, she makes a turn to the left. Greeting her is the door, but something caught her eyes."
    scene hallwayBarricaded
    "stacks and stacks of chairs pile upon the door. It is all over the place, futile to break down." 
    "She feels a rush of unease go through her."
    menu: 
        "Check the back door.":
            jump rightEntrance2

label leftEntrance2:

label rightEntrance1:
    "Walking through the hall, she makes a turn to the right. Greeting her is the back door, but something caught her eyes."
    scene HallwayLocked
    "Lea approaches the locked doors, it is chained and the knob was torn off."
    "She feels a rush of unease go through her."
    menu: 
        "Check the front door.":
            jump leftEntrance2

label rightEntrance2:

# WATER FOUNTAIN INTERACTIONS
label waterFountain1st:
    $ FWatFounInteraction = True
    scene waterfountain 
    "Lea steps on the pressure plate that activates the water fountain, nothing happens."
    
    menu:
        "Try again":
            jump waterFountain2nd
        "Return to the classroom.":
            if classroomFirstInteracted == True:
                jump returnToClassroom
            else:
                jump returnToClassroom1st

label waterFountain2nd:
    $ SWatFounInteraction = True
    scene waterfountain
    "She tries turning the water fountain on again, Lea hear the rushing of liquid, but nothing flows out."
    
    menu:
        "Try again":
            jump waterFountain3rd
        "Return to the classroom.":
            if classroomFirstInteracted == True:
                jump returnToClassroom
            else:
                jump returnToClassroom1st
    

label waterFountain3rd:
    $ waterFountainInteracted = True
    scene waterfountainOozeFlowing
    "In a desperate attempt, Lea turns the water fountain on aggressively, and black unidentifiable liquid pours out."
    scene HallwayBack

    show lea surprised at left
    "Lea stepped back, aghast by the sudden downpour." 
    show lea default at left
    l "Maybe they turn off the filters at night. Still...that's...disturbing."
   
    menu:
        "Return to the classroom.":
            if classroomFirstInteracted == True:
                jump returnToClassroom
            else:
                jump returnToClassroom1st

label waterFountainInteracted:
    scene waterFountainBlackStained
    "Lea looks over to the water fountain."
    "The black ooze is gone."
    "Its stains are left as a gentle reminder to not drink from it."
    scene HallwayBack
    show lea default at left
    l "..."

    menu: 
        "Return to the classroom.":
            if classroomFirstInteracted == True:
                jump returnToClassroom
            else:
                jump returnToClassroom1st