from sr.robot import *
from math import sin, cos, radians
R = Robot()

class StaticMarker:
    def __init__(self, uid, coordinates=(0, 0, 0)):
        self.uid = uid
        self.coordinates = coordinates

origin = StaticMarker(0, (0, 0, 0))
m1 = StaticMarker(1, (1, 0, 0))

while True:
    markers = R.see()

    for marker in markers:
        if(marker.info.code == origin.uid):
            xdist = marker.dist * sin(radians(abs(marker.rot_y) + marker.orientation.rot_y))
            ydist = marker.dist * cos(radians(abs(marker.rot_y) + marker.orientation.rot_y))
            print "x: " + str(xdist)
            print "y: " + str(ydist)
