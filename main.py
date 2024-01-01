#!/usr/bin/env python

import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import LCD1602
GPIO.setmode(GPIO.BCM)
reader = SimpleMFRC522()
LCD1602.init()
GPIO.setup(17, GPIO.OUT) 
Buzz = GPIO.PWM(17, 1100)

def main():
    while True:
        print("Reading...Please place the card...")
        LCD1602.write(0, 0, 'Place the card')
        id, text = reader.read()
        LCD1602.clear()
        if id ==1034764361154:
            LCD1602.write(0, 0, 'Success')
            time.sleep(4)
            LCD1602.clear()
        else:#Access Denied section
            LCD1602.write(0, 0, 'Access Denied')
            Buzz.start(50)
            time.sleep(2)
            Buzz.stop()
            time.sleep(8)
            LCD1602.clear()
            
        
            
        time.sleep(3)
        
def destroy():
    GPIO.cleanup()
    LCD1602.clear()
    
if __name__ == '__main__':
    try:
        main()
    # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
