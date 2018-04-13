from sr.robot import *
from math import sin, cos, radians
R = Robot()

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
            if(5 >= marker.info.code >= 0):
                ydist = dist_from_wall
                xdist = dist_along_wall + staticMarkers[marker.info.code][0]
            elif(11 >= marker.info.code >= 6):
                ydist = dist_along_wall + staticMarkers[marker.info.code][1]
                xdist = staticMarkers[marker.info.code][0] - dist_from_wall
            elif(17 >= marker.info.code >= 12):
                xdist = staticMarkers[marker.info.code][0] - dist_along_wall
                ydist = staticMarkers[marker.info.code][1] - dist_from_wall
            else:
                ydist = dist_along_wall + staticMarkers[marker.info.code][1]
                xdist = dist_from_wall
            return xdist, ydist

def getBearing(marker_list):
    for marker in marker_list:
        if marker.info.marker_type == MARKER_TOKEN:
            return (int(17 >= marker.info.code >= 12) * 0 + int(11 >= marker.info.code >= 6) * 90 + int(5 >= marker.info.code >= 0) * 180 + 270) - marker.orientation.rot_y

if __name__ == "__main__":
    while(True):
        print get(R.see(res=(1296, 736)))
