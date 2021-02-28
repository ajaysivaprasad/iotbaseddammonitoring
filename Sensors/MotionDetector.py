import RPi.GPIO as GPIO
from time import sleep
import time
import datetime
from firebase import firebase
import urllib2, urllib, httplib
import json
import os 
from functools import partial

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
channel = 17
GPIO.setup(channel, GPIO.IN)
firebase = firebase.FirebaseApplication('https://iot-dam-monitoring-system.firebaseio.com/', None)
node = ""
check = "Movement Detected!"

def callback(channel):
        if GPIO.input(channel):
                print "Movement Detected!"
                node = "Movement Detected!"
                firebase.put('/CollectedData','VibrationLevel',node)
        else:
                 print "Movement Not Detected!"
                 node = "Movement Not Detected!"
                 firebase.put('/CollectedData','VibrationLevel',node)
                
       

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        if(node == check):
             node = ""
             firebase.put('/CollectedData','VibrationLevel',node)
             print "cleared"
             
            
        time.sleep(4)
