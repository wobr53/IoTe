import time
import wiringpi
import sys
def blink(_pin1, _pin2):
    wiringpi.digitalWrite(_pin1, 1)    # Write 1 ( HIGH ) to pin
    wiringpi.digitalWrite(_pin2, 1)
    time.sleep(1)
    wiringpi.digitalWrite(_pin1, 0)    # Write 1 ( HIGH ) to pin
    wiringpi.digitalWrite(_pin2, 0)
    time.sleep(1)
#SETUP
print("Start")
pin1 = 2
pin2 = 4
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin1, 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(pin2, 1)
#MAIN
for i in range(0,10):
    if i%2 == 0:
        pin1 = 2
        pin2 = 4
    else:
        pin1 = 3
        pin2 = 5
    blink(pin1, pin2)
#cleanup
print("Done")
