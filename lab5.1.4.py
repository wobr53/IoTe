import time
import wiringpi
import sys
def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.3)
    wiringpi.digitalWrite(_pin, 0)    # Write 1 ( HIGH ) to pin
#SETUP
print("Start")
pin = 2
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )
#MAIN
for i in range(0,4):
    for j in range(0,3):
        blink(pin)
        pin += 1
    for k in range(0,3):
        blink(pin)
        pin -= 1
#cleanup
print("Done")
