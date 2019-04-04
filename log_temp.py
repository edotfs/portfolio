# Import libraries
import Adafruit_DHT
import datetime
import time

# Sensor model
sensor = Adafruit_DHT.DHT11
# Raspberry pin
pin = 23
# Log path
path = "/home/pi/Desktop/"

#Define a function to receive a record from a temperature sensor and save it
#in a file with certain format.
# * date + time + temperature + humidity
# * e.g. 2019-03-14 00:00:00 T=22.0 H=20.0
def log_update(record):
    log = open(path + "log_temp.log","a")
    line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + record + "\n"
    log.write(line)
    log.close()

#Read and review the record from a temperature sensor every five minutes.
#While the record is right, save it, otherwise save an error message.
try:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

            if humidity is not None and temperature is not None:
                    log_update("T=%s" % str(temperature) + " " +"H=%s" % str(humidity))

            else:
                    log_update("error")

            time.sleep(300)

except:
        log_update("error")

# Reference: https://github.com/adafruit/Adafruit_Python_DHT
