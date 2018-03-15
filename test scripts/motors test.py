from sr.robot import *
import time

R = Robot()
R.gpio.pin_mode(1, INPUT_ANALOG)
while True:
    reading = R.gpio.analog_read(1) / 256
    R.motors[0].m0.power = reading
    R.motors[0].m1.power = reading
    time.sleep(0.05)
