# BMP280 Median Logger

This python package logs data from the I2C connected Bosch BMP280.
It runs read and write threads in daemon mode. The read-and write processes are indepent of time-shifting.
The package is configured as follows:
- send a read-command every second to BMP280 for 60 seconds
- take the median value and store it into the specified file

### Installation

This package requires numpy and python to run. The Adafruit BMP280 python library originates from https://github.com/bastienwirtz/Adafruit_Python_BMP.

Navigate to the diretory and run the pip install with the -e flag (in case of own changes to the package)
```sh
$ pip install -e .
```

### Example Run

To start the logging, just navigate to the main directory and start the main.py. It keeps the daemon threads running until the main thread gets killed or a Keyboard Intteruption applies.
```sh
$ python main.py
```
or specify the filename with
```sh
$ python main.py bmpdata.txt
```