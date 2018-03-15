from sr.robot import *
import find_coords
import gotocoords
R = Robot()

while True:
    #begin seek phase
    markers = R.see(res=(1296, 736))
    xcoord, ycoord = 0.0 #initialise xcoord and ycoord
    if len(markers) > 0:
        xcoord, ycoord = find_coords.get(markers) #returns tuple
        #choose a marker
        closest = None
        i = 0
        for marker in markers:
            if marker.info.marker_type = MARKER_TOKEN: #if a token; MARKER_TOKEN may have to be made a string
                if i == 0:
                    closest = marker
                    i += 1
                elif marker.dist < closest.dist: #This has to be this way because closest does not always have the attribute "dist"
                    closest = marker
                    i += 1
        #go to it
        gotocoords.drive(dist=closest.dist - 0.2) #0.2 for clearance between camera and claw
        #pick it up
