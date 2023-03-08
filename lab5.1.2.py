import time
import wiringpi
import sys
def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(0.1)
#SETUP
print("Start")
pin = 2
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )
#MAIN
for i in range(0,30):
    blink(pin)
#cleanup
print("Done")
