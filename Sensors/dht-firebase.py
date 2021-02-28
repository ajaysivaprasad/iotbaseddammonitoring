import RPi.GPIO as GPIO
from time import sleep
import time
import datetime
from firebase import firebase
import Adafruit_DHT

import urllib2, urllib, httplib
import json
import os 
from functools import partial

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

sensor = Adafruit_DHT.DHT11

pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


firebase = firebase.FirebaseApplication('https://iot-dam-monitoring-system.firebaseio.com/', None)
#firebase.put("/dht", "/temp", "0.00")
#firebase.put("/dht", "/humidity", "0.00")

def update_firebase():

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        sleep(5)
        str_temp = ' {0:0.2f} *C '.format(temperature)  
        str_hum  = ' {0:0.2f} %'.format(humidity)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))  
            
    else:
        print('Failed to get reading. Try again!')  
        sleep(10)

    #data = {"temp": temperature, "humidity": humidity}
    firebase.put('/CollectedData','Temperature',temperature)
    firebase.put('/CollectedData','Humidity',humidity)
    


####################################################
TRIG = 23
ECHO = 24
def updateWaterLevel():
    #print "Distance Measurement In Progress"
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(26,GPIO.OUT)
    #print "Waiting For Sensor To Settle"
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    waterlevel = 44.4 - distance
    print "Water Level:",waterlevel,"cm"
    firebase.put('/CollectedData','WaterLevel',waterlevel)
    if(waterlevel>35 and waterlevel<=38):
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,GPIO.HIGH)
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,GPIO.LOW)
        GPIO.setup(19,GPIO.OUT)
        GPIO.output(19,GPIO.LOW)
    elif(waterlevel>38 and waterlevel<=40):
        GPIO.setup(19,GPIO.OUT)
        GPIO.output(19,GPIO.HIGH)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,GPIO.LOW)
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,GPIO.LOW)
    elif(waterlevel>40):
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,GPIO.HIGH)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,GPIO.LOW)
        GPIO.setup(19,GPIO.OUT)
        GPIO.output(19,GPIO.LOW)
    else:
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,GPIO.LOW)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,GPIO.LOW)
        GPIO.setup(19,GPIO.OUT)
        GPIO.output(19,GPIO.LOW)
        
while True:
        update_firebase()
        updateWaterLevel()
   
        #sleepTime = int(sleepTime)
        sleep(5)
