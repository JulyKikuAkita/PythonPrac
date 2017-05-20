__author__ = 'July'
# http://agiliq.com/blog/2013/09/understanding-threads-in-python/
import time
import threading
from threading import Thread
from threading import Lock
lock = Lock()

class CreateListThreadBad(Thread):
    def run(self):
        self.entries = []
        for i in range(10):
            time.sleep(1)
            self.entries.append(i)
        print self.entries

def use_create_list_threadBad():
    start = time.time()
    for i in range(3):
        t = CreateListThreadBad()
        t.start()
    for t in threading.enumerate():
        if t is threading.current_thread():
            continue
        print "joining {}".format(t.getName())
        t.join()

    print "{} elapsed ".format(time.time() - start)

use_create_list_threadBad()

class CreateListThread(Thread):
    def run(self):
        self.entries = []
        for i in range(10):
            time.sleep(1)
            self.entries.append(i)
        lock.acquire()
        print self.entries
        print
        lock.release()

def use_create_list_thread():
    start = time.time()
    for i in range(3):
        t = CreateListThreadBad()
        t.start()

    for t in threading.enumerate():
        if t is threading.current_thread():
            continue
        print "joining {}".format(t.getName())
        t.join()

    print "{} elapsed ".format(time.time() - start)
#use_create_list_thread()