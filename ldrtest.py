import time
import wiringpi
import sys

pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinSwitch, 0)

while True:
    if (wiringpi.digitalRead(pinSwitch) == 0):
        print("dark")
        time.sleep(0.5)
    else:
        print("light")
        time.sleep(0.5)