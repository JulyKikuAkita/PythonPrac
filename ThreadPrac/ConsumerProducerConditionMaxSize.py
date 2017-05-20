__author__ = 'July'
"""
Condition object allows one or more threads to wait until notified by another thread. Taken from here.
Consumer should wait when the queue is empty and resume only when it gets notified by the producer. 
Producer should notify only after it adds something to the queue. 
So after notification from producer, we can be sure that queue is not empty and hence no error can crop if consumer consumes.

Condition is always associated with a lock.
A condition has acquire() and release() methods that call the corresponding methods of the associated lock.
Condition provides acquire() and release() which calls lock's acquire() and release() internally, 
and so we can replace lock instances with condition instances and our lock behaviour will keep working properly.

Consumer needs to wait using a condition instance and producer needs to notify the consumer using the condition instance too. 
So, they must use the same condition instance for the wait and notify functionality to work properly.
"""

import threading
import random
import time
import logging

#setup global var
# Set up some global variables
logging.basicConfig(level=logging.DEBUG, format='( %(threadName) - 9s %(message)s',)
BUF_SIZE = 10
queue = []
num_fetch_threads = 2
condition = threading.Condition()

class ProducerThread(threading.Thread):

    def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, verbose = None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        nums = xrange(9)

        while True:
            condition.acquire()
            if len(queue) == BUF_SIZE:
                logging.debug("Queue full, producer is waiting")
                condition.wait()
                logging.debug("Space in queue, Consumer notified the producer")
            num = random.choice(nums)
            queue.append(num)
            logging.debug("Produced: " + str(num) + " in queue, current size " + str(len(queue)) )
            condition.notifyAll()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(threading.Thread):
    def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, verbose = None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            condition.acquire()
            if len(queue) == 0:
                logging.debug("Nothing in queue, consumer is waiting")
                condition.wait()
                logging.debug("Producer added something to queue and notified the consumer")
            num = queue.pop()
            logging.debug("consumed: " + str(num) + " in queue, current size " + str(len(queue)) )
            condition.notifyAll()
            condition.release()
            time.sleep(random.random())

ProducerThread(name = 'Producer').start()
ConsumerThread(name = 'Consumer').start()