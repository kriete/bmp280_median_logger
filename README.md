# BMP280 Median Logger

This python package logs data from the I2C connected Bosch BMP280.
It runs read and write threads in daemon mode. The read-and-write processes are indepent of time-shifting.
The package is configured as follows:
- send a read-command of temperature and pressure every second to BMP280 for 60 seconds
- take the median value and store it into the specified file
 
Since the child-threads are daemons, they will terminate itself when the parent thread is killed. See example usage.

OrangePi setup with BMP280:
![](/img/setup.jpg?raw=true "OrangePi Setup")

### Installation
##### Requirements
This package requires numpy and pandas to run. Besides, it uses the Adafruit BMP280 python library (originating from https://github.com/bastienwirtz/Adafruit_Python_BMP). This file is included in the pacakge. However, this module uses the Adafruit Python GPIO https://github.com/adafruit/Adafruit_Python_GPIO.
To install it: clone the Adafruit Python GPIO repository and install it with:
```sh
$ git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
$ cd Adafruit_Python_GPIO
$ sudo python setup.py install
```

##### Logger
Navigate to the diretory and run the pip install with the -e flag (in case of own changes to the package)
```sh
$ pip install -e .
```


##### Note on OrangePi
Beware, which SMBUS is used (check with i2cdetect). The OrangePi uses SMBUS(0) (not 1). This must be edited in the Adafruit Python GPIO library in the source I2C.py before compiling.

### Example Run

To start the logging, just navigate to the main directory and start the main.py. It keeps the daemon threads running until the main thread gets killed by a kill command or a Keyboard Intteruption (CTRL-C) applies.
```sh
$ python main.py
```
or specify the filename with
```sh
$ python main.py bmpdata.txt
```