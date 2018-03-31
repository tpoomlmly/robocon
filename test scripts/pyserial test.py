import serial
import time

ser = serial.Serial("COM3", 9600)
time.sleep(2)
while(True):
    ser.write(b'1')
    time.sleep(0.5)
    ser.write(b'0')
    time.sleep(0.5)
