import threading
import time
from datetime import datetime
from BMP280 import BMP280


class Processor:
    def __init__(self):
        self.measuring_interval = 5  # sec
        self.output_interval = 30  # sec
        self.sensor = BMP280()
        self.mean_measurements()

    def mean_measurements(self):
        with open('data.txt', 'a') as datafile:
            print(str(datetime.utcnow()) + ';' + str(self.sensor.read_pressure()) + ';' + str(
                self.sensor.read_temperature()))
            datafile.write(str(datetime.utcnow()) + ';' + str(self.sensor.read_pressure()) + ';' + str(
                self.sensor.read_temperature()) + '\r\n')
            threading.Timer(5, self.mean_measurements).start()
