import Adafruit_DHT
import time

#iot
from time import sleep
import datetime
from firebase import firebase

import urllib2, urllib, httplib
import json
import os 
from functools import partial
#iot

#Air quality
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(27, GPIO.OUT)
#air quality

#rain
from time import sleep
from gpiozero import Buzzer, InputDevice
 
buzz    = Buzzer(13)
no_rain = InputDevice(18)
 
def buzz_now(iterations):
    for x in range(iterations):
        buzz.on()
        sleep(0.1)
        buzz.off()
        sleep(0.1)
#rain


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


#iot
firebase = firebase.FirebaseApplication('https://weather-station-rpi-a2800.firebaseio.com/', None)
#iot
 #temparature, humidity
while(True):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        
        #iot
        data = {"temp": temperature, "humidity": humidity}
	firebase.post('/temphumi/', data)
        #iot
        
     #rain   
    if not no_rain.is_active:
        print("It's raining - get the washing in!")
        buzz_now(5)    
        sleep(1)
        
        #iot
        data = {"temp": temperature, "humidity": humidity}
        firebase.post('/rain/', 'its raining')
        #iot
        
        #gas
    if GPIO.input(20):
         print('Cool environment')
         time.sleep(0.2)
    if GPIO.input(20)!=1:
         print('Detection GAS')
         GPIO.output(27, False)
         time.sleep(0.1)
         GPIO.output(27, True)
         
         #iot
        data = {"temp": temperature, "humidity": humidity}
	firebase.post('/gas/', 'detaction gas')
        #iot
    
  
   