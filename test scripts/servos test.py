import time
import smbus
from sr.robot import *

R = Robot.setup()
R.init(smbus.SMBus(1))

#R.gpio.digital_write(1, True)# Power is allowed to flow into the servos
for i in range(3):
    R.servos[i] = 0
R.wait_start()

while True:
    #reading = int(R.gpio.analog_read(1) *(100.0/8192.0) - 100)
    R.servos[1] = 30
    print "open"
    time.sleep(1)
    R.servos[1] = -80
    print "close"
    time.sleep(1)
