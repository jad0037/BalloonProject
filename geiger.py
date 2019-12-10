"""
Created on Tue Nov  5 10:11:44 2019

@author: daven
"""
import time 
from time import sleep
def geiger():
    import threading 
    import RPi.GPIO as GPIO
    import time 
    from time import sleep
    global eventCount
    eventCount = 0
    GPIO.setmode(GPIO.BOARD)
    GeigerPin  = 8 #This is GPIO 0 it is also BCM 17 and Header 11
    GPIO.setup(GeigerPin, GPIO.IN)
    def eventWrite(k):
        global eventCount
        eventCount = eventCount + 1
        print (eventCount)
    def detect():
        global eventCount
        GPIO.add_event_detect(GeigerPin, GPIO.FALLING, eventWrite)
    def asleep():
        time.sleep(10)
        GPIO.remove_event_detect(GeigerPin) 
    t1 = threading.Thread(target=detect)  
    t2 = threading.Thread(target=asleep)  
    t1.start()
    t2.start()
    time.sleep(10)

 
    return eventCount

