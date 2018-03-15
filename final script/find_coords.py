from math import sin, cos, radians

class StaticMarker:
    def __init__(self, uid, coordinates=(0, 0, 0)):
        self.uid = uid
        self.coordinates = coordinates
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

#Define all the markers - (x, y, z)
origin = StaticMarker(0, (0.5, 0, 0.3))
m1 = StaticMarker(1, (1.5, 0, 0.3))
m2 = StaticMarker(2, (2.5, 0, 0.3))
m3 = StaticMarker(3, (3.5, 0, 0.3))
m4 = StaticMarker(4, (4.5, 0, 0.3))
m5 = StaticMarker(5, (5.5, 0, 0.3))
m6 = StaticMarker(6, (6, 0.5, 0.3))
m7 = StaticMarker(7, (6, 1.5, 0.3))
m8 = StaticMarker(8, (6, 2.5, 0.3))
m9 = StaticMarker(9, (6, 3.5, 0.3))
m10 = StaticMarker(10, (6, 4.5, 0.3))
m11 = StaticMarker(11, (6, 5.5, 0.3))
m12 = StaticMarker(12, (5.5, 6, 0.3))
m13 = StaticMarker(13, (4.5, 6, 0.3))
m14 = StaticMarker(14, (3.5, 6, 0.3))
m15 = StaticMarker(15, (2.5, 6, 0.3))
m16 = StaticMarker(16, (1.5, 6, 0.3))
m17 = StaticMarker(17, (0.5, 6, 0.3))
m18 = StaticMarker(18, (0, 5.5, 0.3))
m19 = StaticMarker(19, (0, 4.5, 0.3))
m20 = StaticMarker(20, (0, 3.5, 0.3))
m21 = StaticMarker(21, (0, 2.5, 0.3))
m22 = StaticMarker(22, (0, 1.5, 0.3))
m23 = StaticMarker(23, (0, 0.5, 0.3))

def get(marker_list):
    for marker in marker_list:
        if(marker.info.code == origin.uid):
            xdist = marker.dist * sin(radians(abs(marker.rot_y) + marker.orientation.rot_y))
            ydist = marker.dist * cos(radians(abs(marker.rot_y) + marker.orientation.rot_y))
            return xdist, ydist

if __name__ == "__main__":
    from sr.robot import *
    R = Robot()
    markers = R.see()
    xdist, ydist = get(markers)
    print "x: " + str(xdist)
    print "y: " + str(ydist)
