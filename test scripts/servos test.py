import time
import smbus
from sr.robot import *

#INITILIZATION
R = Robot.setup()
for i in range(3):
    R.gpio.pin_mode(i + 2, OUTPUT)# Transitor innitilization
R.init(smbus.SMBus(1))

#
for i in range(3):
    R.gpio.digital_write(i+2, True)# Power is allowed to flow into the servos
    R.servos[i] = 0
R.wait_start()

R.gpio.pin_mode(1, INPUT_ANALOG)

while True:
    reading = int(R.gpio.analog_read(1) *(100.0/8192.0) - 100)
    print reading
    R.servos[1] = reading
    time.sleep(0.1)
