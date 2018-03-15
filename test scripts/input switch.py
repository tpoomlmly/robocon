import time

from sr.robot import *

R = Robot() #initialises the Robot
R.gpio.pin_mode(4, INPUT_PULLUP)


while True:
    reading = R.gpio.digital_read(4)
    print reading
    time.sleep(0.1)

