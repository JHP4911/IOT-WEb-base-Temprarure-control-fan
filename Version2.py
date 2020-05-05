#---------------------------------------Import Libraries---------------------------------------#
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

#---------------------------------------initialization-------------------------------#

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Read output from PIR motion sensor
GPIO.setup(11, GPIO.IN)
#LED output pin         
GPIO.setup(3, GPIO.OUT)
#set pin for usb fan         
GPIO.setup(40, GPIO.OUT)
#Define maximum/ minimum temperature
TEMP_MAX=40.0


while True:
    
        file = open("temp.txt", "r")
        status = file.read()
        print (status)
        #when on is clicked on web page  
        if status=='on':
          # turned fan on
           GPIO.output(40, 1)
           humidity, temperature = Adafruit_DHT.read_retry(11, 4)
           print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity) 
           # if temp is more than maximum temperature
           if temperature >= TEMP_MAX:
             #turned fan off
              GPIO.output(40, 0)  
              time.sleep(1)
        # when off is clicked on web page   
        elif status=='off':
             #calculate  motion sensor output 
             i=GPIO.input(11)
             #when no motion detected
             if i==0:
                GPIO.output(40, 0)
                print ("No intruders",i)
             #when motion detected   
             elif i==1:               
                print ("Intruder detected",i)
                GPIO.output(3, 1)  
                humidity, temperature = Adafruit_DHT.read_retry(11, 4)
                print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
                GPIO.output(40, 1)
                #off the fan if temp is greater than max/min temperature defined 
                if temperature >= TEMP_MAX:
                    GPIO.output(40, 0)  
                    time.sleep(1)
          
