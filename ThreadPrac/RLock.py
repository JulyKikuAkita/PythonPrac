__author__ = 'July'
# http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_RLock_Objects_ReEntrant_Locks.php
import threading
import time
import logging

FORMAT = '[%(levelname)s %(asctime)-8s]  (%(threadName)-30s)  %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, )

lock = threading.Lock()
rlock = threading.RLock()

print 'First try :', lock.acquire()
print 'Second try:', lock.acquire(0)
print "print this if not blocked..."

print 'Third try:', lock.acquire(0)   #not print anything, busy waiting
print "print this if not blocked..."


print 'First try :', rlock.acquire()
print 'Second try:', rlock.acquire(0)
print "print this if not blocked..."

print 'Third try:', rlock.acquire()   #Third try: 1  showing able to acquire lock
print "print this if not blocked..."