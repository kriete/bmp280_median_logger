import datetime as dt
import pandas as pd
import threading
import numpy as np


def write_data(w_time, w_temp, w_pres):
    with open('data.txt', 'a') as datafile:
        datafile.write(w_time + ';' + str(w_temp) + ';' + str(w_pres) + '\n')


class MyDataStorage:

    def __init__(self):
        cur_time = dt.datetime.utcnow()
        self.time_index = pd.date_range(cur_time, periods=60, freq='1S')
        columns = ['T', 'P']
        data = np.empty((60, 2,))
        data.fill(np.nan)
        self.index = 0
        self.storage = pd.DataFrame(index=self.time_index, columns=columns, data=data)
        self.mean_data()
        self.read_data()

    def read_data(self):
        #print(str(dt.datetime.utcnow()))
        self.storage.iloc[self.index] = [np.random.randint(30, size=1)[0], np.random.randint(10, size=1)[0]+1000]
        self.index = self.index + 1
        threading.Timer(1, self.read_data).start()

    def mean_data(self):
        #print(str(dt.datetime.utcnow()))
        #print(self.storage)
        write_data(str(self.storage.index[int(np.fix(10/2))]), np.nanmedian(self.storage['T']), np.nanmedian(self.storage['P']))
        cur_time = dt.datetime.utcnow()
        self.time_index = pd.date_range(cur_time, periods=60, freq='1S')
        columns = ['T', 'P']
        data = np.empty((60, 2,))
        data.fill(np.nan)
        self.index = 0
        self.storage = pd.DataFrame(index=self.time_index, columns=columns, data=data)
        threading.Timer(60, self.mean_data).start()


def f():
    # do something here ...
    # call f() again in 60 seconds
    threading.Timer(10, f).start()
    print(str(dt.datetime.utcnow()))


def t():
    threading.Timer(2, t).start()
    print(str(dt.datetime.utcnow()))


def main():
    #f()
    #t()
    MyDataStorage()


if __name__ == "__main__":
    main()



