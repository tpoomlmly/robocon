#need to add steering
import time
from math import pi

circumference = 0.26 * math.pi #c=pi*d
rot_time = circumference / 0.64 #circumference / speed of wheels = circumferences per sec
rot_speed = 360 / rot_time #

def drive(dist=0, _dir=0, _time=0): #dir in degrees
    if dist != 0:
        #steering section - needs finishing
        R.motors[0].m0.power =
        time.sleep(_dir / rot_speed)
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

if __name__ == "__main__":
    from sr.robot import *
    R = Robot()
    while(True):
        markers = R.see()
        if len(markers) > 0:
            drive(dist=markers[0].dist)


