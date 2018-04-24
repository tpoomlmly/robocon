from sr.robot import *

R = Robot()

while True:
    R.motors[0].m0.power = 60
    R.motors[0].m1.power = -60
