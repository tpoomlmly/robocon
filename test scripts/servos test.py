import time
import smbus
from sr.robot import *

#INITILISATION
R = Robot.setup()
#R.gpio.pin_mode(1, OUTPUT)# Transitor innitilization
R.init(smbus.SMBus(1))

#R.gpio.digital_write(1, True)# Power is allowed to flow into the servos
for i in range(3):
    R.servos[i] = 0
R.wait_start()

while True:
    #reading = int(R.gpio.analog_read(1) *(100.0/8192.0) - 100)
    R.servos[2] = 100
    time.sleep(1)
    R.servos[2] = -100
    time.sleep(1)
