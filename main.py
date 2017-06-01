import sys
import os
import logging
import time
import threading
import bmp280_median_logger as bl
logging.getLogger().setLevel(logging.INFO)


def main():
    """
    Keeps the daemon threads running until Process gets killed or keyboard interruption applies.
    """
    if len(sys.argv) > 1:
        bl.Bmp280Reader(sys.argv[1])
    else:
        logging.warning('No filename set. Use default data.txt.')
        bl.Bmp280Reader('data.txt')
        logging.info('BMP 280 logging daemon started on PID ' + str(os.getpid()) + '.')


if __name__ == "__main__":
    t = threading.Thread(target=main)
    t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info('Main thread killed.')
        sys.exit()
