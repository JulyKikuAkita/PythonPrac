__author__ = 'July'
import threading
import time
import logging
import random
import Queue
'''
from redis import Redis
from rq import Queue
'''
from functools import partial
from multiprocessing.pool import Pool

# Below example implement P-C using Queue.Queue - a sync queue class
# Queue encapsulates the behaviour of Condition, wait(), notify(), acquire() etc.
# https://docs.python.org/2/library/queue.html
# Java - blocking queue : http://tutorials.jenkov.com/java-concurrency/blocking-queues.html
"""
http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Producer_Consumer_using_Queue.php

The producer's job is to generate a piece of data, put it into the buffer and start again.
At the same time, the consumer is consuming the data (i.e., removing it from the buffer) one piece at a time

The problem describes two processes, the producer and the consumer, who share a common,
fixed-size buffer used as a queue.

In place of list, we are using a Queue instance(hereafter queue).
queue has a Condition and that condition has its lock. You don't need to bother about Condition and Lock if you use Queue.
Producer uses put available on queue to insert data in the queue.
put() has the logic to acquire the lock before inserting data in queue.
Also put() checks whether the queue is full. If yes, then it calls wait() internally and so producer starts waiting.
Consumer uses get.
get() acquires the lock before removing data from queue.
get() checks if the queue is empty. If yes, it puts consumer in waiting state.
get() and put() has proper logic for notify() too.

"""

# Set up some global variables
logging.basicConfig(level=logging.DEBUG, format='( %(threadName) - 9s %(message)s',)
BUF_SIZE = 3
q = Queue.Queue(BUF_SIZE)
num_fetch_threads = 2


class ProducerThread(threading.Thread):
    def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, verbose = None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name
        self.setDaemon(True)

    def run(self):
        cnt = 0
        while cnt < 10:
            if not q.full():
                item = random.randint(1, 9)
                q. put(item)
                cnt += 1
                logging.debug('Putting ' + str(item) + ': ' + str(q.qsize()) + ' in queue )')
                time.sleep(random.random())
        return

class ConsumerThread(threading.Thread):
    """This is the Worker thread function.
    It putting items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and only exit when
    the main thread ends.
    """
    def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, verbose = None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        self.setDaemon(True)

    def run(self):
        cnt = 0
        while True:
            if not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item) + ': ' + str(q.qsize()) + ' in queue )')
                cnt += 1
                time.sleep(random.random())
        return

if __name__ == '__main__':

    producer = ProducerThread(name = 'Producer')
    producer.start()
    time.sleep(2)

    for i in xrange(num_fetch_threads):
        name = 'consumer' + str(i)
        consumer = ConsumerThread(name = name)
        consumer.start()
        time.sleep(2)

    logging.debug('*** Main thread waiting')
    logging.debug(producer.isAlive())
    logging.debug('*** Done')







