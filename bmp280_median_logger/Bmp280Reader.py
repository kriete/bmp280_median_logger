import datetime as dt
import pandas as pd
import threading
import numpy as np
import time


def write_data(filename, w_time, *args):
    """
    Writes str representations of input to specified file.

    :param filename: str
    :param w_time: str time representation
    :param args: args array
    """
    with open(filename, 'a') as datafile:
        datafile.write(w_time + ';%s' % ';'.join(map(str, args)) + '\n')


class Bmp280Reader:
    """
    Sends a read request to I2C connected BMP280 device every 1 second and stores the median value of 60 second
    observations in the specified filename.

     :param filename: str filename
    """
    def __init__(self, filename):
        self.filename = filename
        self.initiated = False
        self.next_read_call = time.time()
        self.next_write_call = time.time()
        cur_time = dt.datetime.fromtimestamp(self.next_write_call)
        self.time_index = pd.date_range(cur_time, periods=61, freq='1S')
        columns = ['T', 'P']
        data = np.empty((61, 2,))
        data.fill(np.nan)
        self.index = 0
        self.storage = pd.DataFrame(index=self.time_index, columns=columns, data=data)
        self.mean_data()
        self.initiated = True
        self.read_data()

    def read_data(self):
        self.storage.iloc[self.index] = [np.random.randint(30, size=1)[0], np.random.randint(10, size=1)[0]+1000]
        self.index = self.index + 1
        self.next_read_call = self.next_read_call + 1.0
        threading.Timer(self.next_read_call - time.time(), self.read_data).start()

    def mean_data(self):
        if not self.initiated:
            self.next_write_call = self.next_write_call + 60.0
            threading.Timer(self.next_write_call - time.time(), self.mean_data).start()
            return
        write_data(self.filename, str(self.storage.index[int(60/2)]), np.nanmedian(self.storage['T']), np.nanmedian(
            self.storage['P']))
        print(str(self.storage.index[int(60/2)]), np.nanmedian(self.storage['T']), np.nanmedian(
            self.storage['P']))
        print(self.storage)
        cur_time = dt.datetime.fromtimestamp(self.next_write_call)
        self.time_index = pd.date_range(cur_time, periods=61, freq='1S')
        columns = ['T', 'P']
        data = np.empty((61, 2,))
        data.fill(np.nan)
        self.index = 0
        self.storage = pd.DataFrame(index=self.time_index, columns=columns, data=data)
        self.next_write_call = self.next_write_call + 60.0
        threading.Timer(self.next_write_call - time.time(), self.mean_data).start()
