from sr.robot import *
from math import sin, cos, radians, pi
import time

R = Robot.setup()
R.init(smbus.SMBus(1))
for i in range(3):
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
            if marker.info.marker_type == MARKER_TOKEN: #if a token
                if i == 0 or marker.dist < closest.dist: #This has to be this way because closest does not always have the attribute "dist"
                    closest = marker
                    i += 1
        #go to it
        drive(dist=closest.dist - 0.2, angle=closest.rot_y) #0.2 for clearance between camera and claw
        #pick it up

if __name__ == "__main__":
    while True:
        main()
