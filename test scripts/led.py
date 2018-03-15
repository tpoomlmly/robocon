import time

from sr.robot import *

R = Robot() #initialises the Robot

LED_PIN = 2 #Sets the LED to GPIO pin 2
R.gpio.pin_mode(LED_PIN, OUTPUT)

while True:
    R.gpio.digital_write(LED_PIN, True)
    time.sleep(1)
    R.gpio.digital_write(LED_PIN, False)
    time.sleep(1)

