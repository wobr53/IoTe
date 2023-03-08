import time
import wiringpi
import sys
def blink(_pin1, _pin2, _pin3,_pin4,ontime):
    wiringpi.digitalWrite(_pin1, 1)    # Write 1 ( HIGH ) to pin
    wiringpi.digitalWrite(_pin2, 1)
    wiringpi.digitalWrite(_pin3, 1)
    wiringpi.digitalWrite(_pin4, 1)
    time.sleep(ontime)
    wiringpi.digitalWrite(_pin1, 0)    # Write 1 ( HIGH ) to pin
    wiringpi.digitalWrite(_pin2, 0)
    wiringpi.digitalWrite(_pin3, 0)
    wiringpi.digitalWrite(_pin4, 0)
    time.sleep(0.5)
#SETUP
print("Start")
pin1 = 2
pin2 = 3
pin3 = 4
pin4 = 5 
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin1, 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(pin2, 1)
wiringpi.pinMode(pin3, 1)
wiringpi.pinMode(pin4, 1)
#MAIN
for i in range(0,10):
    blink(pin1, pin2, pin3, pin4, 0.5)
    blink(pin1, pin2, pin3, pin4, 1.5)
    blink(pin1, pin2, pin3, pin4, 0.5)
#cleanup
print("Done")
