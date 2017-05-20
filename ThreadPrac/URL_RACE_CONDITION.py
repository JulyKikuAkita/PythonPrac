__author__ = 'July'
# http://agiliq.com/blog/2013/09/understanding-threads-in-python/


#define a global variable
from threading import Thread
from threading import Lock
some_var = 0
lock = Lock()

class IncrementThreadRace(Thread):
    def run(self):
        #we want to read a global variable
        #and then increment it
        global some_var
        read_value = some_var
        print "some_var in %s is %d" % (self.name, read_value)
        some_var = read_value + 1
        print "some_var in %s after increment is %d" % (self.name, some_var)

class IncrementThread(Thread):
    def run(self):
        #we want to read a global variable
        #and then increment it
        global some_var
        lock.acquire()
        read_value = some_var
        print "some_var in %s is %d" % (self.name, read_value)
        some_var = read_value + 1
        print "some_var in %s after increment is %d" % (self.name, some_var)
        lock.release()

def use_increment_threadRace():
    threads = []
    for i in range(50):
        t = IncrementThreadRace()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "After 50 modifications, shared_var should have become 50"
    print "After 50 modifications, shared_var is %d" % (some_var,)

def use_increment_thread():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "After 50 modifications, shared_var should have become 50"
    print "After 50 modifications, shared_var is %d" % (some_var,)


use_increment_threadRace()
#use_increment_thread()