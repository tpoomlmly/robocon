from sr.robot import *
from math import sin, cos, radians, pi
import time
import gotocoords
R = Robot.setup()
R.init()
for i in range(4):
    R.servos[i] = 0 #stop all servos from rotating
R.wait_start()

def main():
    #begin seek phase
    markers = R.see(res=(1296, 736))
    xcoord, ycoord = 0.0 #initialise xcoord and ycoord
    if len(markers) > 0:
        xcoord, ycoord = find_coords.get(markers) #returns tuple
        #choose a marker
        closest = None
        i = 0
        for marker in markers:
            if marker.info.marker_type == MARKER_TOKEN: #if a token; MARKER_TOKEN may have to be made a string
                if i == 0:
                    closest = marker
                    i += 1
                elif marker.dist < closest.dist: #This has to be this way because closest does not always have the attribute "dist"
                    closest = marker
                    i += 1
        #go to it
        gotocoords.drive(dist=closest.dist - 0.2) #0.2 for clearance between camera and claw
        #pick it up


#Start of coordinate finding code
##class StaticMarker:
##    def __init__(self, uid, coordinates=(0, 0, 0)):
##        self.uid = uid
##        self.coordinates = coordinates
##        self.x = coordinates[0]
##        self.y = coordinates[1]
##        self.z = coordinates[2]

#Define all the markers - (uid: (x, y, z))
staticMarkers = [(0.5, 0, 0.3), (1.5, 0, 0.3), (2.5, 0, 0.3),
                 (3.5, 0, 0.3), (4.5, 0, 0.3), (5.5, 0, 0.3),
                 (6, 0.5, 0.3), (6, 1.5, 0.3), (6, 2.5, 0.3),
                 (6, 3.5, 0.3), (6, 4.5, 0.3), (6, 5.5, 0.3),
                 (5.5, 6, 0.3), (4.5, 6, 0.3), (3.5, 6, 0.3),
                 (2.5, 6, 0.3), (1.5, 6, 0.3), (0.5, 6, 0.3),
                 (0, 5.5, 0.3), (0, 4.5, 0.3), (0, 3.5, 0.3),
                 (0, 2.5, 0.3), (0, 1.5, 0.3), (0, 0.5, 0.3)]

def get(marker_list):
    for marker in marker_list:
        if marker.info.marker_type == MARKER_TOKEN:
            #xdist = marker.dist * sin(radians(abs(marker.rot_y) + marker.orientation.rot_y))
            #ydist = marker.dist * cos(radians(abs(marker.rot_y) + marker.orientation.rot_y))
            dist_from_wall = marker.dist * cos(radians(marker.orientation.rot_y - marker.rot_y))
            dist_along_wall = 0 - (marker.dist * sin(radians(marker.orientation.rot_y - marker.rot_y)))
            if (marker.info.code >= 0) and (marker.info.code <= 5):
                ydist = dist_from_wall
                xdist = dist_along_wall + staticMarkers[marker.info.code][0]
            elif (marker.info.code >= 6) and (marker.info.code <= 11):
                ydist = dist_along_wall + staticMarkers[marker.info.code][1]
                xdist = staticMarkers[marker.info.code][0] - dist_from_wall
            elif (marker.info.code >= 12) and (marker.info.code <= 17):
                xdist = staticMarkers[marker.info.code][0] - dist_along_wall
                ydist = staticMarkers[marker.info.code][1] - dist_from_wall
            else:
                ydist = dist_along_wall + staticMarkers[marker.info.code][1]
                xdist = dist_from_wall
            return xdist, ydist

##Usage:
##markers = R.see()
##xdist, ydist = get(markers)
##print "x: " + str(xdist)
##print "y: " + str(ydist)
#end of coordinate finding code

#start of driving code
#need to add steering
import time
from math import pi

circumference = 0.26 * math.pi #c=pi*d
rot_time = circumference / 0.64 #circumference / speed of wheels = circumferences per sec
rot_speed = 360 / rot_time #

def drive(dist=0, angle=0, _time=0): #dir in degrees
    if dist != 0:
        #steering section - needs finishing
        R.motors[0].m0.power =
        R.motors[0].m1.power = 
        time.sleep(angle / rot_speed)
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0
        #end steering section
        R.motors[0].m0.power = 42
        R.motors[0].m1.power = 42
        time.sleep(dist / 0.64) #time = distance / speed
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0
    elif time != 0:
        R.motors[0].m0.power = 42
        R.motors[0].m1.power = 42
        time.sleep(_time)
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0

#Usage:
#drive(dist=markers[0].dist)
#end of driving code

if __name__ == "__main__":
    while True:
        main()
