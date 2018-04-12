from sr.robot import *
import time
R = Robot()

circumference = 0.26 * math.pi #c=pi*d
rot_time = circumference / 0.91 #circumference / speed of wheels = circumferences per sec
rot_speed = 360 / rot_time #degrees per second

def drive(dist=0, angle=0, _time=0): #dir in degrees
    if angle != 0:
        R.motors[0].m0.power = (120 * int(angle > 0)) - 60
        R.motors[0].m1.power = (120 * int(angle < 0)) - 60
        time.sleep(abs(angle) / rot_speed)
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0
    if dist != 0:
        R.motors[0].m0.power = 60
        R.motors[0].m1.power = 60
        time.sleep(dist / 0.91) #time = distance / speed
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0
    elif time != 0:
        R.motors[0].m0.power = 60
        R.motors[0].m1.power = 60
        time.sleep(_time)
        R.motors[0].m0.power = 0
        R.motors[0].m1.power = 0

while(True):
    markers = R.see()
    if len(markers) > 0:
        drive(dist=markers[0].dist, angle=markers[0].rot_y)
