import sys
import time
import Adafruit_DHT


while True:

    f = open("temp_file.txt", "w+")
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    data = temperature
    textdata = str(data)
    f.write(textdata+'\n')
    time.sleep(0.5)

f.close()
    
    
