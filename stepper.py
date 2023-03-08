import time
import wiringpi
import sys
def wave(_pin1, _pin2, _pin3,_pin4):
    wiringpi.digitalWrite(_pin1, 1)
    time.sleep(0.01)    
    wiringpi.digitalWrite(_pin1, 0)
    wiringpi.digitalWrite(_pin2, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pin2, 0)
    wiringpi.digitalWrite(_pin3, 1)
    time.sleep(0.01)    
    wiringpi.digitalWrite(_pin3, 0)
    wiringpi.digitalWrite(_pin4, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pin4, 0)

def full(_pin1, _pin2, _pin3,_pin4):
    wiringpi.digitalWrite(_pin1, 1)
    wiringpi.digitalWrite(_pin2, 1)
    time.sleep(0.01)    
    wiringpi.digitalWrite(_pin1, 0)
    wiringpi.digitalWrite(_pin3, 1)
    time.sleep(0.01)   
    wiringpi.digitalWrite(_pin2, 0) 
    wiringpi.digitalWrite(_pin4, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pin3, 0)
    wiringpi.digitalWrite(_pin1, 1)
    time.sleep(0.01)
    wiringpi.digitalWrite(_pin4, 0)
    wiringpi.digitalWrite(_pin1, 0)
    

#SETUP
print("Start")
pin1 = 3
pin2 = 4
pin3 = 6
pin4 = 9 
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin1, 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(pin2, 1)
wiringpi.pinMode(pin3, 1)
wiringpi.pinMode(pin4, 1)
#MAIN
for i in range(200):
    #wave(pin1, pin2, pin3, pin4)
    full(pin1, pin2, pin3, pin4)    
#cleanup
print("Done")