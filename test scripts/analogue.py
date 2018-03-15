import time

from sr.robot import *

LED_PIN = 2
R = Robot() #initialises the Robot
R.gpio.pin_mode(1, INPUT_ANALOG)
R.gpio.pin_mode(2, OUTPUT)
R.gpio.digital_write(2,0)


while True:
    reading = R.gpio.analog_read(1)
    print reading

    if (reading > 800):
        R.gpio.digital_write(LED_PIN, True)
    else:
        R.gpio.digital_write(LED_PIN, False)   
    
    time.sleep(0.5)

