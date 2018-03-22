from sr.robot import *
import time

R = Robot()
R.gpio.pin_mode(1, INPUT_ANALOG)
while True:
    reading = R.gpio.analog_read(1) * (25 / 4096) #Scale the signal to a value out of 100
    R.motors[0].m0.power = reading
    R.motors[0].m1.power = reading
    time.sleep(0.05)
