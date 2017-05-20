__author__ = 'July'
import threading
import os
import sys


def dead_loop():
    while True:
        pass

#t = threading.Thread(target = dead_loop)
#t.start()
dead_loop()
#t.join()
print sys.setcheckinterval