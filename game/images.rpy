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

#hallways 
image hallway1stFloor:
    "hallway1stFloor.webp"
image hallwayBarricadedZoomed:
    "HallwayBarricaded.webp"
image hallwayBarricaded:
    "LeftHallway.webp"

#water fountain
image waterFountain:
    "waterFountain.webp"
image waterFountainOozeFlowing:
    "waterFountainOozeFlowing.webp"