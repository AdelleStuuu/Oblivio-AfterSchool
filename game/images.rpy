# Explicit image definitions to ensure scene names map to files.
# If your Ren'Py version doesn't support WebP, convert to PNG/JPG and update the filenames.


# intro 
image chairZoomed:
    "chairZoomed.webp"
image chairUnzoomed:
    "chairUnzoomed.webp"


# lea expressions
#image legacyLea default:
#    "Lea/lea default.webp"
#    zoom .5
#image legacyLea headHurt:
#    "Lea/lea headHurt.webp"
#    zoom .5 
#image legacyLea defaultZoomed:
#    "Lea/lea default.webp"

transform yOffset:
    yoffset 50

image lea default:
    "Lea/lea default.webp"
    yOffset
    zoom .5
image lea headHurt:
    "Lea/lea headHurt.webp"
    yOffset
    zoom .5 
image lea smiling:
    "Lea/lea smiling.webp"
    yOffset
    zoom .5 
image lea worried:
    "Lea/lea worried.webp"
    yOffset
    zoom .5 
image lea scared:
    "Lea/lea scared.webp"
    yOffset
    zoom .5 
image lea surprised:
    "Lea/lea surprised.webp"
    yOffset
    zoom .5

image notLea:
    "Lea/notLea.webp"
    zoom 2
    yoffset 700

image ShatteredLea:
    "Endings/Shattered.webp"
    yoffset 800
    zoom 2
image UnifiedLea:
    "Endings/Unified.webp"
    yoffset 1500
    zoom 1.8

#items
image bathroomKey:
    "Items/DoorKey.webp"
image note:
    "Items/note.webp"

#hallways 

## FLOORS
image hallway1stFloor:
    "hallway1stFloor.webp"
image hallway2ndFloor:
    "hallway2ndFloor.webp"
image hallway3rdFloor:
    "hallway3rdFloor.webp"

## INTRETACTIONS
image HallwayBack:
    "hallway1stFloor.webp"
image HallwayStalking:
    "HallwayStalking.webp"
image hallwayBarricadedZoomed:
    "HallwayBarricaded.webp"
image LeftHallway:
    "LeftHallway.webp"
image hallwayBarricaded:
    "LeftHallway.webp"
image hallwayLocked:
    "hallwayLocked.webp"
image hallwayInteraction:
    "hallwayInteraction.webp"

#rooms
image Classroom1:
    "Classroom1.webp"
image Classroom2:
    "Classroom2.webp"
image BathroomOpen:
    "BathroomOpen.webp"
image BathroomOutside:
    "BathroomOutside2.webp"
image BathroomUnity:
    "BathroomUnity.webp"
image Library:
    "Library.webp"

#water fountain
image waterFountain:
    "waterFountain.webp"
image waterFountainOozeFlowing:
    "waterFountainOozeFlowing.webp"

#hospital 
image Hospital1:
    "Hospital1.webp"
image Hospital2:
    "Hospital2.webp"