import time
from sr.robot import *

R = Robot.setup()
R.init()
R.servos[0] = 0
R.wait_start()

R.gpio.pin_mode(1, INPUT_ANALOG)

while True:
    reading = R.gpio.analog_read(1) *(100.0/8192.0) - 100
    print reading
    R.servos[0] = reading
    time.sleep(0.1)
