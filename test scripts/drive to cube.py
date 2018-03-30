from sr.robot import *
import time
R = Robot()

def drive(dist=0, _time=0):
    if dist != 0:
        R.motors[0].m0.power = 60
        R.motors[0].m1.power = 60
        time.sleep(dist / 0.91) #time = distance / speed
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0
    elif _time != 0:
        R.motors[0].m0.power = 60
        R.motors[0].m1.power = 60
        time.sleep(_time)
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0

while(True):
    markers = R.see()
    if len(markers) > 0:
        drive(dist=markers[0].dist)
