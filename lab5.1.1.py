import time
import wiringpi
import sys
def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.3)
    wiringpi.digitalWrite(_pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(0.3)
#SETUP
print("Start")
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )
#MAIN
i = 0
while i != 1:
    blink(pin)
#cleanup
print("Done")
