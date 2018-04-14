from sr.robot import *
from math import sin, cos, radians
R = Robot()

staticMarkers = [(0.5, 0, 0.05), (1.5, 0, 0.05), (2.5, 0, 0.05),
                 (3.5, 0, 0.05), (4.5, 0, 0.05), (5.5, 0, 0.05),
                 (6, 0.5, 0.05), (6, 1.5, 0.05), (6, 2.5, 0.05),
                 (6, 3.5, 0.05), (6, 4.5, 0.05), (6, 5.5, 0.05),
                 (5.5, 6, 0.05), (4.5, 6, 0.05), (3.5, 6, 0.05),
                 (2.5, 6, 0.05), (1.5, 6, 0.05), (0.5, 6, 0.05),
                 (0, 5.5, 0.05), (0, 4.5, 0.05), (0, 3.5, 0.05),
                 (0, 2.5, 0.05), (0, 1.5, 0.05), (0, 0.5, 0.05)]

def getPos(marker_list):
    easiest = None
    i = 0
    for marker in marker_list:
        if marker.info.marker_type == MARKER_ARENA:
            if (i == 0) or (abs(marker.orientation.rot_y) < abs(easiest.orientation.rot_y)):
                easiest = marker
                i += 1
    del i
            
    if easiest is not None:
        #xdist = marker.dist * sin(radians(abs(marker.rot_y) + marker.orientation.rot_y))
        #ydist = marker.dist * cos(radians(abs(marker.rot_y) + marker.orientation.rot_y))
        dist_from_wall = easiest.dist * cos(radians(easiest.orientation.rot_y - easiest.rot_y))
        dist_along_wall = 0 - (easiest.dist * sin(radians(easiest.orientation.rot_y - easiest.rot_y)))
        if(5 >= easiest.info.code >= 0):
            ydist = dist_from_wall
            xdist = dist_along_wall + staticMarkers[easiest.info.code][0]
        elif(11 >= easiest.info.code >= 6):
            ydist = dist_along_wall + staticMarkers[easiest.info.code][1]
            xdist = staticMarkers[easiest.info.code][0] - dist_from_wall
        elif(17 >= easiest.info.code >= 12):
            xdist = staticMarkers[easiest.info.code][0] - dist_along_wall
            ydist = staticMarkers[easiest.info.code][1] - dist_from_wall
        else:
            ydist = dist_along_wall + staticMarkers[easiest.info.code][1]
            xdist = dist_from_wall
        return xdist, ydist
    else:
        return easiest

def getBearing(marker_list):
    for marker in marker_list:
        if marker.info.marker_type == MARKER_ARENA:
            return (int(17 >= marker.info.code >= 12) * 0 + int(11 >= marker.info.code >= 6) * 90 + int(5 >= marker.info.code >= 0) * 180 + 270) - marker.orientation.rot_y

if __name__ == "__main__":
    while(True):
        print getPos(R.see(res=(1920, 1440)))
