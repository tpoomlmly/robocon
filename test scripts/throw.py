#requires you to put a cube in its claws
#make sure there is at least 3m of space!

from sr.robot import *
import time
import smbus

R = Robot.setup()
R.init(smbus.SMBus(1))
for i in range(3):
    R.servos[i] = 0
R.wait_start()

R.motors[0].m0.power = 100
R.motors[0].m1.power = 100
time.sleep(1.5)
R.servos[0] = 100
time.sleep(0.5)
R.servos[1] = -40
R.servos[0] = 0
time.sleep(1)
R.motors[0].m0.power = 0
R.motors[0].m1.power = 1
time.sleep(0.3)
R.servos[1] = 0
