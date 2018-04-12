import time
import smbus
from sr.robot import *

R = Robot.setup()
R.init(smbus.SMBus(1))
for i in range(4):
    R.servos[i] = 0
R.wait_start()

R.gpio.pin_mode(1, INPUT_ANALOG)

while True:
    reading = int(R.gpio.analog_read(1) *(100.0/8192.0) - 100)
    print reading
    R.servos[1] = reading
    time.sleep(0.1)
